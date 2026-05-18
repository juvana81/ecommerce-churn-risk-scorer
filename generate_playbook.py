from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

OUTPUT = "reports/intervention_playbook.pdf"

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    topMargin=12*mm, bottomMargin=12*mm,
    leftMargin=16*mm, rightMargin=16*mm
)

# ── Colours ────────────────────────────────────────────────
NAVY   = colors.HexColor("#1e3a5f")
BLUE   = colors.HexColor("#2563eb")
RED    = colors.HexColor("#dc2626")
GREEN  = colors.HexColor("#16a34a")
ORANGE = colors.HexColor("#ea580c")
LGRAY  = colors.HexColor("#f1f5f9")
MGRAY  = colors.HexColor("#94a3b8")
WHITE  = colors.white

base = getSampleStyleSheet()

def style(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

S = {
    "header_title": style("ht", fontSize=20, textColor=WHITE, fontName="Helvetica-Bold", leading=24),
    "header_sub"  : style("hs", fontSize=9,  textColor=colors.HexColor("#bfdbfe"), leading=12),
    "header_name" : style("hn", fontSize=9,  textColor=MGRAY, leading=11),
    "section"     : style("sec", fontSize=8, textColor=BLUE, fontName="Helvetica-Bold", leading=10, spaceBefore=6),
    "body"        : style("body", fontSize=8.5, textColor=colors.HexColor("#1e293b"), leading=13, spaceAfter=3),
    "kpi_val"     : style("kv", fontSize=22, fontName="Helvetica-Bold", textColor=NAVY, leading=26, alignment=TA_CENTER),
    "kpi_lbl"     : style("kl", fontSize=7.5, textColor=MGRAY, leading=10, alignment=TA_CENTER),
    "tier_title"  : style("tt", fontSize=11, fontName="Helvetica-Bold", textColor=WHITE, leading=14),
    "tier_sub"    : style("ts", fontSize=8,  textColor=colors.HexColor("#e2e8f0"), leading=11),
    "step_title"  : style("st", fontSize=8.5, fontName="Helvetica-Bold", textColor=NAVY, leading=11),
    "step_body"   : style("sb", fontSize=8,  textColor=colors.HexColor("#334155"), leading=12),
    "tag"         : style("tag", fontSize=7, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=9),
    "footer"      : style("ft", fontSize=7.5, textColor=MGRAY, alignment=TA_CENTER, leading=10),
    "metric_val"  : style("mv", fontSize=14, fontName="Helvetica-Bold", textColor=WHITE, leading=18, alignment=TA_CENTER),
    "metric_lbl"  : style("ml", fontSize=7,  textColor=colors.HexColor("#e2e8f0"), leading=9, alignment=TA_CENTER),
}

story = []

# ── HEADER ─────────────────────────────────────────────────
header_data = [[
    Paragraph("CUSTOMER CHURN INTERVENTION PLAYBOOK", S["header_name"]),
    Paragraph("Juvana Dsouza  |  juvanadsouza81@gmail.com", S["header_name"]),
],[
    Paragraph("3-Tier Churn Risk\nIntervention Playbook", S["header_title"]),
    Paragraph("", S["header_title"]),
],[
    Paragraph("RFM Analysis + Random Forest Classifier  •  6,908 Customers Scored  •  99.9% Model Accuracy", S["header_sub"]),
    Paragraph("", S["header_sub"]),
]]
header_table = Table(header_data, colWidths=[120*mm, 58*mm])
header_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), NAVY),
    ("SPAN",          (0,1), (-1,1)),
    ("SPAN",          (0,2), (-1,2)),
    ("ALIGN",         (1,0), (1,0), "RIGHT"),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ("RIGHTPADDING",  (0,0), (-1,-1), 8),
]))
story.append(header_table)
story.append(Spacer(1, 5*mm))

# ── KPI ROW ────────────────────────────────────────────────
story.append(Paragraph("MODEL OUTPUT SUMMARY", S["section"]))
story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=3))

kpis = [
    ("6,908", "Customers Scored"),
    ("3,550", "High Risk (51.4%)"),
    ("3,356", "Medium Risk (48.6%)"),
    ("2", "Low Risk (0.03%)"),
    ("99.9%", "Model Accuracy"),
]
kpi_cells = [
    [Paragraph(v, S["kpi_val"]) for v,_ in kpis],
    [Paragraph(l, S["kpi_lbl"]) for _,l in kpis],
]
kpi_table = Table(kpi_cells, colWidths=[35.6*mm]*5)
kpi_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), LGRAY),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LINEAFTER",     (0,0), (3,-1), 0.5, colors.HexColor("#cbd5e1")),
]))
story.append(kpi_table)
story.append(Spacer(1, 5*mm))

# ── METHODOLOGY ────────────────────────────────────────────
story.append(Paragraph("SCORING METHODOLOGY", S["section"]))
story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=3))
story.append(Paragraph(
    "Customers were scored using the industry-standard RFM (Recency, Frequency, Monetary) framework, "
    "then classified into three churn risk tiers using a Random Forest machine learning model trained on "
    "128,975 Amazon India transactions. Each customer segment receives a composite RFM score (3-9 scale) "
    "and is assigned to a risk tier with a specific, time-bound intervention action.",
    S["body"]
))
story.append(Spacer(1, 4*mm))

# ── 3 TIER CARDS ───────────────────────────────────────────
story.append(Paragraph("3-TIER INTERVENTION FRAMEWORK", S["section"]))
story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=3))

tiers = [
    (RED,    "🔴 HIGH RISK",    "3,550 customers  |  51.4%  |  RFM Score ≤ 4",
     "Win-back email + 15% discount voucher within 48hrs",
     [
         ("Signal",      "No order in 40+ days, low frequency, below-avg spend"),
         ("Urgency",     "IMMEDIATE — contact within 48 hours of identification"),
         ("Channel",     "Personalised email + SMS + push notification"),
         ("Offer",       "15% discount voucher on their most purchased category"),
         ("Goal",        "Re-engage before 60-day churn threshold is crossed"),
         ("Success KPI", "Re-purchase within 30 days of intervention"),
         ("Owner",       "CRM Team + Performance Marketing"),
     ]),
    (ORANGE, "🟡 MEDIUM RISK", "3,356 customers  |  48.6%  |  RFM Score 5-6",
     "Personalised product recommendation push notification",
     [
         ("Signal",      "No order in 20-40 days, moderate frequency"),
         ("Urgency",     "Within 7 days of risk identification"),
         ("Channel",     "Push notification + in-app banner + email"),
         ("Offer",       "Curated product recommendations based on past purchases"),
         ("Goal",        "Maintain engagement before they drop to High Risk tier"),
         ("Success KPI", "Click-through on recommendation within 14 days"),
         ("Owner",       "Product Team + Email Marketing"),
     ]),
    (GREEN,  "🟢 LOW RISK",    "2 customers  |  0.03%  |  RFM Score ≥ 7",
     "Loyalty points reward + early access to new arrivals",
     [
         ("Signal",      "Recent order, high frequency, above-avg spend"),
         ("Urgency",     "Monthly loyalty touchpoint — no urgency"),
         ("Channel",     "Email newsletter + loyalty programme dashboard"),
         ("Offer",       "Double loyalty points on next purchase + early access"),
         ("Goal",        "Deepen engagement and increase order frequency"),
         ("Success KPI", "Increase in monthly order frequency by 10%"),
         ("Owner",       "Loyalty Programme Team"),
     ]),
]

for color, title, subtitle, action, steps in tiers:
    # Tier header
    tier_header = Table([
        [Paragraph(title, S["tier_title"])],
        [Paragraph(subtitle, S["tier_sub"])],
        [Paragraph(f"→ ACTION: {action}", ParagraphStyle("ta", fontSize=8.5,
                   fontName="Helvetica-Bold", textColor=WHITE, leading=11))],
    ], colWidths=[178*mm])
    tier_header.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), color),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ]))
    story.append(tier_header)

    # Steps table
    step_data = [[
        Paragraph(k, S["step_title"]),
        Paragraph(v, S["step_body"])
    ] for k,v in steps]

    step_table = Table(step_data, colWidths=[28*mm, 150*mm])
    step_table.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), LGRAY),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ("LINEBELOW",     (0,0), (-1,-2), 0.3, colors.HexColor("#e2e8f0")),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]))
    story.append(step_table)
    story.append(Spacer(1, 4*mm))

# ── IMPLEMENTATION TIMELINE ────────────────────────────────
story.append(Paragraph("IMPLEMENTATION TIMELINE", S["section"]))
story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=3))

timeline_data = [
    ["WEEK 1", "WEEK 2-3", "WEEK 4", "MONTH 2-3"],
    [
        "- Export High Risk list\n- Set up win-back email\n- Brief CRM team",
        "- Launch Medium Risk push\n- Monitor High Risk re-purchase\n- A/B test discount %",
        "- Review campaign results\n- Adjust messaging\n- Update risk scores",
        "- Scale successful campaigns\n- Re-score all customers\n- Report to leadership"
    ]
]
timeline_table = Table(timeline_data, colWidths=[44*mm, 44*mm, 44*mm, 46*mm])
timeline_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), NAVY),
    ("BACKGROUND",    (0,1), (-1,1), LGRAY),
    ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 7.5),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
    ("VALIGN",        (0,0), (-1,-1), "TOP"),
]))
story.append(timeline_table)
story.append(Spacer(1, 5*mm))

# ── FOOTER ─────────────────────────────────────────────────
footer_data = [[
    Paragraph("Juvana Dsouza  |  B.E. AI & Data Science, Fr. CRCE Mumbai", S["footer"]),
    Paragraph("github.com/juvana81/ecommerce-churn-risk-scorer", S["footer"]),
    Paragraph("Tools: Python • Scikit-learn • RFM • Power BI", S["footer"]),
]]
footer_table = Table(footer_data, colWidths=[60*mm, 72*mm, 46*mm])
footer_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), NAVY),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 6),
]))
story.append(footer_table)

doc.build(story)
print(f"Playbook saved to {OUTPUT}")
