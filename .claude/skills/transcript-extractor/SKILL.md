---
name: transcript-extractor
description: |
  Extrai transcrições de aulas de cursos online hospedados em plataformas com vídeos Vimeo ou YouTube.
  This skill should be used when the user asks to transcribe lessons, extract transcripts, or work with course video content.
  Supports Vimeo (transcript panel extraction) and YouTube (yt-dlp + browser fallback).
  Generic — works with any course platform that uses iframe video embeds.
user-invocable: true
argument-hint: "<action> --url <URL> [--module-name <name>] [--module-slug <slug>]"
---

# Transcript Extractor

## Purpose

Extract transcriptions from online course lessons. Navigates the course platform via browser automation (Playwright), discovers video embeds (Vimeo or YouTube), extracts transcripts, and saves as formatted markdown files.

## Prerequisites

- Python 3.9+ with `playwright` package
- Chromium: `playwright install chromium`
- `yt-dlp` (for YouTube lessons): `brew install yt-dlp`
- Course credentials in environment: `COURSE_EMAIL` and `COURSE_PASSWORD`

## Workflow

### 1. Discover lessons in a module/page

```bash
source .env && python3 .claude/skills/transcript-extractor/scripts/extract_transcript.py \
  discover --url "https://membros.site.com/area/modulo/1" \
  --email "$COURSE_EMAIL" --password "$COURSE_PASSWORD"
```

Returns a numbered list of all lessons found on that page.

### 2. Extract a single lesson

```bash
source .env && python3 .claude/skills/transcript-extractor/scripts/extract_transcript.py \
  lesson --url "https://membros.site.com/area/produto/item/12345" \
  --module-name "Nome do Módulo" --module-slug "modulo-01-slug" --num "01" \
  --email "$COURSE_EMAIL" --password "$COURSE_PASSWORD"
```

### 3. Extract all lessons from a module

```bash
source .env && python3 .claude/skills/transcript-extractor/scripts/extract_transcript.py \
  module --url "https://membros.site.com/area/modulo/1" \
  --module-name "Nome do Módulo" --module-slug "modulo-01-slug" \
  --email "$COURSE_EMAIL" --password "$COURSE_PASSWORD"
```

Discovers all lessons on the page, then extracts each one sequentially. Skips lessons that already have a .md file.

## Extraction Logic

### Vimeo (most lessons)
1. Navigate to lesson page on course platform
2. Find Vimeo iframe src
3. Open Vimeo player directly
4. Click `#transcript-control-bar-button` to open transcript panel
5. Scroll through `TranscriptCue` elements (Vimeo uses virtualized lazy list)
6. Collect and deduplicate all text cues

### YouTube (some lessons)
1. Navigate to lesson page, find YouTube iframe
2. Extract video ID from embed URL
3. Try `yt-dlp --write-auto-sub --sub-lang pt` first
4. If yt-dlp fails (private video), open YouTube in browser and extract from transcript panel

## Output Format

```markdown
# [Lesson Title]
**Módulo:** [Module Name]
**URL:** [lesson URL]

## Transcrição

[full transcript text, no timestamps]
```

Files saved to `transcricoes/{module-slug}/{num}-{lesson-slug}.md`

## Options

| Flag | Description |
|------|-------------|
| `--base-url` | Platform base URL (default: membros.jonathantaioba.com) |
| `--output-dir` | Custom output directory (default: transcricoes/) |
| `--headless` | Run browser without visible window |
| `--num` | Lesson number prefix for filename (e.g. "01") |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Login fails | Check credentials, check if site has CAPTCHA |
| `TRANSCRIPT_BUTTON_NOT_FOUND` | Video has no transcript on Vimeo |
| `CONTAINER_NOT_FOUND` | Transcript panel didn't load |
| Session expired | Delete `scripts/.auth_state.json` to force re-login |
| yt-dlp fails | Private video — browser fallback is automatic |
