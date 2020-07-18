# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:45:50 2019

@author: UX009405
"""
import pandas as pd
import numpy as np


mydict = [{'aa': 9, 'bb': 10, 'cc': 11},
           {'a': 100, 'b': 200, 'c': 300},
           {'a': 1000, 'b': 2000, 'c': 3000},
            {'l': 1000, 'm': 2000, 'n': 3000},
            {'ll': 1000, 'mm': 2000, 'nn': 3000},
            {'l': 1000, 'mmm': 2000, 'nnn': 3000}]
 df = pd.DataFrame(mydict)
 df
type(df.loc[0])
df.loc[0]
df.loc[[0, 1]]

df.iloc[3:6]



WAYS OF SELECTING COLUMNS AND ROWS

df[df.columns[1:4]] 
df.loc[0:1, 'Name':'Address'] 
df.iloc[:, 0:2]
ufo[['City','State']]
#ROWS , COLUIMNS
DF.LOC[[,'City','State']]


"""

import pandas as pd 
  
# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data) 
  
# select all rows  
# and second to fourth column 
#-----> df[df.columns[1:4,2]] HERE WE CANNOT GIVE ROWS INDEXES SINCE WE HAVE GIVEN ONLU COLUMNS
df[df.columns[1:4]]   ##rows,columns
df[['Name','Age']]
df.loc[0:3,'Name':'Address']# RESULT IS NOT EXPECTED
df.loc[:,'Name':'Address']

df.iloc[:, 0:2]

"""
df.iloc[:, 0:2]  vs df.loc[:,'Name':'Address']
when we are giving column name then we should not give iloc only loc
when we are giving column indexes then we should not give iloc only iloc

"""