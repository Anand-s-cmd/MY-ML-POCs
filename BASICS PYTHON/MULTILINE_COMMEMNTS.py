# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:13:05 2019

@author: UX009405
"""

import pandas as pd
#x1={'day':1,'name':'a','dates':['1/3/19',NaN]}
x1=df1=pd.read_csv("C:\\EXCELR\\MY PYTHON SCRIPTS\\PANDAS_EXERCISES\\weather_NaN.csv")
df1=pd.DataFrame(x1)
df1.fillna(0,inplace=True)
df1
df1
##-----------OUTPUT---->
"""        day  temperature  windspeed weather
0  1/3/2019         32.0          7   sunny
1  1/4/2019         24.0          8   sunny
2  1/5/2019         38.0          7    rain
3  1/6/2019         26.0          9   sunny
4  1/7/2019          0.0          6    snow

"""
