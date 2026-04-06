import pandas as pd

# ==============================
# LOAD TEMPERATURE DATA
# ==============================

temp = pd.read_csv(
    "dataset/raw_data/temperature.csv",
    skiprows=1,
    on_bad_lines='skip'
)

temp = temp.iloc[:, :2]
temp.columns = ["Year", "Temperature_Anomaly"]

temp["Year"] = pd.to_numeric(temp["Year"], errors='coerce')
temp["Temperature_Anomaly"] = pd.to_numeric(temp["Temperature_Anomaly"], errors='coerce')

temp = temp.dropna()


# ==============================
# LOAD CO2 DATA (ROBUST)
# ==============================

with open("dataset/raw_data/co2.csv", "r") as f:
    lines = f.readlines()

clean_data = []

for line in lines:
    if line.startswith("#") or len(line.strip()) == 0:
        continue

    parts = line.strip().split()

    if len(parts) >= 2:
        year = parts[0]
        co2_val = parts[1]
        clean_data.append([year, co2_val])

co2 = pd.DataFrame(clean_data, columns=["Year", "CO2_ppm"])

co2["Year"] = pd.to_numeric(co2["Year"], errors='coerce')
co2["CO2_ppm"] = pd.to_numeric(co2["CO2_ppm"], errors='coerce')

co2 = co2.dropna()


# ==============================
# LOAD RAINFALL DATA
# ==============================

rain = pd.read_csv("dataset/raw_data/rainfall.csv")

rain = rain[["Year", "Rainfall_mm"]]

rain["Year"] = pd.to_numeric(rain["Year"], errors='coerce')
rain["Rainfall_mm"] = pd.to_numeric(rain["Rainfall_mm"], errors='coerce')

rain = rain.dropna()


# ==============================
# MERGE ALL DATA (FIXED)
# ==============================

df = temp.merge(co2, on="Year", how="outer")
df = df.merge(rain, on="Year", how="outer")

df = df.sort_values(by="Year")

# Fill missing values forward
df = df.fillna(method='ffill')


# ==============================
# SAVE FINAL FILE
# ==============================

df.to_csv("dataset/raw_data/climate_data.csv", index=False)

print("✅ climate_data.csv created successfully!!")
