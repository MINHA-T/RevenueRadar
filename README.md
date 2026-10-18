# 📊 RevenueRadar

**E-commerce Customer & Revenue Intelligence**

🌐 **Live dashboard:** [revenueradar-minha.streamlit.app](https://revenueradar-minha.streamlit.app)  
💻 **Source code:** [GitHub repository](https://github.com/MINHA-T/RevenueRadar)

RevenueRadar turns historical e-commerce transactions into business insights through data cleaning, exploratory data analysis (EDA), RFM customer segmentation, a historical customer-inactivity classification experiment, and an interactive Streamlit dashboard.

## Features

- Data cleaning and validation of duplicates, missing values, cancellations, returns, zero-priced transactions, and unusual records.
- EDA of monthly and daily revenue, country performance, top products, customer spending, and purchase frequency.
- RFM (Recency, Frequency, Monetary) customer segmentation.
- Random Forest classification experiment for historical customer inactivity.
- Interactive Streamlit dashboard with KPIs, Plotly charts, customer segments, historical model results, country filtering, and a filtered CSV download.
- Data quality, revenue consistency, and transaction date checks.

## Tech stack

Python, Pandas, NumPy, scikit-learn, Plotly, Streamlit, Google Colab, and Visual Studio Code.

## Current dashboard metrics

| Metric | Value |
|---|---:|
| Product-sales revenue | £10,642,110.80 |
| Unique invoices | 19,962 |
| Unique customers | 4,338 |
| Unique products (StockCode) | 3,922 |
| Countries | 38 |
| Cleaned sales rows | 524,878 |
| Transaction dates | 1 Dec 2010 – 9 Dec 2011 |

**Revenue note:** The displayed value is the sum of revenue in the cleaned positive-sales dataset. It is not profit or an audited accounting figure.

## Run locally

All files below should be in the same folder:

```text
RevenueRadar/
├── app.py
├── sales_data.csv.gz
├── rfm_segments.csv
├── prediction_results.csv
├── requirements.txt
├── .gitignore
└── README.md
```

1. Install Python.
2. Open a terminal in this folder and install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the dashboard:

   ```bash
   python -m streamlit run app.py
   ```

4. Open the local URL printed in the terminal, usually `http://localhost:8501`.

Pandas reads `sales_data.csv.gz` directly; do not unzip that file into a CSV for this version of the app.

## Dashboard sections

- Revenue, invoice, customer, and product KPIs
- Monthly revenue and revenue-by-country charts
- Customer segment distribution and summary
- Historical inactivity model results
- Country filter and transaction table
- Data validation and filtered CSV download

## Model evaluation and limitations

The current dashboard reports **66.16% test accuracy** across **721 historical test customers**. This is a held-out result on historical data, not a guarantee of performance on current customers or future transactions.

The inactivity target was defined using a historical prediction window of October–November 2011 and features from an earlier observation period. RFM segments are rule-based categories, not independently verified labels. Feature importance describes how a fitted model used its inputs; it does not establish causation. The dataset ends on 9 December 2011, so December is incomplete and results may not represent present-day e-commerce behaviour.

## Selected business insights

- The United Kingdom is the dominant market, with about £9.0 million in product-sales revenue.
- November is the highest-revenue month in the analysed period; December is incomplete.
- Top-selling products by quantity and top products by revenue are not necessarily the same.
- Customer segments can help organise retention efforts, while model predictions should be treated as exploratory decision support.

## Future improvements

- Add automated tests for data processing and dashboard calculations.
- Compare classification models and report precision, recall, F1-score, and a confusion matrix.
- Strengthen time-based validation and assess class imbalance.
- Add segment-specific recommendations and further interactive filters.

## Dataset

The project uses the Online Retail transactional dataset from the UCI Machine Learning Repository.
