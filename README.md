# 📊 RevenueRadar

**E-commerce Customer & Revenue Intelligence**

RevenueRadar is a Python data analytics project that transforms historical e-commerce transactions into business insights through data cleaning, exploratory data analysis (EDA), RFM customer segmentation, a historical customer-inactivity classification experiment, and an interactive Streamlit dashboard.

## Features

- **Data cleaning and validation:** investigates duplicates, missing values, cancellations, returns, zero-priced transactions, and unusual records.
- **Exploratory data analysis:** examines monthly and daily revenue, country performance, top products by quantity and revenue, customer spending, and order frequency.
- **RFM segmentation:** groups customers using Recency, Frequency, and Monetary value.
- **Historical inactivity model:** trains a Random Forest classifier on past customer behaviour to predict inactivity in a later historical window.
- **Interactive dashboard:** presents KPIs, revenue charts, segment distributions, model results, country filtering, and a transaction table.
- **Export and data checks:** includes validation sections and a download button for filtered sales data.

## Technology Stack

- Python
- Pandas and NumPy
- scikit-learn
- Plotly
- Streamlit
- Google Colab
- Visual Studio Code

## Dashboard Metrics

The current local dashboard displays these results:

| Metric | Value |
|---|---:|
| Total product-sales revenue | £10,642,110.80 |
| Unique invoices | 19,962 |
| Unique customers | 4,338 |
| Unique products (StockCode) | 3,922 |
| Countries represented | 38 |
| Transaction date range | 1 Dec 2010 – 9 Dec 2011 |

The sales dataset used by the dashboard contains **524,878 rows** after cleaning.

> **Revenue note:** this value is the sum of revenue in the cleaned positive-sales dataset. It is not profit or an audited accounting figure.

## Run Locally

### 1. Create the project folder

Keep the following files together in the `RevenueRadar` folder:

```text
RevenueRadar/
├── app.py
├── sales_data.csv
├── rfm_segments.csv
├── prediction_results.csv
├── RevenueRadar.ipynb
└── README.md
```

The notebook is optional for launching the dashboard but documents the analysis workflow.

### 2. Install dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install streamlit pandas plotly
```

### 3. Launch Streamlit

```bash
python -m streamlit run app.py
```

Open the local URL printed in the terminal, usually **http://localhost:8501**.

## Dashboard Sections

- Revenue, invoice, customer, and product KPIs
- Monthly revenue trend
- Revenue by country
- Customer segment chart and summary
- Historical inactivity model evaluation
- Country selector and sales-data table
- Data quality and revenue consistency checks
- Filtered CSV download

## Model Results and Limitations

The current dashboard reports **66.16% test accuracy** across **721 historical test customers**. This is a historical held-out test result, not a guarantee of performance on current customers or future transactions.

The inactivity target was constructed using a historical prediction window of October–November 2011, based on customer behaviour from the preceding observation period. RFM segments are rule-based categories, not independently verified customer labels. Feature importance describes how the trained model used its input features; it does not establish causation.

The dataset ends on **9 December 2011**, so December is incomplete. Results are historical and may not reflect present-day customer behaviour.

## Selected Business Insights

- The United Kingdom is the dominant market in the dataset, contributing approximately £9.0 million in product-sales revenue.
- November is the highest-revenue month in the analysed period; December is incomplete and should be interpreted cautiously.
- The product with the highest quantity sold is not necessarily the product with the highest revenue.
- Customer segmentation can help organise retention efforts, while inactivity predictions should be treated as exploratory decision support.

## Possible Future Improvements

- Add automated tests for data cleaning and dashboard metrics.
- Compare classification models and report precision, recall, F1-score, and the confusion matrix.
- Strengthen time-based model evaluation and address class imbalance.
- Deploy the dashboard and document the live URL here.
- Add segment-specific recommendations and further interactive filters.

## Dataset

The project uses the **Online Retail** transactional dataset from the UCI Machine Learning Repository.

---

*RevenueRadar — Python-powered customer and revenue intelligence.*
