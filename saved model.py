# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import pandas as pd
import numpy as np
with open('Laptop_price.sav','rb') as file:
    loaded_model=pickle.load(file))
laptop = pd.DataFrame([{
    "Processor_Speed": 3.830296,
    "RAM_Size":16,
    "Storage_Capacity":700
}])
prediction= loaded_model.predict(laptop)

print(prediction)
