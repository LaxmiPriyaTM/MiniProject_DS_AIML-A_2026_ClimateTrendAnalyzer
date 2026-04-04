import pandas as pd

RAW_PATH = "dataset/raw_data/climate_data.csv"
PROCESSED_PATH = "dataset/processed_data/climate_cleaned.csv"


# ==============================
# LOAD DATA
# ==============================

def load_data(filepath):
    print(f"[INFO] Loading data from: {filepath}")
    df = pd.read_csv(filepath)
    return df


# ==============================
# CLEAN DATA
# ==============================

def clean_data(df):

    # Convert to numeric (IMPORTANT FIX)
    df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
    df["CO2_ppm"] = pd.to_numeric(df["CO2_ppm"], errors='coerce')
    df["Temperature_Anomaly"] = pd.to_numeric(df["Temperature_Anomaly"], errors='coerce')
    df["Rainfall_mm"] = pd.to_numeric(df["Rainfall_mm"], errors='coerce')

    # Drop missing values
    df = df.dropna(subset=["Year"])

    df = df.fillna(method="ffill")
    df = df.fillna(method="bfill")

    # Sort by Year
    df = df.sort_values(by="Year")

    return df


# ==============================
# FEATURE ENGINEERING
# ==============================

def feature_engineering(df):

    # Decade column
    df["Decade"] = (df["Year"] // 10) * 10

    # Rolling mean (Temperature trend smoothing)
    df["Temp_RollingMean"] = df["Temperature_Anomaly"].rolling(window=5, min_periods=1).mean()

    # Anomaly flag (high temp anomaly)
    df["Anomaly_Flag"] = df["Temperature_Anomaly"].apply(lambda x: 1 if x > df["Temperature_Anomaly"].mean() else 0)

    return df


# ==============================
# SAVE DATA
# ==============================

def save_data(df, filepath):
    df.to_csv(filepath, index=False)
    print(f"[SAVED] Cleaned data → {filepath}")


# ==============================
# PIPELINE
# ==============================

def run_pipeline():
    df = load_data(RAW_PATH)
    df = clean_data(df)
    df = feature_engineering(df)
    save_data(df, PROCESSED_PATH)


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    run_pipeline()