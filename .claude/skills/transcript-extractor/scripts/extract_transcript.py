#!/usr/bin/env python3
"""
Transcript Extractor — Generic
Extrai transcrições de aulas hospedadas em plataformas de cursos online.
Suporta vídeos Vimeo (transcrição embutida) e YouTube (yt-dlp / browser).
Flexível: descobre aulas dinamicamente navegando no site.
"""

import sys
import os
import re
import subprocess
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
STATE_FILE = os.path.join(os.path.dirname(__file__), ".auth_state.json")

# ---------------------------------------------------------------------------
# JavaScript snippets
# ---------------------------------------------------------------------------
JS_LIST_LESSONS = """
Array.from(document.querySelectorAll('a'))
  .filter(a => a.href.includes('/item/'))
  .map(a => ({
    name: a.textContent.trim(),
    href: a.href,
    id: a.href.match(/item\\/(\\d+)/)?.[1] || null
  }))
  .filter(a => a.name && a.id)
"""

JS_GET_PAGE_TITLE = """
document.querySelector('h1, .lesson-title, .content-title, title')?.textContent?.trim() || document.title
"""

JS_GET_ALL_IFRAMES = """
Array.from(document.querySelectorAll('iframe')).map(f => ({src: f.src, id: f.id, name: f.name}))
"""

JS_GET_VIMEO_URL = """
Array.from(document.querySelectorAll('iframe'))
  .map(f => f.src)
  .find(s => s.includes('vimeo')) || "NOT_FOUND"
"""

JS_GET_YOUTUBE_ID = """
(() => {
  const iframes = Array.from(document.querySelectorAll('iframe'));
  for (const iframe of iframes) {
    const src = iframe.src || "";
    if (src.includes('youtube') || src.includes('youtube-nocookie')) {
      const match = src.match(/embed\\/([^?/]+)/);
      if (match) return match[1];
    }
  }
  return "NOT_YOUTUBE";
})()
"""

JS_EXTRACT_VIMEO_TRANSCRIPT = """
(async () => {
  // Click transcript button
  const btn = document.getElementById('transcript-control-bar-button');
  if (!btn) return "TRANSCRIPT_BUTTON_NOT_FOUND";
  btn.click();
  await new Promise(r => setTimeout(r, 2500));

  // Find transcript container
  const container = document.querySelector('[class*="TranscriptList_lazy_module_listContainer"]');
  if (!container) return "CONTAINER_NOT_FOUND";

  // Scroll through all cues (Vimeo uses virtualized/lazy list)
  const cuesMap = new Map();
  container.scrollTop = 0;
  await new Promise(r => setTimeout(r, 300));

  let lastScrollTop = -1;
  let iterations = 0;
  while (iterations < 200) {
    const visibleCues = document.querySelectorAll('[class*="TranscriptCue"]');
    visibleCues.forEach(el => {
      const text = el.querySelector('span:first-child')?.textContent.trim() || "";
      const time = el.querySelector('span:last-child')?.textContent.trim() || "";
      if (text) cuesMap.set(`${time}|${text}`, { time, text });
    });
    lastScrollTop = container.scrollTop;
    container.scrollTop += 800;
    await new Promise(r => setTimeout(r, 250));
    if (container.scrollTop === lastScrollTop) break;
    iterations++;
  }

  return Array.from(cuesMap.values()).map(c => c.text).join(' ');
})()
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def slugify(text):
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    # Normalize common Portuguese characters
    replacements = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e', 'í': 'i', 'ó': 'o',
        'ô': 'o', 'õ': 'o', 'ú': 'u', 'ü': 'u',
        'ç': 'c', 'ñ': 'n',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def format_transcript(title, module_name, url, text):
    """Format transcript into the standard markdown format."""
    return f"""# {title}
**Módulo:** {module_name}
**URL:** {url}

## Transcrição

{text.strip()}
"""


def parse_vtt(vtt_path):
    """Parse a .vtt file into clean text."""
    content = Path(vtt_path).read_text(encoding="utf-8")
    lines = content.split("\n")
    text_lines = []
    seen = set()

    for line in lines:
        line = line.strip()
        if not line or line.startswith("WEBVTT") or line.startswith("Kind:") or \
           line.startswith("Language:") or "-->" in line or line.isdigit():
            continue
        clean = re.sub(r"<[^>]+>", "", line)
        if clean and clean not in seen:
            seen.add(clean)
            text_lines.append(clean)

    return " ".join(text_lines)


# ---------------------------------------------------------------------------
# Core extraction functions
# ---------------------------------------------------------------------------
class TranscriptExtractor:
    def __init__(self, base_url, email, password, output_dir, headless=False):
        self.base_url = base_url.rstrip('/')
        self.email = email
        self.password = password
        self.output_dir = Path(output_dir)
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        """Launch browser and login."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)

        # Try saved session
        if os.path.exists(STATE_FILE):
            print("Reutilizando sessão salva...")
            self.context = self.browser.new_context(storage_state=STATE_FILE)
        else:
            self.context = self.browser.new_context()

        self.page = self.context.new_page()

        # Check if login needed
        self.page.goto(f"{self.base_url}/area", wait_until="domcontentloaded", timeout=45000)
        if "/login" in self.page.url.lower():
            self._login()
        else:
            print("Sessão válida, login não necessário.")

    def _login(self):
        """Authenticate on the platform."""
        login_url = f"{self.base_url}/login"
        print(f"Fazendo login em {login_url}...")
        self.page.goto(login_url, wait_until="domcontentloaded", timeout=45000)

        self.page.fill('#AcessoEmail, input[name="Acesso[email]"], input[type="email"], input[name="email"]', self.email)
        self.page.fill('#AcessoSenha, input[name="Acesso[senha]"], input[type="password"]', self.password)
        self.page.click('button[type="submit"]')
        self.page.wait_for_load_state("networkidle", timeout=15000)

        self.context.storage_state(path=STATE_FILE)
        print("  -> Login OK. Sessão salva.")

    def stop(self):
        """Close browser."""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def discover_lessons(self, page_url):
        """Navigate to a page and discover all lesson links."""
        print(f"\nDescobrir aulas em: {page_url}")
        self.page.goto(page_url, wait_until="domcontentloaded", timeout=45000)
        self.page.wait_for_timeout(3000)

        lessons = self.page.evaluate(JS_LIST_LESSONS)
        print(f"  -> {len(lessons)} aulas encontradas")
        for i, lesson in enumerate(lessons, 1):
            print(f"  {i:2d}. {lesson['name']} (ID: {lesson['id']})")
        return lessons

    def detect_video_type(self):
        """Detect if current page has a Vimeo or YouTube embed."""
        iframes = self.page.evaluate(JS_GET_ALL_IFRAMES)

        for iframe in iframes:
            src = iframe.get("src", "")
            if "vimeo" in src:
                return "vimeo", src
            if "youtube" in src or "youtube-nocookie" in src:
                match = re.search(r'embed/([^?/]+)', src)
                yt_id = match.group(1) if match else None
                return "youtube", yt_id

        return "unknown", None

    def extract_vimeo(self, vimeo_url):
        """Extract transcript from a Vimeo player URL."""
        vimeo_page = self.context.new_page()
        try:
            print(f"  Abrindo Vimeo: {vimeo_url}")
            vimeo_page.goto(vimeo_url, wait_until="domcontentloaded", timeout=45000)
            vimeo_page.wait_for_timeout(2000)

            result = vimeo_page.evaluate(JS_EXTRACT_VIMEO_TRANSCRIPT)

            if result in ("TRANSCRIPT_BUTTON_NOT_FOUND", "CONTAINER_NOT_FOUND"):
                print(f"  AVISO: {result}")
                return ""

            return result
        except Exception as e:
            print(f"  ERRO Vimeo: {e}")
            return ""
        finally:
            vimeo_page.close()

    def extract_youtube(self, youtube_id):
        """Extract transcript from YouTube using yt-dlp, then browser fallback."""
        print(f"  YouTube ID: {youtube_id}")

        # Try yt-dlp first
        transcript = self._yt_dlp_extract(youtube_id)
        if transcript:
            return transcript

        # Browser fallback
        return self._youtube_browser_extract(youtube_id)

    def _yt_dlp_extract(self, youtube_id):
        """Use yt-dlp to download auto-generated subtitles."""
        try:
            tmp_dir = Path("/tmp/yt-transcripts")
            tmp_dir.mkdir(exist_ok=True)

            cmd = [
                "yt-dlp",
                "--write-auto-sub",
                "--sub-lang", "pt",
                "--skip-download",
                "--sub-format", "vtt",
                "-o", str(tmp_dir / "%(id)s.%(ext)s"),
                f"https://www.youtube.com/watch?v={youtube_id}",
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            vtt_files = list(tmp_dir.glob(f"{youtube_id}*.vtt"))
            if vtt_files:
                return parse_vtt(vtt_files[0])

            print(f"  yt-dlp: legenda não encontrada")
            return ""
        except FileNotFoundError:
            print("  yt-dlp não instalado, usando fallback browser")
            return ""
        except Exception as e:
            print(f"  yt-dlp erro: {e}")
            return ""

    def _youtube_browser_extract(self, youtube_id):
        """Fallback: extract YouTube transcript via browser."""
        yt_page = self.context.new_page()
        try:
            print(f"  Abrindo YouTube no browser...")
            yt_page.goto(f"https://www.youtube.com/watch?v={youtube_id}", wait_until="domcontentloaded", timeout=45000)
            yt_page.wait_for_timeout(3000)

            # Try to open transcript panel
            yt_page.click('button[aria-label="More actions"], #button-shape button', timeout=5000)
            yt_page.wait_for_timeout(1000)

            # Click "Show transcript" / "Mostrar transcrição"
            transcript_btn = yt_page.locator('text=/transcript|transcrição/i').first
            transcript_btn.click(timeout=5000)
            yt_page.wait_for_timeout(2000)

            segments = yt_page.evaluate("""
                Array.from(document.querySelectorAll(
                  'ytd-transcript-segment-renderer .segment-text, ' +
                  'ytd-transcript-segment-renderer yt-formatted-string'
                )).map(el => el.textContent.trim()).join(' ')
            """)
            return segments or ""
        except Exception as e:
            print(f"  YouTube browser erro: {e}")
            return ""
        finally:
            yt_page.close()

    def extract_lesson(self, lesson_url, module_name, module_slug, lesson_num=None):
        """
        Extract transcript from a single lesson.

        Args:
            lesson_url: Full URL of the lesson page
            module_name: Human-readable module name
            module_slug: Folder name for output (e.g. modulo-05-automatizando)
            lesson_num: Optional lesson number prefix (e.g. "01")
        """
        print(f"\n{'='*60}")

        # Navigate to lesson page
        self.page.goto(lesson_url, wait_until="domcontentloaded", timeout=45000)
        self.page.wait_for_timeout(2000)

        title = self.page.evaluate(JS_GET_PAGE_TITLE)
        # Clean title (remove site name suffix if present)
        title = re.sub(r'\s*[-–|].*$', '', title).strip()
        print(f"Aula: {title}")
        print(f"Módulo: {module_name}")

        # Detect video type
        video_type, video_ref = self.detect_video_type()
        print(f"Tipo: {video_type}")

        if video_type == "vimeo":
            transcript = self.extract_vimeo(video_ref)
        elif video_type == "youtube":
            transcript = self.extract_youtube(video_ref)
        else:
            print("  ERRO: Nenhum player de vídeo encontrado")
            return None

        if not transcript:
            print("  ERRO: Transcrição vazia")
            return None

        # Build filename
        slug = slugify(title)
        prefix = f"{lesson_num}-" if lesson_num else ""
        filename = f"{prefix}{slug}.md"

        # Save
        out_dir = self.output_dir / module_slug
        out_dir.mkdir(parents=True, exist_ok=True)
        filepath = out_dir / filename

        content = format_transcript(title, module_name, lesson_url, transcript)
        filepath.write_text(content, encoding="utf-8")
        print(f"  -> Salvo: {filepath}")

        return filepath

    def extract_module(self, module_page_url, module_name, module_slug):
        """
        Discover all lessons in a module page and extract each one.

        Args:
            module_page_url: URL of any page that lists the module's lessons
            module_name: Human-readable module name
            module_slug: Folder name for output
        """
        lessons = self.discover_lessons(module_page_url)

        results = {"success": [], "failed": []}
        for i, lesson in enumerate(lessons, 1):
            num = f"{i:02d}"
            slug = slugify(lesson["name"])
            filepath = self.output_dir / module_slug / f"{num}-{slug}.md"

            if filepath.exists():
                print(f"\n  [SKIP] Já existe: {filepath}")
                results["success"].append(lesson["name"])
                continue

            try:
                result = self.extract_lesson(
                    lesson_url=lesson["href"],
                    module_name=module_name,
                    module_slug=module_slug,
                    lesson_num=num,
                )
                if result:
                    results["success"].append(lesson["name"])
                else:
                    results["failed"].append(lesson["name"])
            except Exception as e:
                print(f"  ERRO: {e}")
                results["failed"].append(lesson["name"])

        # Summary
        print(f"\n{'='*60}")
        print(f"MÓDULO: {module_name}")
        print(f"Sucesso: {len(results['success'])} | Falha: {len(results['failed'])}")
        if results["failed"]:
            print("Falhas:")
            for f in results["failed"]:
                print(f"  - {f}")

        return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extrator de Transcrições — Genérico",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  # Descobrir aulas em uma página
  python3 extract_transcript.py discover --url https://membros.site.com/area/modulo/1

  # Extrair uma aula específica
  python3 extract_transcript.py lesson --url https://membros.site.com/area/produto/item/123 \\
    --module-name "Módulo 1" --module-slug modulo-01 --num 01

  # Extrair um módulo inteiro (descobre aulas automaticamente)
  python3 extract_transcript.py module --url https://membros.site.com/area/modulo/1 \\
    --module-name "Módulo 1" --module-slug modulo-01
        """
    )
    parser.add_argument("action", choices=["discover", "lesson", "module"],
                        help="Ação: discover (listar aulas), lesson (extrair uma), module (extrair todas)")
    parser.add_argument("--url", required=True, help="URL da página")
    parser.add_argument("--base-url", default="https://membros.jonathantaioba.com",
                        help="URL base do site")
    parser.add_argument("--email", default=os.environ.get("COURSE_EMAIL"),
                        help="Email de login (ou COURSE_EMAIL env var)")
    parser.add_argument("--password", default=os.environ.get("COURSE_PASSWORD"),
                        help="Senha de login (ou COURSE_PASSWORD env var)")
    parser.add_argument("--output-dir", default=None,
                        help="Diretório de saída (default: transcricoes/ no projeto)")
    parser.add_argument("--module-name", help="Nome do módulo (para metadata)")
    parser.add_argument("--module-slug", help="Slug do módulo (nome da pasta)")
    parser.add_argument("--num", help="Número da aula (prefixo do arquivo, ex: 01)")
    parser.add_argument("--headless", action="store_true", help="Rodar sem janela")

    args = parser.parse_args()

    if not args.email or not args.password:
        print("ERRO: Email e senha obrigatórios (--email/--password ou COURSE_EMAIL/COURSE_PASSWORD)")
        sys.exit(1)

    # Default output dir: transcricoes/ in project root
    if args.output_dir:
        output_dir = args.output_dir
    else:
        script_dir = Path(__file__).resolve().parent
        output_dir = script_dir.parent.parent.parent.parent / "transcricoes"

    extractor = TranscriptExtractor(
        base_url=args.base_url,
        email=args.email,
        password=args.password,
        output_dir=output_dir,
        headless=args.headless,
    )

    try:
        extractor.start()

        if args.action == "discover":
            extractor.discover_lessons(args.url)

        elif args.action == "lesson":
            if not args.module_name or not args.module_slug:
                print("ERRO: --module-name e --module-slug obrigatórios para 'lesson'")
                sys.exit(1)
            extractor.extract_lesson(args.url, args.module_name, args.module_slug, args.num)

        elif args.action == "module":
            if not args.module_name or not args.module_slug:
                print("ERRO: --module-name e --module-slug obrigatórios para 'module'")
                sys.exit(1)
            extractor.extract_module(args.url, args.module_name, args.module_slug)

    finally:
        extractor.stop()
