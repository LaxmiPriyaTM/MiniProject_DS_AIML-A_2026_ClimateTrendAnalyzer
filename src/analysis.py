"""
analysis.py
-----------
ClimateTrend Analyzer - EDA & Visualization Module
Author: [Your Name]
Date: 2024

This module handles:
- Exploratory Data Analysis (EDA)
- Correlation analysis
- All visualizations (temperature trend, CO2 vs temp, anomaly detection, etc.)
- Saves all graphs to outputs/graphs/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import os

# ─────────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────────
DATA_PATH = "dataset/processed_data/climate_cleaned.csv"
GRAPH_DIR = "outputs/graphs/"

# Use a clean, readable style
sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams["figure.dpi"] = 120
plt.rcParams["font.size"] = 11


def load_data(path: str) -> pd.DataFrame:
    """Load processed dataset."""
    df = pd.read_csv(path)
    print(f"[INFO] Loaded processed data: {df.shape}")
    return df


def save_fig(filename: str) -> None:
    """Save current figure to outputs/graphs/."""
    os.makedirs(GRAPH_DIR, exist_ok=True)
    filepath = os.path.join(GRAPH_DIR, filename)
    plt.savefig(filepath, bbox_inches="tight")
    print(f"[SAVED] {filepath}")
    plt.close()


# ─────────────────────────────────────────────
# EDA FUNCTIONS
# ─────────────────────────────────────────────

def run_eda(df: pd.DataFrame) -> None:
    """Print EDA summary: shape, dtypes, stats, correlations."""
    print("\n===== EXPLORATORY DATA ANALYSIS =====")
    print(f"Shape      : {df.shape}")
    print(f"Columns    : {list(df.columns)}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nDescriptive Stats:\n{df.describe()}")

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 1:
        print(f"\nCorrelation Matrix:\n{df[numeric_cols].corr()}")


# ─────────────────────────────────────────────
# VISUALIZATION FUNCTIONS
# ─────────────────────────────────────────────

def plot_temperature_trend(df: pd.DataFrame) -> None:
    """
    Line chart: Annual temperature anomaly over years.
    Includes 5-year rolling mean for trend clarity.
    """
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(df["Year"], df["Temperature_Anomaly"],
            color="#78c1f3", alpha=0.5, linewidth=1, label="Annual Anomaly")

    if "Temp_RollingMean" in df.columns:
        ax.plot(df["Year"], df["Temp_RollingMean"],
                color="#e05c5c", linewidth=2.5, label="5-Year Rolling Mean")

    ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    ax.set_title("Global Temperature Anomaly Over Time", fontsize=14, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature Anomaly (°C)")
    ax.legend()
    save_fig("01_temperature_trend.png")


def plot_co2_trend(df: pd.DataFrame) -> None:
    """Bar / line chart: CO2 concentration over years."""
    if "CO2_ppm" not in df.columns:
        print("[SKIP] CO2_ppm column not found.")
        return

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.fill_between(df["Year"], df["CO2_ppm"], alpha=0.4, color="#f4a261")
    ax.plot(df["Year"], df["CO2_ppm"], color="#e76f51", linewidth=2)
    ax.set_title("Atmospheric CO₂ Concentration Over Time", fontsize=14, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("CO₂ (ppm)")
    save_fig("02_co2_trend.png")


def plot_co2_vs_temperature(df: pd.DataFrame) -> None:
    """
    Scatter plot: CO2 vs Temperature Anomaly.
    Shows correlation between greenhouse gases and warming.
    """
    if "CO2_ppm" not in df.columns:
        print("[SKIP] CO2_ppm column not found.")
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    sc = ax.scatter(df["CO2_ppm"], df["Temperature_Anomaly"],
                    c=df["Year"], cmap="YlOrRd", s=40, alpha=0.8, edgecolors="none")
    plt.colorbar(sc, ax=ax, label="Year")
    ax.set_title("CO₂ vs Temperature Anomaly", fontsize=14, fontweight="bold")
    ax.set_xlabel("CO₂ Concentration (ppm)")
    ax.set_ylabel("Temperature Anomaly (°C)")
    save_fig("03_co2_vs_temperature.png")


def plot_anomaly_detection(df: pd.DataFrame) -> None:
    """
    Highlight years where temperature anomaly exceeds +0.5°C (extreme warming events).
    """
    if "Anomaly_Flag" not in df.columns:
        print("[SKIP] Anomaly_Flag column not found.")
        return

    anomalies = df[df["Anomaly_Flag"] == 1]
    normal = df[df["Anomaly_Flag"] == 0]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.scatter(normal["Year"], normal["Temperature_Anomaly"],
               color="#74c69d", s=25, label="Normal", alpha=0.7)
    ax.scatter(anomalies["Year"], anomalies["Temperature_Anomaly"],
               color="#d62828", s=50, label="Anomaly (>0.5°C)", zorder=5)
    ax.axhline(0.5, color="orange", linestyle="--", linewidth=1.2, label="Threshold (0.5°C)")
    ax.set_title("Temperature Anomaly Detection", fontsize=14, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature Anomaly (°C)")
    ax.legend()
    save_fig("04_anomaly_detection.png")


def plot_decade_avg(df: pd.DataFrame) -> None:
    """Bar chart: Average temperature anomaly per decade."""
    if "Decade" not in df.columns:
        print("[SKIP] Decade column not found.")
        return

    decade_avg = df.groupby("Decade")["Temperature_Anomaly"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ["#d62828" if v > 0 else "#4361ee" for v in decade_avg["Temperature_Anomaly"]]
    ax.bar(decade_avg["Decade"].astype(str), decade_avg["Temperature_Anomaly"],
           color=colors, edgecolor="white")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Average Temperature Anomaly by Decade", fontsize=14, fontweight="bold")
    ax.set_xlabel("Decade")
    ax.set_ylabel("Avg Temperature Anomaly (°C)")
    plt.xticks(rotation=45)
    save_fig("05_decade_avg.png")


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Seaborn heatmap of correlations between numeric features."""
    numeric_df = df.select_dtypes(include=[np.number]).drop(
        columns=["Anomaly_Flag", "Decade"], errors="ignore"
    )
    if numeric_df.shape[1] < 2:
        print("[SKIP] Not enough numeric columns for heatmap.")
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f",
                cmap="coolwarm", linewidths=0.5, ax=ax)
    ax.set_title("Feature Correlation Heatmap", fontsize=14, fontweight="bold")
    save_fig("06_correlation_heatmap.png")


def plot_rainfall_trend(df: pd.DataFrame) -> None:
    """Line chart: Annual rainfall over time (if available)."""
    if "Rainfall_mm" not in df.columns:
        print("[SKIP] Rainfall_mm column not found.")
        return

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df["Year"], df["Rainfall_mm"], color="#219ebc", linewidth=1.5)
    ax.set_title("Annual Rainfall Over Time", fontsize=14, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Rainfall (mm)")
    save_fig("07_rainfall_trend.png")


# ─────────────────────────────────────────────
# MAIN RUNNER
# ─────────────────────────────────────────────

def run_analysis():
    """Run full EDA and generate all graphs."""
    df = load_data(DATA_PATH)
    run_eda(df)

    print("\n[INFO] Generating visualizations...")
    plot_temperature_trend(df)
    plot_co2_trend(df)
    plot_co2_vs_temperature(df)
    plot_anomaly_detection(df)
    plot_decade_avg(df)
    plot_correlation_heatmap(df)
    plot_rainfall_trend(df)

    print("\n[SUCCESS] All graphs saved to outputs/graphs/")


if __name__ == "__main__":
    run_analysis()
