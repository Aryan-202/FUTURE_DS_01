# FUTURE_DS_01 - Business Sales Performance Analytics

**Future Interns** - Data Science & Analytics Internship Task 1

## Project Overview

This repository contains the completion of **Task 1: Business Sales Performance Analytics** for the Data Science & Analytics track at Future Interns.

The primary objective of this project is to analyze business sales data to identify:

- Revenue trends over time (2014-2017)
- Top-selling products and categories
- High-value customer segments
- Regional performance across the United States

By performing exploratory data analysis (EDA) and data cleaning, we uncover key business insights and deliver actionable recommendations to focus on profitable areas and drive business growth.

## Tools & Technologies Used

- **Programming Language:** Python
- **Data Manipulation:** Pandas
- **Data Visualization:** Matplotlib, Seaborn
- **Interactive Dashboard:** Power BI
- **Environment:** Jupyter Notebook (`notebooks/analysis.ipynb`)

## 📂 Project Structure

```
FUTURE_DS_01/
│
├── dashboard/
│   └── FUTURE_DS_01.pbix    # Power BI Dashboard for interactive visualization
│
├── data/
│   ├── superstore.csv       # Raw dataset (Superstore)
│   └── cleaned_superstore.csv # Processed dataset ready for analysis
│
├── notebooks/
│   └── analysis.ipynb       # Jupyter Notebook containing Data Cleaning and EDA
│
└── README.md                # Project documentation
```

## Dataset Information

**Dataset Used**: [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
The dataset comprises sales, profit, region, and category data for an e-commerce retail store. It serves as an excellent foundation to extract meaningful business KPIs.

## Workflow & Steps Performed

1. **Data Cleaning & Preparation**:
   - Handled encoding issues (Latin-1 to standard UTF-8).
   - Removed duplicate entries to ensure data integrity.
   - Formatted Date columns (`Order Date`, `Ship Date`) into datetime objects.
   - Performed feature engineering to extract **Year**, **Month**, and **Month Name** for time-series analysis.
2. **Exploratory Data Analysis (EDA)**:
   - Conducted statistical analysis to derive revenue trends.
   - Analyzed performance by **Product Sub-Category**, **Region**, and **Segment**.
   - Generated visual representations (Line plots, Bar charts) to identify growth patterns.
3. **Visualization & Dashboarding**:
   - Created an interactive dashboard in Power BI to present KPIs and geographical performance.

## Key Learnings & Insights

Based on the analysis performed in the notebook:

- **Sales Growth:** There is a consistent upward trend in revenue from 2014 to 2017, with 2017 showing the highest total sales ($733k+).
- **Product Performance:** **Phones** and **Chairs** are the top revenue generators, contributing significantly to the overall sales.
- **Regional Strength:** The **West Region** is the strongest market, followed by the East, while the South shows significant room for growth.
- **Customer Segments:** The **Consumer Segment** represents the largest portion of sales and profit.
- **Profitability vs Sales:** While sales are high in some categories (like Tables), high discounts occasionally lead to negative profits, suggesting a need for optimized pricing strategies.

---

*This repository is built as part of the Future Interns program.*
