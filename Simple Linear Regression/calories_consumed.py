"""CALORIES CONSUMED"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

cal=pd.read_csv("C:\\EXCELR\\SOLVING_ASSIGNMENTS\\Simple Linear Regression\\calories_consumed.csv")
cal.columns
cal.shape
plt.hist(cal.weight)
plt.hist(cal.calories)
plt.boxplot(cal.weight,0,"rs",0)
plt.boxplot(cal.calories,0,"rs",0)
cal=cal.rename(columns={"Weight gained (grams)": "weight", "Calories Consumed": "calories"})

plt.scatter(cal.weight,cal.calories,color="red");plt.xlabel("weight");plt.ylabel("calories")
cal.calories.corr(cal.weight)#0.9469910088554458
#LETS BUILD THE MODEL AND R=0.9469910088554458

mod1=smf.ols("cal.calories~cal.weight",data=cal).fit()
mod1.params
mod1.summary()
"""
R=0.9469910088554458
R-squared:                       0.897
Adj. R-squared:                  0.888
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1577.2007    100.541     15.687      0.000    1358.141    1796.260
cal.weight     2.1344      0.209     10.211      0.000       1.679       2.590
==============================================================================

"""

mod1_pred=mod1.predict(cal.weight)
mod1_errors=cal.calories-mod1_pred
mod1_pred.corr(cal.calories)
plt.scatter(cal.weight,cal.calories,color="red")
plt.plot(cal.weight,mod1_pred);plt.xlabel("weight");plt.ylabel("calories")


""" I WANT TO SEE THE SCATTER DIAGRAM FOR RESIDUAL ERROR TO CHECK THE HOMOSCADASTICITY"""

import statsmodels.api as sm
fig = sm.qqplot(mod1_errors)

print(mod1.conf_int(0.01)) 