#NOTE : WHEN A VARIABLE IS NOT REMOVED MEANS ADDED STILL IT IS NOT CONTRIBUTING THEN ADJUSTED R SQ VALUE WILL BE LESS THAN MULTIPLE R 2
#BECAE IT CHECK WHETHER VAR IS CONTRIBUTING OR MOT

""" Salary_hike -> Build a prediction model for Salary_hike """
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

sal_hike=pd.read_csv("C:\\EXCELR\\SOLVING_ASSIGNMENTS\\Simple Linear Regression\\Salary_Data.csv")
sal_hike.columns
sal_hike.shape
sal_hike=sal_hike.rename(columns={"YearsExperience": "exp", "Salary": "sal"})


plt.hist(sal_hike.exp)
plt.hist(sal_hike.sal)
plt.boxplot(sal_hike.exp,0,"rs",0)
plt.boxplot(sal_hike.sal,0,"rs",0)

plt.scatter(sal_hike.exp,sal_hike.sal,color="red");plt.xlabel("exp");plt.ylabel("sal")
emp.churn.corr(emp.salary)# R=-0.9117216186909108

mod1=smf.ols("sal_hike.sal~sal_hike.exp",data=sal_hike).fit()
mod1.summary()
"""
 R-squared:                       0.957
 Adj. R-squared:                  0.955
 ================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     2.579e+04   2273.053     11.347      0.000    2.11e+04    3.04e+04
sal_hike.exp  9449.9623    378.755     24.950      0.000    8674.119    1.02e+04
==============================================================================
Omnibus:                        2.140   Durbin-Watson:                   1.648
Prob(Omnibus):                  0.343   Jarque-Bera (JB):                1.569
Skew:                           0.363   Prob(JB):                        0.456
Kurtosis:                       2.147   Cond. No.                         13.2
==============================================================================
"""

mod1_pred=mod1.predict(sal_hike.exp)
mod1_errors=sal_hike.sal-mod1_pred
mod1_pred.corr(sal_hike.sal)#---> R=0.9782416184887597
plt.scatter(sal_hike.exp,sal_hike.sal,color="red")
plt.plot(sal_hike.exp,mod1_pred);plt.xlabel("DT");plt.ylabel("ST")


print(mod1.conf_int(0.01)) 

""" I WANT TO SEE THE SCATTER DIAGRAM FOR RESIDUAL ERROR TO CHECK THE HOMOSCADASTICITY"""

import statsmodels.api as sm
fig = sm.qqplot(mod1_errors)
