from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Dynamic Data from pathlib import Path

DATA_PATH = Path.cwd().parent / "data" / "processed" / "your_data_clean.csv"  # Update to your filename

# Log paths for debugging
# st.write(f"Looking for file at: {DATA_PATH.resolve()}")

if not DATA_PATH.exists():
    st.error(f"CSV not found at: {DATA_PATH.resolve()}")
    st.stop()

df = pd.read_csv(DATA_PATH)


# --- Sidebar Filters ---
st.sidebar.header("Filter Netflix Data")
years = sorted(df['date_added'].dropna().unique())
selected_years = st.sidebar.multiselect("Select Year Added", years, default=years)
types = df['type'].dropna().unique()
selected_types = st.sidebar.multiselect("Select Type", types, default=list(types))

# --- Filter Data ---
df_filtered = df[df['date_added'].isin(selected_years) & df['type'].isin(selected_types)]

# --- Main Page ---
st.title("🎬 Netflix Content Dashboard")
st.markdown("Explore how Netflix's catalog evolved by type, genre, rating, and region.")

if df_filtered.empty:
    st.warning("No data matches your filter selection.")
    st.stop()

# Content over time
st.subheader("📈 Content Added Over Time")
content_by_year = df_filtered['date_added'].value_counts().sort_index()
st.line_chart(content_by_year)

# Genre breakdown
st.subheader("🎭 Top Genres")
if 'listed_in' in df_filtered.columns:
    genres = df_filtered['listed_in'].dropna().str.split(',').explode().str.strip()
    top_genres = genres.value_counts().nlargest(10)
    st.bar_chart(top_genres)
else:
    st.info("No genre information available.")

# Country share
st.subheader("🌍 Top Countries")
if 'country' in df_filtered.columns:
    countries = df_filtered['country'].dropna().str.split(',').explode().str.strip()
    top_countries = countries.value_counts().nlargest(10)
    fig = px.pie(values=top_countries.values, names=top_countries.index, title='Top Producing Countries')
    st.plotly_chart(fig)
else:
    st.info("No country information available.")

# Ratings breakdown
st.subheader("🔞 Ratings Distribution")
if 'rating' in df_filtered.columns:
    st.bar_chart(df_filtered['rating'].dropna().value_counts())
else:
    st.info("No rating information available.")

# --- Footer ---
st.markdown("---")
st.markdown("Data Source: [Kaggle Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)")