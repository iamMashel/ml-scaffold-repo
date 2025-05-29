# import streamlit as st
# import pandas as pd

# import os

# st.set_page_config(page_title="📊 Sales Analysis", layout="wide")

# st.title("📊 Sales Dashboard")

# # Load data
# DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sales_data.csv')
# df = pd.read_csv(DATA_PATH)

# st.subheader("Raw Data")
# st.dataframe(df)

# # Aggregation
# sales_by_region = df.groupby("region")["units_sold"].sum().reset_index()

# st.subheader("Units Sold by Region")
# st.bar_chart(sales_by_region.set_index("region"))
