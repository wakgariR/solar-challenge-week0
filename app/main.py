import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, plot_boxplot, summarize_metrics
import warnings
warnings.simplefilter(action="ignore", category=UserWarning)
warnings.simplefilter(action="ignore", category=FutureWarning)

# ---- App Title ----
st.title("Solar Irradiance Dashboard")

# ---- Load data ----
df_benin, df_sierraleone, df_togo = load_data()

# ---- Sidebar: Select countries ----
country_options = ["Benin", "Sierra Leone", "Togo"]
selected_countries = st.sidebar.multiselect(
    "Select Countries", country_options, default=country_options
)

# Combine selected countries
df_all = pd.concat([
    df_benin[df_benin["Country"].isin(selected_countries)],
    df_sierraleone[df_sierraleone["Country"].isin(selected_countries)],
    df_togo[df_togo["Country"].isin(selected_countries)]
], ignore_index=True)

# ---- Boxplot of GHI ----
st.subheader("Boxplot of GHI by Country")
fig = plot_boxplot(df_all, metric="GHI")
st.pyplot(fig)

# ---- Summary Table ----
st.subheader("Summary Table of Metrics")
summary_df = summarize_metrics(df_all)
st.dataframe(summary_df)
