import os 
import streamlit as st
import pandas as pd

st.set_page_config(page_title="📊 Sales Analysis", layout="wide")
st.title("📊 Sales Dashboard")

# Load data
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sales_data.csv')
DATA_PATH = os.path.abspath(DATA_PATH)  # Ensure absolute path

try:
    df = pd.read_csv(DATA_PATH)
    st.subheader("Raw Data")
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"❌ File not found: {DATA_PATH}")
    st.stop()

# Aggregation
if "region" in df.columns and "units_sold" in df.columns:
    sales_by_region = df.groupby("region")["units_sold"].sum().reset_index()
    st.subheader("Units Sold by Region")
    st.bar_chart(sales_by_region.set_index("region"))
else:
    st.error("❌ Columns 'region' and/or 'units_sold' not found in the data.")