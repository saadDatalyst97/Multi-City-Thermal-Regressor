# 🤖 Multi-City Thermal Regressor (Machine Learning Pipeline)

This repository contains the complete Machine Learning operations (MLOps) pipeline for training a highly accurate "Real-Feel" temperature prediction model. The model is trained on 10 years of historical weather data across 8 major cities in Pakistan.

## 🎯 Project Overview
The goal of this project is to go beyond descriptive weather data and build a predictive AI model capable of estimating dynamic thermal comfort (Real-Feel Temperature). 

**Key Achievements:**
* **Big Data Handling:** Extracted **700,000+ rows** (10 years of data) via the Open-Meteo REST API using a custom chunking algorithm to bypass API rate limits and connection timeouts.
* **High Accuracy:** Trained a `RandomForestRegressor` achieving an R-Squared accuracy of **99.7%** and a Mean Absolute Error (MAE) of just **0.50°C**.
* **Deployment Ready:** The final model is serialized as a `.pkl` file (141 MB) for seamless integration into real-time ETL pipelines.

## 🛠️ Technology Stack
* **Language:** Python
* **Data Extraction:** `requests` (REST API)
* **Data Engineering:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (Random Forest Regressor)
* **Model Serialization:** `pickle`

## 📂 Architecture & Folder Structure

```text
Multi-City Thermal Regressor (MODEL TRAINING)/
│
├── data/
│   ├── raw/
│   │   └── All_Pakistan_10_Years_Chunked_Weather.csv  # 700k+ rows of raw API data
│   └── cleaned/
│       └── All_Pakistan_10_Years_ML_Ready.csv         # Feature-engineered data
│
├── models/
│   └── MultiCity_Thermal_Model_PRO.pkl                # The trained AI model (141 MB)
│
├── src/
│   ├── step1_data.py             # API extraction & chunking algorithm
│   ├── step2_prepare_data.py     # Data cleaning & feature encoding
│   ├── step3_train.py            # Random Forest model training & evaluation
│   └── step4_live_test.py        # Live prediction testing & QA
│
├── requirements.txt
└── README.md