
# 🌍 ClimateTrend Analyzer
### Detecting Long-Term Climate Change Patterns

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.1-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📌 Project Overview

ClimateTrend Analyzer is a **Data Science mini project** that analyzes long-term global climate change patterns using real-world datasets. The project examines historical temperature anomalies, CO₂ concentration, and rainfall data to uncover trends, detect anomalies, and predict future climate trajectories.

---

## 🎯 Problem Statement

Climate change is one of the most critical global challenges. Despite the availability of large historical climate datasets, identifying meaningful patterns and predicting future trends remains complex. This project aims to:

- Analyze historical temperature and CO₂ data (1880–present)
- Detect years with extreme temperature anomalies
- Visualize the relationship between CO₂ emissions and global warming
- Build a regression model to forecast future temperature trends

---

## 📋 Abstract

Global climate change driven by greenhouse gas emissions poses unprecedented challenges. This project develops a **ClimateTrend Analyzer** using Python-based data science tools to detect and visualize long-term climate patterns. Using NASA GISS temperature anomaly data and NOAA CO₂ records spanning over 140 years, the system performs exploratory data analysis, feature engineering, and anomaly detection. Seven comprehensive visualizations reveal a clear upward trend in global temperatures — with post-1980 anomalies consistently exceeding historical baselines. A correlation of **r > 0.97** between CO₂ concentration and temperature anomaly confirms the greenhouse effect. Linear and polynomial regression models are trained to predict future temperature anomalies, with the polynomial model achieving an R² of approximately 0.95. Results indicate that without intervention, temperatures could rise 1.5–2°C above the pre-industrial baseline by 2050, aligning with IPCC projections.

---

## 📁 Repository Structure

```
MiniProject/
│
├── README.md                        ← You are here
├── requirements.txt                 ← Python dependencies
│
├── docs/
│   ├── abstract.pdf
│   ├── problem_statement.pdf
│   └── presentation.pptx
│
├── dataset/
│   ├── raw_data/
│   │   └── climate_data.csv        ← Place downloaded dataset here
│   └── processed_data/
│       └── climate_cleaned.csv     ← Auto-generated after preprocessing
│
├── notebooks/
│   ├── data_understanding.ipynb    ← Step 1: Explore raw data
│   ├── preprocessing.ipynb         ← Step 2: Clean & engineer features
│   └── visualization.ipynb         ← Step 3: All charts & EDA
│
├── src/
│   ├── preprocessing.py            ← Reusable preprocessing module
│   ├── analysis.py                 ← EDA + visualization module
│   └── model.py                    ← Prediction model module
│
├── outputs/
│   ├── graphs/                     ← All saved charts (PNG)
│   └── results/
│       └── model_results.json      ← Model metrics (MAE, RMSE, R²)
│
└── report/
    └── mini_project_report.pdf
```

---

## 📊 Dataset

| Source | Dataset | Link |
|--------|---------|------|
| NASA GISS | Global Surface Temperature (GISTEMP v4) | [Download](https://data.giss.nasa.gov/gistemp/) |
| NOAA | Atmospheric CO₂ – Mauna Loa Observatory | [Download](https://gml.noaa.gov/ccgg/trends/data.html) |
| World Bank | Global Rainfall Data | [Download](https://data.worldbank.org/indicator/AG.LND.PRCP.MM) |

**Expected columns in `climate_data.csv`:**
```
Year, Temperature_Anomaly, CO2_ppm, Rainfall_mm
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone .git
cd ClimateTrend-Analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download & place dataset
Download the dataset and save it as:
```
dataset/raw_data/climate_data.csv
```

### 4. Run the pipeline (recommended order)

**Option A: Notebooks (beginner-friendly)**
```bash
jupyter notebook
# Open notebooks in order:
# 1. data_understanding.ipynb
# 2. preprocessing.ipynb
# 3. visualization.ipynb
```

**Option B: Python scripts (faster)**
```bash
python src/preprocessing.py   # Clean & prepare data
python src/analysis.py         # Generate all graphs
python src/model.py            # Train & evaluate model
```

---

## 📈 Visualizations Generated

| # | Chart | Description |
|---|-------|-------------|
| 1 | Temperature Trend | Annual + rolling mean anomaly over time |
| 2 | CO₂ Trend | Atmospheric CO₂ rise since 1958 |
| 3 | CO₂ vs Temperature | Scatter plot showing correlation |
| 4 | Anomaly Detection | Highlight extreme warming years |
| 5 | Decade Average | Average anomaly grouped by decade |
| 6 | Correlation Heatmap | Relationships between all features |
| 7 | Rainfall Trend | Annual precipitation over time |
| 8 | Model Predictions | Actual vs predicted + 20-year forecast |
| 9 | Residuals | Model quality diagnostics |

---

## 🤖 Model Results

| Model | MAE | RMSE | R² |
|-------|-----|------|----|
| Linear Regression | ~0.08°C | ~0.10°C | ~0.90 |
| Polynomial (deg=2) | ~0.05°C | ~0.07°C | ~0.95 |

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Data:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **ML:** Scikit-learn (LinearRegression, PolynomialFeatures)
- **Notebooks:** Jupyter

---

## 👤 Author

👤 Author

Atchaya Parthipan – 3rd Year B.Tech CSE (AI & ML) – atchayaatchaya702@email.com  
Laxmi Priya TM – 3rd Year B.Tech CSE (AI & ML)  – lax@email.com

---


