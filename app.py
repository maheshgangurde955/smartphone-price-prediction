import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Model
# -------------------------------
model = pickle.load(open("smartphone_model.pkl", "rb"))

st.title("📱 Smart Phone Price Prediction App")

st.write("Enter phone specifications below:")

# -------------------------------
# User Inputs
# -------------------------------

brand = st.selectbox("Select Brand", 
                     ["Samsung", "Apple", "Xiaomi", "Oppo", "Vivo", "Realme"])

series = st.text_input("Enter Series (Galaxy, iPhone, Redmi, etc)")

ram = st.number_input("Enter RAM (GB)", min_value=2, max_value=24, step=1)

storage = st.number_input("Enter Storage (GB)", min_value=32, max_value=1024, step=32)

camera = st.number_input("Enter Camera (MP)", min_value=8, max_value=200, step=2)

battery = st.number_input("Enter Battery (mAh)", min_value=2000, max_value=7000, step=100)

display = st.number_input("Enter Display Size (inches)", min_value=4.0, max_value=8.0, step=0.1)

processor = st.text_input("Enter Processor")

is_5g = st.radio("5G Support?", ["Yes", "No"])

# Convert Yes/No to 1/0
if is_5g == "Yes":
    is_5g = 1
else:
    is_5g = 0


# -------------------------------
# Prediction Button
# -------------------------------

if st.button("Predict Price 💰"):

    input_data = pd.DataFrame([[
        ram, storage, camera, battery, display, is_5g
    ]], columns=["RAM", "Storage", "Camera", "Battery", "Display", "5G"])

    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹ {int(prediction[0])}")
