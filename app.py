import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache_data
def load_data(path: str):
    return pd.read_csv(path)


st.set_page_config(page_title="Airbnb EDA", layout="wide")
st.title("Airbnb Exploratory Data Analysis")

DATA_PATH = "Airbnb_Open_Data.csv"

try:
    df = load_data(DATA_PATH)
except Exception as e:
    st.error(f"Could not load data from {DATA_PATH}: {e}")
    st.stop()

st.markdown("---")
st.header("Data Preview")
st.dataframe(df.head())

st.header("Basic Summary")
st.write(df.describe(include='all'))

num_cols = df.select_dtypes(include=['number']).columns.tolist()

if num_cols:
    st.sidebar.header("Plots")
    col = st.sidebar.selectbox("Numeric column for histogram", num_cols)
    st.subheader(f"Histogram — {col}")
    st.altair_chart(alt.Chart(df.dropna(subset=[col])).mark_bar().encode(
        x=alt.X(col, bin=alt.Bin(maxbins=50)),
        y='count()'
    ).properties(width=800, height=300), use_container_width=True)

    st.subheader("Correlation Matrix")
    corr = df[num_cols].corr()
    if not corr.empty:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='vlag', ax=ax)
        st.pyplot(fig)

if 'latitude' in df.columns and 'longitude' in df.columns:
    st.header("Map")
    coords = df[['latitude', 'longitude']].dropna()
    if not coords.empty:
        st.map(coords)

st.header("Rows / Columns")
st.write(f"Rows: {df.shape[0]} — Columns: {df.shape[1]}")
