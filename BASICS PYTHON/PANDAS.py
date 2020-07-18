# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:19:43 2019

@author: UX009405
"""

import pandas as pd
df1=pd.read_csv("C:\\EXCELR\\MY PYTHON SCRIPTS\\PANDAS_EXERCISES\\weather.csv")
df1

#--------------------------># USING # dictionaries 
import pandas as pd
x = {'A':[10],'C':[-12],'B':[30]}
type(x)
df1=pd.DataFrame(x)
df1
type(df1)

import pandas as pd
weather_data={'day':['1/3/2019','1/4/2019','1/5/2019','1/6/2019','1/7/2019'],'temperature':[32,24,38,26,32],'windspeed':[7,8,7,9,6],'weather':['sunny','sunny','rain','sunny','snow']}
df2=pd.DataFrame(weather_data)
df2

df2['temperature'].max()
df2['day'][df2['weather']=='sunny']
df2['day'][df2['temperature'].max()] ## ERROR

df2[df2['temperature'].max()]  ## ERROR

##
##  ---------- >> 
##-->  File "pandas\_libs\index.pyx", line 114, in pandas._libs.index.IndexEngine.get_value



##   Q----------->
import pandas as pd
x={'day':1,'name':'a','dates':['1/3/19','2/3/19']}
df=pd.DataFrame(x)
df

##-----------------> OUTPUT
##   day name   dates
##0    1    a  1/3/19
##1    1    a  2/3/19

## Q------> OPERATIONS
df['day'].mean()
df['day'].min()
df['day'].max()
df['day'].std()
df['day'].var()

import pandas as pd
#x1={'day':1,'name':'a','dates':['1/3/19',NaN]}
x1=df1=pd.read_csv("C:\\EXCELR\\MY PYTHON SCRIPTS\\PANDAS_EXERCISES\\weather_NaN.csv")
df1=pd.DataFrame(x1)
df1.fillna(0,inplace=True)
df1

##-----------OUTPUT---->
"""        day  temperature  windspeed weather
0  1/3/2019         32.0          7   sunny
1  1/4/2019         24.0          8   sunny
2  1/5/2019         38.0          7    rain
3  1/6/2019         26.0          9   sunny
4  1/7/2019          0.0          6    snow

"""


##  Q----->  SHAPE
df1.shape
##--> (5,4)---> (row,column)

row,column=df1.shape
row
column

## Q-------------> HEAD TAIL FUMCTIONS
df1.head
df1.tail

df1.head(3)
df1.tail(2)

##  Q------------>>
"""
TO PRINT FROM 2ND ROW TO 4 ROW"""
df1[2:4]
df.columns

df1['day']

df1.describe()
