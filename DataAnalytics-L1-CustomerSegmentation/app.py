import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Get the folder this script lives in, so file paths work regardless of working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the saved model and scaler
kmeans = joblib.load(os.path.join(BASE_DIR, 'kmeans_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'rfm_scaler.pkl'))

st.set_page_config(page_title="Customer Segmentation", page_icon="📊")
st.title("📊 Customer Segment Predictor")
st.write("Enter a customer's RFM values to predict which segment they belong to.")

# Input fields
recency = st.number_input("Recency (days since last purchase)", min_value=0, value=30)
frequency = st.number_input("Frequency (number of orders)", min_value=0, value=5)
monetary = st.number_input("Monetary (total amount spent)", min_value=0.0, value=500.0)

if st.button("Predict Segment"):
    # Prepare input in the same column order used for training
    input_data = pd.DataFrame([[recency, frequency, monetary]], 
                                columns=['Recency', 'Frequency', 'Monetary'])
    input_scaled = scaler.transform(input_data)
    cluster = kmeans.predict(input_scaled)[0]

    # Segment descriptions based on your cluster profile analysis
    segment_info = {
        0: ("Regular / Active Customer", "Buys fairly often and recently — a steady, engaged customer."),
        1: ("Lapsed / Low-Value Customer", "Hasn't purchased in a long time and spends little — at risk of churning."),
        2: ("High-Value Frequent Buyer", "Purchases often and spends significantly — a valuable, loyal customer."),
        3: ("Top-Tier VIP Customer", "Extremely frequent, high-spending, and recent — your most valuable customer segment.")
    }

    label, description = segment_info.get(cluster, ("Unknown", ""))
    st.success(f"**Predicted Segment: Cluster {cluster} — {label}**")
    st.write(description)
