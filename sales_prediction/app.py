import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/walmart_sales_model.pkl")

st.title("🛒 Weekly Sales Prediction")

st.write("Enter the required details to predict the weekly sales for a store & department.")

# User Inputs
store = st.number_input("Store Number", min_value=1, max_value=50, step=1)
dept = st.number_input("Department Number", min_value=1, max_value=100, step=1)
is_holiday = st.selectbox("Is Holiday?", ["No", "Yes"])
temperature = st.number_input("Temperature (F)", step=0.1)
fuel_price = st.number_input("Fuel Price", step=0.01)
cpi = st.number_input("CPI", step=0.01)
unemployment = st.number_input("Unemployment Rate", step=0.01)
store_type = st.selectbox("Store Type", ["A", "B", "C"])
size = st.number_input("Store Size", step=100)
year = st.number_input("Year", min_value=2010, max_value=2030, step=1)
month = st.number_input("Month", min_value=1, max_value=12, step=1)
week = st.number_input("Week Number", min_value=1, max_value=52, step=1)

# Convert categorical to numeric if needed
is_holiday = 1 if is_holiday == "Yes" else 0

type_map = {"A": 1, "B": 2, "C": 3}
store_type = type_map[store_type]

# Prepare input for model
input_data = pd.DataFrame([[
    store, dept, is_holiday, temperature, fuel_price, 0, 0, 0, 0, 0,
    cpi, unemployment, store_type, size, year, month, week
]], columns=[
    'Store','Dept','IsHoliday_x','Temperature','Fuel_Price',
    'MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5',
    'CPI','Unemployment','Type','Size','Year','Month','Week'
])

if st.button("Predict Weekly Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Weekly Sales: **${prediction:,.2f}**")
