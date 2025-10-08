import os
import sys
import logging

# Suppress Streamlit warnings globally before import
logging.getLogger('streamlit').setLevel(logging.ERROR)

import streamlit as st
import pickle
import numpy as np

# Load the pickled model
try:
    with open('saving.pkl', 'rb') as file:
        Model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Streamlit app title and instructions
st.title("LAPTOP PRICE PREDICTION")
st.write("Fill the following to get the laptop price prediction")

# Input fields
process = st.number_input("Processing speed (e.g., GHz)", min_value=0.1, step=0.1, value=2.5)
RAM = st.number_input("RAM Size (e.g., GB)", min_value=1, step=1, value=8)
Storage = st.number_input("Storage size (e.g., GB)", min_value=32, step=32, value=256)

# Prediction button
if st.button("Predict"):
    try:
        # Prepare input as a 2D array (1 sample, 3 features)
        input_ = np.array([[process, RAM, Storage]])
        # Make prediction
        Pred = Model.predict(input_)
        # Display result
        st.success(f"Price = {Pred[0]:.2f} RWF")
    except Exception as e:
        st.error(f"Prediction error: {e}")

# Optional: Add a note about model requirements
#st.write("Note: Ensure the model expects inputs in the order [Processing speed, RAM, Storage].")