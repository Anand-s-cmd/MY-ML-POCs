# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:51:08 2019

@author: UX009405
"""

import pandas as pd 
  
# Define a dictionary containing Students data 
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 
df

address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 
  
# Using 'Address' as the column name 
# and equating it to the list 
df['Address'] = address 
  
# Observe the result 

print(df) 

df.Name.sort_values()
df['Name'].sort_values(ascending = True)
df.sort_values('Name')


"""
----------------------------------> DOUBT NOT CLEARED
import pandas as pd 
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.columns
ufo.drop([0,1],axis=0,inplace = True)######### Q---> NOT CLEARED DOUBT
ufo.columns
"""



























