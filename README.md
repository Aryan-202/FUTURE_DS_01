# FUTURE_DS_01 - Business Sales Performance Analytics

**Future Interns** - Data Science & Analytics Internship Task 1

## Project Overview

This repository contains the completion of **Task 1: Business Sales Performance Analytics** for the Data Science & Analytics track at Future Interns.

The primary objective of this project is to analyze business sales data to identify:

- Revenue trends over time
- Top-selling products
- High-value categories
- Regional performance

By performing exploratory data analysis (EDA) and data cleaning, we aim to uncover key business insights and deliver actionable recommendations to help focus on profitable areas and drive business growth.

## Tools & Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas (for data cleaning and manipulation)
- **Environment:** Jupyter Notebook (`analysis.ipynb`), Python Scripts (`main.py`)

## 📂 Project Structure

```
FUTURE_DS_01/
│
├── data/
│   ├── raw/                 # Raw dataset (Superstore.csv)
│   └── processed/           # Cleaned and processed dataset ready for analysis
│
├── main.py                  # Python script for automated data cleaning
├── analysis.ipynb           # Jupyter Notebook containing Exploratory Data Analysis (EDA)
└── README.md                # Project documentation
```

## Dataset Information

**Dataset Used**: [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
The dataset comprises sales, profit, region, and category data for an e-commerce retail store. It serves as an excellent foundation to extract meaningful business KPIs.

## Workflow & Steps Performed

1. **Data Cleaning (`main.py`)**:
   - Handled encoding issues (Windows-1252 to UTF-8 standard).
   - Removed duplicate entries and empty rows/columns.
   - Standardized column names and stripped hidden white spaces in string data.
   - Formatted Date columns (`Order Date`, `Ship Date`) properly.
2. **Data Analysis (`analysis.ipynb`)**:
   - Loaded the cleaned dataset from `data/processed/`.
   - Conducted statistical analysis to derive revenue trends and high-performing segments.
   - Generated visual representations and extracted key business insights.

## Key Learnings & Insights

_(Note: To be updated based on the final analysis notebook output)_

- **Data Cleaning & Preparation:** Implementing automated pipelines using Pandas to format raw datasets.
- **KPI Analysis:** Understanding and formulating business-focused metrics.
- **Trend & Performance Analysis:** Extracting actionable business recommendations.

---

_This repository is built as part of the Future Interns program._
