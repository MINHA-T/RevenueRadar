
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="RevenueRadar", page_icon="📊", layout="wide")

st.title("📊 RevenueRadar")
st.caption("E-commerce Customer & Revenue Intelligence")

sales = pd.read_csv("sales_data.csv.gz", parse_dates=["InvoiceDate"])
rfm = pd.read_csv("rfm_segments.csv")
predictions = pd.read_csv("prediction_results.csv")

sales["Month"] = sales["InvoiceDate"].dt.to_period("M").astype(str)

revenue = sales["Revenue"].sum()
orders = sales["InvoiceNo"].nunique()
customers = sales["CustomerID"].nunique()
products = sales["StockCode"].nunique()

a, b, c, d = st.columns(4)
a.metric("Total Revenue", f"£{revenue:,.0f}")
b.metric("Invoices", f"{orders:,}")
c.metric("Customers", f"{customers:,}")
d.metric("Products", f"{products:,}")

st.divider()
left, right = st.columns(2)

with left:
    st.subheader("Monthly Revenue")
    monthly = sales.groupby("Month", as_index=False)["Revenue"].sum()
    fig = px.line(monthly, x="Month", y="Revenue", markers=True)
    st.plotly_chart(fig, width="stretch")

with right:
    st.subheader("Revenue by Country")
    countries = sales.groupby("Country", as_index=False)["Revenue"].sum()
    countries = countries.nlargest(10, "Revenue").sort_values("Revenue")
    fig = px.bar(countries, x="Revenue", y="Country", orientation="h")
    st.plotly_chart(fig, width='stretch')

st.divider()
left, right = st.columns(2)

with left:
    st.subheader("Customer Segments")
    if "Segment" in rfm.columns:
        segments = rfm["Segment"].value_counts().reset_index()
        segments.columns = ["Segment", "Customers"]
        fig = px.pie(segments, names="Segment", values="Customers", hole=0.4)
        st.plotly_chart(fig, width='stretch')
    else:
        st.warning("The RFM file has no Segment column.")

with right:
    st.subheader("Inactivity Model Results")
    actual = predictions["Actual_Inactive"]
    predicted = predictions["Predicted_Inactive"]
    accuracy = (actual == predicted).mean() * 100
    st.metric("Test Accuracy", f"{accuracy:.2f}%")
    st.metric("Test Customers", f"{len(predictions):,}")
    st.caption("Historical test-set predictions, not current customer status.")

    st.subheader("Customer Segment Summary")
    if "Segment" in rfm.columns:
        segment_summary = rfm["Segment"].value_counts().reset_index()
        segment_summary.columns = ["Segment", "Customers"]
        segment_summary["Percentage"] = (
        segment_summary["Customers"] / segment_summary["Customers"].sum() * 100
        ).round(2)
        st.dataframe(segment_summary, hide_index=True, width="stretch")

st.divider()
st.subheader("Explore Sales Data")
country_options = ["All"] + sorted(sales["Country"].dropna().unique().tolist())
selected_country = st.selectbox("Filter by country", country_options)

filtered = sales if selected_country == "All" else sales[sales["Country"] == selected_country]
st.dataframe(filtered.head(100), width="stretch")
st.caption(f"Showing up to 100 rows out of {len(filtered):,} filtered transactions.")



# STEP 64: Verify dashboard metrics

st.subheader("Data Validation")

st.write("Total rows:", len(sales))
st.write("Unique invoices:", sales["InvoiceNo"].nunique())
st.write("Unique customers:", sales["CustomerID"].nunique())
st.write("Unique products:", sales["StockCode"].nunique())
st.write("Total revenue:", round(sales["Revenue"].sum(), 2))


# STEP 67: Check data quality

st.subheader("Data Quality Status")

missing_dates = sales["InvoiceDate"].isna().sum()
missing_revenue = sales["Revenue"].isna().sum()

if missing_dates == 0 and missing_revenue == 0:
    st.success("Data quality check passed!")
else:
    st.warning(
        f"Missing dates: {missing_dates} | "
        f"Missing revenue values: {missing_revenue}"
    )


# STEP 68: Verify revenue consistency

st.subheader("Revenue Consistency Check")

calculated_revenue = round(sales["Revenue"].sum(), 2)

st.metric("Verified Total Revenue", f"£{calculated_revenue:,.2f}")


# STEP 69: Display transaction date range

st.subheader("Transaction Date Range")

st.write("First transaction:", sales["InvoiceDate"].min().date())
st.write("Last transaction:", sales["InvoiceDate"].max().date())



# STEP 70: Validate customer count

st.subheader("Customer Count Validation")

customer_count = sales["CustomerID"].nunique()

st.metric("Verified Unique Customers", f"{customer_count:,}")


# STEP 71: Validate invoice count

st.subheader("Invoice Count Validation")

invoice_count = sales["InvoiceNo"].nunique()

st.metric("Verified Unique Invoices", f"{invoice_count:,}")


# STEP 68: Download sales data

st.subheader("Download Sales Data")

st.download_button(
    label="Download Filtered CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="revenue_radar_sales.csv",
    mime="text/csv"
)
