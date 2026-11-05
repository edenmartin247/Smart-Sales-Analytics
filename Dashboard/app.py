import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# Page Configuration
st.set_page_config(
    page_title="Smart Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "Data" / "Processed" / "SuperStoreOrders_cleaned.csv"

df = pd.read_csv(data_path)

# Dashboard Title
st.title("📊 Smart Sales Analytics Dashboard")

st.write(
    "An interactive dashboard for analyzing sales, "
    "profit, products, regions and business performance."
)




# ==============================
# STEP 13: INTERACTIVE FILTERS
# ==============================

st.sidebar.header("Dashboard Filters")

# Region Filter
selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["region"].dropna().unique()),
    default=sorted(df["region"].dropna().unique())
)

# Category Filter
selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].dropna().unique()),
    default=sorted(df["category"].dropna().unique())
)

# Market Filter
selected_markets = st.sidebar.multiselect(
    "Select Market",
    options=sorted(df["market"].dropna().unique()),
    default=sorted(df["market"].dropna().unique())
)

# Year Filter
selected_years = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["order_year"].dropna().unique()),
    default=sorted(df["order_year"].dropna().unique())
)

# Apply Filters
filtered_df = df[
    (df["region"].isin(selected_regions)) &
    (df["category"].isin(selected_categories)) &
    (df["market"].isin(selected_markets)) &
    (df["order_year"].isin(selected_years))
]

st.sidebar.success(
    f"{len(filtered_df):,} records selected"
)


# ==============================
# STEP 12: KPI CARDS
# ==============================

st.subheader("Business Performance Overview")

# Calculate KPIs

total_sales = filtered_df["sales"].sum()

total_profit = filtered_df["profit"].sum()

total_orders = filtered_df["order_id"].nunique()

average_order_value = (
    filtered_df.groupby("order_id")["sales"].sum().mean()
)

profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

# Display KPI Cards

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Sales",
    f"{total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"{total_profit:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col4.metric(
    "Average Order Value",
    f"{average_order_value:,.2f}"
)

col5.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

# Dataset Information
st.subheader("Dataset Overview")

col1, col2 = st.columns(2)

col1.metric("Total Records", f"{len(filtered_df):,}")
col2.metric("Total Columns", len(df.columns))

st.success("Dataset loaded successfully!")

st.dataframe(filtered_df.head(10), use_container_width=True)

# ==============================
# STEP 14: INTERACTIVE CHARTS
# ==============================

st.header("Sales Analysis")

# Sales by Category

st.subheader("Sales by Category")

category_sales = filtered_df.groupby("category")["sales"].sum().reset_index()

fig_category = px.bar(
    category_sales,
    x="category",
    y="sales",
    title="Total Sales by Category",
    text_auto=True,
    color="category"
)

st.plotly_chart(fig_category, use_container_width=True)

# ==============================
# CHART 2: PROFIT BY REGION
# ==============================

st.subheader("Profit by Region")

region_profit = (
    filtered_df.groupby("region")["profit"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_profit,
    x="region",
    y="profit",
    title="Total Profit by Region",
    text_auto=True,
    color="region"
)

st.plotly_chart(fig_region, use_container_width=True)

# ==============================
# CHART 3: MONTHLY SALES TREND
# ==============================

st.subheader("Monthly Sales Trend")

monthly_sales = filtered_df.copy()

monthly_sales["order_date"] = pd.to_datetime(
    monthly_sales["order_date"],
    errors="coerce"
)

monthly_sales = (
    monthly_sales.groupby(
        monthly_sales["order_date"].dt.to_period("M")
    )["sales"]
    .sum()
    .reset_index()
)

monthly_sales["month"] = monthly_sales["order_date"].astype(str)

fig_monthly = px.line(
    monthly_sales,
    x="month",
    y="sales",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(fig_monthly, use_container_width=True)

# ==============================
# CHART 4: SALES BY MARKET
# ==============================

st.subheader("Sales by Market")

market_sales = (
    filtered_df.groupby("market")["sales"]
    .sum()
    .reset_index()
)

fig_market = px.pie(
    market_sales,
    names="market",
    values="sales",
    title="Sales Distribution by Market",
    hole=0.4
)

fig_market.update_traces(
    textinfo="percent+label"
)

st.plotly_chart(fig_market, use_container_width=True)