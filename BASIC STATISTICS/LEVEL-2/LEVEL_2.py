"""LEVEL2 ASSIGNMENTS SOLUTIONS"""
"""
Q1"""
data=[]

import pandas as pd
data = {"Measure_X":pd.Series([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00])}
data_frame = pd.DataFrame(data) ## MAKING HERE ALSO DATA FRAME---pandas.core.frame.DataFrame
type(data_frame)
data_frame
data_frame.mean()
data_frame.var()
data_frame.std()
