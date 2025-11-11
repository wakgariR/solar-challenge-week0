import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


# Function to load data
def load_data():
    # Get the folder where this script is located
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Build path to data folder
    data_dir = os.path.join(BASE_DIR, "..", "data")

    # Load CSV files
    df_benin = pd.read_csv(os.path.join(data_dir, "benin-malanville_clean.csv"))
    df_sierraleone = pd.read_csv(os.path.join(data_dir, "sierraleone-bumbuna_clean.csv"))
    df_togo = pd.read_csv(os.path.join(data_dir, "togo-dapaong_qc_clean.csv"))
    df_benin["Country"] = "Benin"
    df_sierraleone["Country"] = "Sierra Leone"
    df_togo["Country"] = "Togo"

    return df_benin, df_sierraleone, df_togo

# Function to plot boxplot
def plot_boxplot(df, metric="GHI"):
    plt.figure(figsize=(8,5))
    sns.boxplot(x="Country", y=metric, data=df, palette="Set2")
    plt.title(f"Distribution of {metric} by Country")
    plt.ylabel(metric)
    plt.xlabel("Country")
    plt.tight_layout()
    fig = plt.gcf()
    return fig

# Function to summarize metrics
def summarize_metrics(df):
    metrics = ["GHI", "DNI", "DHI"]
    summary = df.groupby("Country")[metrics].agg(["mean", "median", "std"]).round(2)
    return summary
