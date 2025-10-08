import streamlit as st
import numpy as np
import pickle

with open('Saving.pkl', 'rb') as file:
    Model = pickle.load(file)

st.title("LAPTOP PRICE PREDICTION")
st.write("Fill the following to get the Laptop price prediction")
process = st.number_input("Processing speed")
RAM = st.number_input("RAM Size")
Storage = st.number_input("Storage size")

if st.button("Predict"):
    input_ = np.array([[process, RAM, Storage]])
    Pred = Model.predict(input_)
    st.success(f"Price = {Pred[0]:.2f} RWF")  # Combine into a single string using f-string