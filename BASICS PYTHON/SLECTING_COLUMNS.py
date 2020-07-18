# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:46:16 2019

@author: UX009405
"""

"""
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
df.loc[0:3,'Name':'Address']
df.loc[:,'Name':'Address']

df.iloc[:, 0:2]
df.iloc[0:2, 0:2]
print(df.ix[:, 0:2])
"""
df.iloc[:, 0:2]  vs df.loc[:,'Name':'Address']
when we are giving column name then we should not give iloc only loc
when we are giving column indexes then we should not give iloc only iloc

"""