import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

DATA_PATH = "dataset/processed_data/climate_cleaned.csv"


def load_data():
    df = pd.read_csv(DATA_PATH)
    print(f"[INFO] Loaded data: {df.shape}")
    return df


def prepare_data(df):

    # Convert only needed columns
    df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
    df["Temperature_Anomaly"] = pd.to_numeric(df["Temperature_Anomaly"], errors='coerce')

    # 🔥 ONLY drop required columns
    df = df.dropna(subset=["Year", "Temperature_Anomaly"])

    print("[INFO] Data after cleaning:", df.shape)

    # Use ONLY Year (simple + stable)
    X = df[["Year"]]
    y = df["Temperature_Anomaly"]

    return X, y


def train_model(X, y):

    print("[DEBUG] X shape:", X.shape)
    print("[DEBUG] y shape:", y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\n===== MODEL PERFORMANCE =====")
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R² Score:", r2_score(y_test, y_pred))

    return model


def run_model():
    df = load_data()
    X, y = prepare_data(df)
    model = train_model(X, y)
    print("\n[SUCCESS] Model trained successfully!")


if __name__ == "__main__":
    run_model()