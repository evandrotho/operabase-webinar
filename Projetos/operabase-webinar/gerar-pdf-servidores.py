#!/usr/bin/env python3
"""Gera PDF: Servidores Recomendados para Automações e IA"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate, Frame
import os

OUTPUT_PATH = os.path.expanduser("~/Downloads/Servidores-Recomendados-Operabase.pdf")

# ── Cores ──────────────────────────────────────────────
DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#0f3460")
LIGHT_BG = HexColor("#f8f9fa")
GREEN = HexColor("#22c55e")
BLUE = HexColor("#3b82f6")
PURPLE = HexColor("#8b5cf6")
ORANGE = HexColor("#f97316")
RED = HexColor("#ef4444")
GRAY = HexColor("#6b7280")
LIGHT_GRAY = HexColor("#e5e7eb")
WHITE = white

BADGE_COLORS = {
    "Iniciante": GREEN,
    "Intermediário": BLUE,
    "Avançado": PURPLE,
    "IA em Produção": ORANGE,
    "IA Máxima": RED,
}

# ── Estilos ────────────────────────────────────────────
style_title = ParagraphStyle(
    "Title", fontName="Helvetica-Bold", fontSize=28, leading=34,
    textColor=DARK, alignment=TA_CENTER, spaceAfter=8*mm
)
style_subtitle = ParagraphStyle(
    "Subtitle", fontName="Helvetica", fontSize=14, leading=18,
    textColor=GRAY, alignment=TA_CENTER, spaceAfter=12*mm
)
style_section = ParagraphStyle(
    "Section", fontName="Helvetica-Bold", fontSize=18, leading=22,
    textColor=DARK, spaceBefore=8*mm, spaceAfter=4*mm
)
style_body = ParagraphStyle(
    "Body", fontName="Helvetica", fontSize=11, leading=15,
    textColor=HexColor("#374151"), spaceAfter=3*mm
)
style_body_center = ParagraphStyle(
    "BodyCenter", fontName="Helvetica", fontSize=11, leading=15,
    textColor=HexColor("#374151"), alignment=TA_CENTER
)
style_card_name = ParagraphStyle(
    "CardName", fontName="Helvetica-Bold", fontSize=16, leading=20,
    textColor=DARK
)
style_card_spec = ParagraphStyle(
    "CardSpec", fontName="Helvetica", fontSize=10, leading=14,
    textColor=HexColor("#4b5563")
)
style_card_price = ParagraphStyle(
    "CardPrice", fontName="Helvetica-Bold", fontSize=20, leading=24,
    textColor=ACCENT
)
style_card_bullet = ParagraphStyle(
    "CardBullet", fontName="Helvetica", fontSize=10, leading=14,
    textColor=HexColor("#374151"), leftIndent=8
)
style_card_link = ParagraphStyle(
    "CardLink", fontName="Helvetica", fontSize=9, leading=13,
    textColor=BLUE
)
style_footer = ParagraphStyle(
    "Footer", fontName="Helvetica", fontSize=8, leading=11,
    textColor=GRAY, alignment=TA_CENTER
)
style_badge = ParagraphStyle(
    "Badge", fontName="Helvetica-Bold", fontSize=9, leading=12,
    textColor=WHITE, alignment=TA_CENTER
)


def build_cover(elements):
    """Página de capa."""
    elements.append(Spacer(1, 50*mm))

    # Linha decorativa
    elements.append(HRFlowable(width="40%", thickness=2, color=ACCENT, spaceAfter=10*mm))

    elements.append(Paragraph("Servidores Recomendados<br/>para Automações e IA", style_title))
    elements.append(Paragraph("Guia de escolha por orçamento e necessidade", style_subtitle))

    # Linha decorativa
    elements.append(HRFlowable(width="40%", thickness=2, color=ACCENT, spaceBefore=5*mm, spaceAfter=15*mm))

    elements.append(Paragraph("OperaBase", ParagraphStyle(
        "Brand", fontName="Helvetica-Bold", fontSize=22, leading=26,
        textColor=ACCENT, alignment=TA_CENTER
    )))

    elements.append(Spacer(1, 40*mm))

    elements.append(Paragraph(
        "Março 2026",
        ParagraphStyle("Date", fontName="Helvetica", fontSize=10,
                       textColor=GRAY, alignment=TA_CENTER)
    ))

    elements.append(PageBreak())


def build_section1(elements):
    """Seção 1 — Como escolher o servidor certo."""
    elements.append(Paragraph("Como escolher o servidor certo", style_section))
    elements.append(HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY, spaceAfter=5*mm))

    elements.append(Paragraph(
        "A escolha do servidor depende do momento do seu negócio. "
        "Comece com uma <b>VPS</b> para validar e rodar automações leves. "
        "Quando o volume crescer, migre para um <b>Dedicado AMD</b> com mais poder de processamento. "
        "Para rodar modelos de IA em produção (LLMs locais, fine-tuning, inferência), "
        "você precisa de um <b>Dedicado com GPU</b>.",
        style_body
    ))

    # Fluxo visual
    flow_data = [[
        Paragraph("<b>VPS</b><br/><font size=8 color='#6b7280'>Para começar</font>", style_body_center),
        Paragraph("→", ParagraphStyle("Arrow", fontName="Helvetica-Bold", fontSize=18, textColor=ACCENT, alignment=TA_CENTER)),
        Paragraph("<b>Dedicado AMD</b><br/><font size=8 color='#6b7280'>Para escalar</font>", style_body_center),
        Paragraph("→", ParagraphStyle("Arrow", fontName="Helvetica-Bold", fontSize=18, textColor=ACCENT, alignment=TA_CENTER)),
        Paragraph("<b>Dedicado GPU</b><br/><font size=8 color='#6b7280'>IA em produção</font>", style_body_center),
    ]]

    flow_table = Table(flow_data, colWidths=[90, 25, 110, 25, 110])
    flow_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, 0), HexColor("#f0fdf4")),
        ('BACKGROUND', (2, 0), (2, 0), HexColor("#eff6ff")),
        ('BACKGROUND', (4, 0), (4, 0), HexColor("#fef3c7")),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('BOX', (0, 0), (0, 0), 0.5, LIGHT_GRAY),
        ('BOX', (2, 0), (2, 0), 0.5, LIGHT_GRAY),
        ('BOX', (4, 0), (4, 0), 0.5, LIGHT_GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(Spacer(1, 5*mm))
    elements.append(flow_table)
    elements.append(Spacer(1, 10*mm))


def make_card(name, badge_label, specs, price, ideal_for, link, link_label, badge_color):
    """Cria um card de servidor como tabela formatada."""
    elements = []

    # Badge
    badge_style = ParagraphStyle(
        "BadgeInline", fontName="Helvetica-Bold", fontSize=9,
        textColor=WHITE, backColor=badge_color, alignment=TA_LEFT,
        leftIndent=0, spaceBefore=0, spaceAfter=2*mm,
        borderPadding=(3, 8, 3, 8)
    )

    # Header com nome e badge
    badge_text = f'<font color="white"><b>  {badge_label}  </b></font>'

    header_data = [[
        Paragraph(name, style_card_name),
    ]]
    header_table = Table(header_data, colWidths=[450])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    elements.append(header_table)

    # Badge como tabela colorida
    badge_data = [[Paragraph(f'<font color="white"><b>{badge_label}</b></font>',
                             ParagraphStyle("B", fontName="Helvetica-Bold", fontSize=9,
                                            textColor=WHITE, alignment=TA_CENTER))]]
    badge_w = max(len(badge_label) * 6.5 + 20, 80)
    badge_table = Table(badge_data, colWidths=[badge_w], rowHeights=[18])
    badge_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), badge_color),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
        ('TOPPADDING', (0, 0), (0, 0), 2),
        ('BOTTOMPADDING', (0, 0), (0, 0), 2),
    ]))
    elements.append(badge_table)
    elements.append(Spacer(1, 3*mm))

    # Specs
    elements.append(Paragraph(specs, style_card_spec))
    elements.append(Spacer(1, 2*mm))

    # Preço
    elements.append(Paragraph(price, style_card_price))
    elements.append(Spacer(1, 3*mm))

    # Ideal para
    elements.append(Paragraph("<b>Ideal para:</b>", ParagraphStyle(
        "IdealTitle", fontName="Helvetica-Bold", fontSize=10, leading=13,
        textColor=HexColor("#374151")
    )))
    for item in ideal_for:
        elements.append(Paragraph(f"✓  {item}", style_card_bullet))

    elements.append(Spacer(1, 3*mm))

    # Link
    elements.append(Paragraph(
        f'<a href="{link}" color="#3b82f6">🔗 {link_label}</a>',
        style_card_link
    ))

    return elements


def build_cards(elements):
    """Seção 2 — Os 5 cards de servidores."""
    elements.append(Paragraph("As 5 opções recomendadas", style_section))
    elements.append(HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY, spaceAfter=5*mm))

    servers = [
        {
            "name": "Hostinger KVM8",
            "badge": "Iniciante",
            "specs": "CPU: 8 vCPUs  •  RAM: 32 GB  •  Disco: 400 GB NVMe",
            "price": "R$ 250/mês",
            "ideal": [
                "Primeiras automações (n8n, Flowise, Make)",
                "Sites, APIs leves, bancos de dados pequenos",
                "Quem está começando e quer gastar pouco",
            ],
            "link": "https://www.hostinger.com/vps-hosting",
            "link_label": "Hostinger VPS Hosting",
        },
        {
            "name": "Hetzner AX41-NVMe",
            "badge": "Intermediário",
            "specs": "CPU: AMD Ryzen 5 3600 (6c/12t)  •  RAM: 64 GB DDR4  •  Disco: 2× 512 GB NVMe",
            "price": "€ 37/mês (~R$ 240)",
            "ideal": [
                "Múltiplas automações simultâneas",
                "Bancos de dados maiores, processos em paralelo",
                "Escalar operação sem GPU",
            ],
            "link": "https://www.hetzner.com/dedicated-rootserver/ax41-nvme/",
            "link_label": "Hetzner AX41-NVMe",
        },
        {
            "name": "Hetzner AX102-U",
            "badge": "Avançado",
            "specs": "CPU: AMD EPYC (alta performance)  •  RAM: 128 GB DDR5 ECC  •  Disco: 2× 1.92 TB NVMe",
            "price": "€ 104/mês (~R$ 680)",
            "ideal": [
                "Operações pesadas com muitos agentes rodando",
                "RAG local, embeddings, banco vetorial",
                "Infra robusta para equipe ou clientes",
            ],
            "link": "https://www.hetzner.com/dedicated-rootserver/ax102-u/",
            "link_label": "Hetzner AX102-U",
        },
        {
            "name": "Hetzner GEX44",
            "badge": "IA em Produção",
            "specs": "CPU: Intel Core i5-13500  •  RAM: 64 GB DDR5  •  GPU: NVIDIA L40S (48 GB VRAM)  •  Disco: 2× 512 GB NVMe",
            "price": "€ 184/mês (~R$ 1.200)",
            "ideal": [
                "Rodar LLMs locais (Llama, Mistral, Qwen)",
                "Fine-tuning de modelos com seus dados",
                "Inferência em produção com baixa latência",
            ],
            "link": "https://www.hetzner.com/dedicated-rootserver/gex44/",
            "link_label": "Hetzner GEX44",
        },
        {
            "name": "Hetzner GEX131",
            "badge": "IA Máxima",
            "specs": "CPU: AMD EPYC 9254 (24c/48t)  •  RAM: 384 GB DDR5 ECC  •  GPU: NVIDIA RTX PRO 6000 (96 GB VRAM)  •  Disco: 2× 1.92 TB NVMe",
            "price": "€ 889/mês (~R$ 5.800)",
            "ideal": [
                "Treinamento de modelos grandes",
                "Múltiplos LLMs em produção simultânea",
                "Processamento massivo de dados (vídeo, imagem, texto)",
            ],
            "link": "https://www.hetzner.com/dedicated-rootserver/gex131/",
            "link_label": "Hetzner GEX131",
        },
    ]

    for i, srv in enumerate(servers):
        # Card container como tabela com borda
        card_elements = make_card(
            srv["name"], srv["badge"], srv["specs"], srv["price"],
            srv["ideal"], srv["link"], srv["link_label"],
            BADGE_COLORS[srv["badge"]]
        )

        # Montar conteúdo do card em uma única célula
        inner_content = []
        for el in card_elements:
            inner_content.append(el)

        card_data = [[inner_content]]
        card_table = Table(card_data, colWidths=[460])

        # Cor de fundo alternada
        bg = WHITE if i % 2 == 0 else HexColor("#fafafa")
        border_color = BADGE_COLORS[srv["badge"]]

        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), bg),
            ('BOX', (0, 0), (0, 0), 1, LIGHT_GRAY),
            ('LINEBEFOREDECAL', (0, 0), (0, 0), 0),
            ('LINEBEFORE', (0, 0), (0, 0), 4, border_color),
            ('TOPPADDING', (0, 0), (0, 0), 12),
            ('BOTTOMPADDING', (0, 0), (0, 0), 12),
            ('LEFTPADDING', (0, 0), (0, 0), 16),
            ('RIGHTPADDING', (0, 0), (0, 0), 16),
            ('VALIGN', (0, 0), (0, 0), 'TOP'),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ]))

        elements.append(card_table)
        elements.append(Spacer(1, 5*mm))


def build_footer_section(elements):
    """Rodapé com notas."""
    elements.append(Spacer(1, 8*mm))
    elements.append(HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY, spaceAfter=4*mm))

    elements.append(Paragraph(
        "💱 <b>Nota sobre cotação:</b> Os valores em R$ são estimativas com base na cotação "
        "de ~R$ 6,50/€ (março 2026). Consulte a cotação do dia antes de contratar.",
        ParagraphStyle("Note", fontName="Helvetica", fontSize=9, leading=13,
                       textColor=GRAY, spaceBefore=2*mm, spaceAfter=2*mm)
    ))

    elements.append(Paragraph(
        "⚠️ <b>Aviso:</b> Preços, configurações e disponibilidade podem variar. "
        "Consulte os sites oficiais para informações atualizadas.",
        ParagraphStyle("Note2", fontName="Helvetica", fontSize=9, leading=13,
                       textColor=GRAY, spaceAfter=2*mm)
    ))

    elements.append(Spacer(1, 8*mm))

    elements.append(Paragraph(
        "Guia produzido por OperaBase  •  Março 2026",
        style_footer
    ))


def add_page_number(canvas_obj, doc):
    """Adiciona número de página no rodapé."""
    canvas_obj.saveState()
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.setFillColor(GRAY)
    page_num = canvas_obj.getPageNumber()
    if page_num > 1:  # Não mostra na capa
        canvas_obj.drawCentredString(A4[0] / 2, 15*mm, f"— {page_num} —")
    canvas_obj.restoreState()


def main():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=25*mm,
        rightMargin=25*mm,
        topMargin=20*mm,
        bottomMargin=25*mm,
        title="Servidores Recomendados para Automações e IA",
        author="OperaBase",
        subject="Guia de Servidores",
    )

    elements = []

    # Capa
    build_cover(elements)

    # Seção 1
    build_section1(elements)

    # Seção 2 — Cards
    build_cards(elements)

    # Rodapé
    build_footer_section(elements)

    # Build
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF gerado: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
