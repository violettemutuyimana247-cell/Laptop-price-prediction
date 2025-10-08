# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 21:07:06 2025

@author: user
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the trained model
with open('Laptop_price.sav','rb')as file:
    loaded_model = pickle.load(file)

def laptop_price_prediction(Processor_Speed, RAM_Size, Storage_Capacity):
    # Create a dataframe for the model
    laptop = pd.DataFrame([{
        "Processor_Speed": Processor_Speed,
        "RAM_Size": RAM_Size,
        "Storage_Capacity": Storage_Capacity
    }])
    
    # Predict the price
    predicted_price = loaded_model.predict(laptop)
    return predicted_price[0]

def main():
    st.title('Laptop Price Prediction')

    # Input fields
    Processor_Speed = st.text_input('Enter the speed of processor')
    RAM_Size = st.text_input('Enter the RAM size')
    Storage_Capacity = st.text_input('Enter the Storage capacity')

    if st.button('Predict Price'):
        try:
            # Convert inputs to numeric types
            Processor_Speed = float(Processor_Speed)
            RAM_Size = int(RAM_Size)
            Storage_Capacity = int(Storage_Capacity)
            
            # Get prediction
            price = laptop_price_prediction(Processor_Speed, RAM_Size, Storage_Capacity)
            st.success(f'The predicted price for the laptop is: Rwf {price:.2f}')
        except ValueError:
            st.error("Please enter valid numeric values for Processor_Speed, RAM_Size, and Storage_Capacity.")

if __name__ == '__main__':
    main()

