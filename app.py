import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
model = pickle.load(open("smartphone_model.pkl", "rb"))

st.title("📱 Smart Phone Price Prediction App")

st.write("Enter Phone Specifications")

# User Inputs
brand = st.selectbox("Select Brand",
                     ["Samsung", "Apple", "Xiaomi", "Oppo", "Vivo", "Realme"])

series = st.text_input("Enter Series (Galaxy, iPhone, Redmi etc)")

ram = st.number_input("RAM (GB)", 2, 24)

storage = st.number_input("Storage (GB)", 32, 1024)

camera = st.number_input("Camera (MP)", 8, 200)

battery = st.number_input("Battery (mAh)", 2000, 7000)

display = st.number_input("Display Size (inches)", 4.0, 8.0)

is_5g = st.selectbox("5G Support", ["Yes", "No"])

if st.button("Predict Price 💰"):

    input_data = pd.DataFrame([{
        "Brand": brand,
        "Series": series,
        "RAM": ram,
        "Storage": storage,
        "Camera": camera,
        "Battery": battery,
        "Display": display,
        "Processor": "Snapdragon",   # Default or add input field
        "5G": is_5g
    }])

    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹ {int(prediction[0])}")
