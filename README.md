# E-Commerce Customer Churn Risk Scorer

> **Which customers are about to leave — and what should we do about it?**
> This project builds a data-driven churn risk scoring system for an Indian e-commerce platform using RFM analysis and machine learning, translating model output into a actionable 3-tier intervention playbook.

---

## Business Problem

Customer acquisition costs 5-7x more than retention. Yet most e-commerce platforms have no early warning system for customers at risk of churning. This project answers three questions:

1. Which customers are showing early signs of disengagement?
2. What behavioural patterns predict churn before it happens?
3. What specific interventions should be triggered for each risk tier?

---

## Approach

### Step 1 — RFM Segmentation
RFM (Recency, Frequency, Monetary) is the industry-standard framework used by e-commerce and banking analysts to segment customers by behaviour:
- **Recency** — How recently did they order?
- **Frequency** — How often do they order?
- **Monetary** — How much do they spend?

### Step 2 — Churn Label Engineering
Customers with high recency (haven't ordered recently), low frequency, and low monetary value are labelled as churn risk using a rule-based threshold system.

### Step 3 — ML Risk Classifier
A Random Forest classifier is trained on RFM features to score each customer as:
- 🔴 **High Risk** — Immediate intervention needed
- 🟡 **Medium Risk** — Nurture campaign recommended
- 🟢 **Low Risk** — Loyalty reward to retain

### Step 4 — Power BI Dashboard
Risk scores visualised by segment, category, state, and order behaviour.

### Step 5 — Intervention Playbook
1-page PDF detailing exactly what action to take for each risk tier.

---

## Tools & Stack

| Layer | Tool |
|---|---|
| Data Wrangling | Python (Pandas, NumPy) |
| Feature Engineering | RFM Analysis |
| Machine Learning | Scikit-learn (Random Forest) |
| Visualisation | Power BI, Matplotlib, Seaborn |
| Reporting | Intervention Playbook (PDF) |
| Version Control | Git + GitHub |

---

## Repository Structure

```
ecommerce-churn-risk-scorer/
│
├── data/
│   ├── raw/                        # Original dataset
│   └── cleaned/
│       └── rfm_scored_customers.csv  # RFM scores + churn labels
│
├── notebooks/
│   └── churn_risk_analysis.ipynb   # Full analysis + ML model
│
├── models/
│   └── churn_model_summary.txt     # Model performance metrics
│
├── dashboard/
│   └── screenshots/                # Power BI dashboard exports
│
├── reports/
│   └── intervention_playbook.pdf   # 3-tier action plan
│
└── README.md
```

---

## Key Results

| Metric | Value |
|---|---|
| Total Customers Analysed | TBD after running notebook |
| High Risk Customers | TBD |
| Medium Risk Customers | TBD |
| Low Risk Customers | TBD |
| Model Accuracy | TBD |

*Update after completing the analysis.*

---

## Intervention Playbook Summary

| Risk Tier | Signal | Recommended Action |
|---|---|---|
| 🔴 High Risk | No order in 60+ days, low frequency | Win-back email + 15% discount voucher |
| 🟡 Medium Risk | No order in 30-60 days, avg frequency | Personalised product recommendation push |
| 🟢 Low Risk | Recent order, high frequency | Loyalty points + early access offer |

---

## Dashboard Preview

| Churn Risk Overview | Segment Analysis | Intervention Map |
|---|---|---|
| ![Page 1](dashboard/screenshots/page1_risk_overview.png) | ![Page 2](dashboard/screenshots/page2_segments.png) | ![Page 3](dashboard/screenshots/page3_interventions.png) |

*Add screenshots after completing Power BI dashboard.*

---

## How to Run

```bash
git clone https://github.com/juvana81/ecommerce-churn-risk-scorer.git
cd ecommerce-churn-risk-scorer
pip install pandas numpy matplotlib seaborn scikit-learn jupyter reportlab
jupyter notebook notebooks/churn_risk_analysis.ipynb
```

---

## Dataset

**Source:** Amazon Sale Report (same dataset as India E-Commerce Pulse project)
**Size:** 128,975 rows
**Link:** [Kaggle](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data)

---

## About

**Juvana Dsouza** | B.E. AI & Data Science, Fr. CRCE Mumbai
[LinkedIn](https://linkedin.com/in/juvana) · [GitHub](https://github.com/juvana81) · juvanadsouza81@gmail.com
