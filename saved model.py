# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import pandas as pd
import numpy as np
loaded_model=pickle.load(open('C:/Users/user/Downloads/Lap top/Laptop_price.sav','rb'))
laptop = pd.DataFrame([{
    "Processor_Speed": 3.830296,
    "RAM_Size":16,
    "Storage_Capacity":700
}])
prediction= loaded_model.predict(laptop)
print(prediction)