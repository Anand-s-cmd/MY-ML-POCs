""" new_set_startups """
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.preprocessing import OneHotEncoder
# loading the data
startups = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\multiliear regression\\startups.csv")
startups=startups.rename(columns={"R&D Spend": "RD_spend", "Marketing Spend": "Marketing_Spend"})
startups.columns

startups.head()
""" HERE WE HAVE STATE A CATEGORICAL VARIABLE WITH 3 TYPES SO WE HAVE GO FOR ONE HOT ENCODING FOR THIS TO CONVERT"""


startups1=pd.get_dummies(startups['State'],drop_first=True)
# here 2 cols created by dropping third couln that is California
startups1.columns#Index(['Florida', 'New York'], dtype='object')

startups=pd.concat([startups,startups1],axis=1)
startups.columns
startups=startups.rename(columns={"New York": "New_York"})



""" Index(['RD_spend', 'Administration', 'Marketing_Spend', 'State', 'Profit',
       'Florida', 'New York'],
      dtype='object')"""
#so now drp State column since we have created 2 more column out of 3 states
startups.columns
startups=startups.drop('State',axis=1)# REOVING COLUMNS
"""
REMOVING ROWS 
cars_new=cars.drop(cars.index[76],axis=0)#cars_new=cars.drop(cars.index[76,70],axis=0)
"""

""" WE DID ON HOT ENCODING FOR 3 TYOES OF STATS ABOVE NOW SPLIT IT TRAIN AND TEST """

from sklearn.model_selection import train_test_split
train,test=train_test_split(startups,test_size=0.25)

train.columns
train.head()
train.corr()
import seaborn as sns
sns.pairplot(train)

train.isnull().sum()
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

train_mod1=smf.ols("Profit~RD_spend+Administration+Marketing_Spend+New_York+Florida",data=train).fit()
train_mod1.summary()
"""
R-squared:                       0.953
Adj. R-squared:                  0.946
here 
Administration    p value-->  0.924 
Marketing_Spend   p value-->  0.220 
New_York          p value-->  0.799
Florida           p value-->  0.892
so will go forsome transformation techs

"""

train_mod2=smf.ols("Profit~RD_spend+np.log(Administration)+Marketing_Spend+New_York+Florida",data=train).fit()
train_mod2.summary()

train_mod3=smf.ols("np.log(Profit)~RD_spend+Administration+Marketing_Spend+New_York+Florida",data=train).fit()
train_mod3.summary()
























