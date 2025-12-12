# 📦 SmartStock – Inventory Optimization & Sales Forecasting

SmartStock is a machine-learning powered solution designed to help retail stores **optimize inventory**, **forecast weekly sales**, and make **data-driven decisions**.  
Using Walmart’s historical sales dataset, the system predicts weekly sales based on store, department, seasonal features, and economic indicators.

---

## 🚀 Project Features

### 🔹 1. Data Preparation Module
- Cleaned and merged `train.csv`, `features.csv`, and `stores.csv`
- Handled missing values and numerical imputation  
- Created engineered features including:
  - **Year**, **Month**, **Week**
  - Store type encoding  
  - Holiday indicator  
- Prepared a final ML-ready dataset

---

### 🔹 2. Model Development Module
- Trained multiple ML models and finalized **XGBoost Regressor**
- Achieved high performance:
  - **MAE:** ~2124  
  - **RMSE:** ~3943  
  - **R² Score:** **0.97 (97% accuracy)**  
- Exported trained model as:


---

### 🔹 3. UI Development Module (Streamlit)
A clean web interface allowing users to enter store details and instantly receive sales predictions.

User inputs include:
- Store Number  
- Department  
- Holiday Flag  
- Temperature  
- Fuel Price  
- CPI  
- Unemployment  
- Store Type  
- Store Size  
- Year, Month, Week  

Run using:
```bash
streamlit run app.py
```
### 🔹 4. Final Deployment Module

-Created virtual environment

-Installed dependencies

-Loaded exported ML model

-Integrated model with Streamlit UI

-Prepared project for GitHub deployment and future cloud hosting

### 📁 Project Structure
``` sql
springboard_sales_ml/
│── sales_prediction/
│   ├── app.py
│   ├── model/
│   │   └── walmart_sales_model.pkl
│── venv/
│── README.md
│── .gitignore
```
