""" Emp_data -> Build a prediction model for Churn_out_rate """
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

emp=pd.read_csv("C:\\EXCELR\\SOLVING_ASSIGNMENTS\\Simple Linear Regression\\emp_data.csv")
emp.columns
emp.shape

emp=emp.rename(columns={"Salary_hike": "salary", "Churn_out_rate": "churn"})
plt.hist(emp.salary)
plt.hist(emp.churn)
plt.boxplot(emp.salary,0,"rs",0)
plt.boxplot(emp.churn,0,"rs",0)

plt.scatter(emp.salary,emp.churn,color="red");plt.xlabel("weight");plt.ylabel("calories")
emp.churn.corr(emp.salary)#---> R=-0.9117216186909108

mod1=smf.ols("emp.churn~emp.salary",data=emp).fit()
mod1.summary()
"""
R-squared:                       0.831
Adj. R-squared:                  0.810

==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    244.3649     27.352      8.934      0.000     181.291     307.439
emp.salary    -0.1015      0.016     -6.277      0.000      -0.139      -0.064
==============================================================================
Omnibus:                        2.201   Durbin-Watson:                   0.562
Prob(Omnibus):                  0.333   Jarque-Bera (JB):                1.408
Skew:                           0.851   Prob(JB):                        0.495
Kurtosis:                       2.304   Cond. No.                     3.27e+04
==============================================================================

"""
mod1_pred=mod1.predict(emp.salary)
mod1_errors=emp.churn-mod1_pred
mod1_pred.corr(emp.churn)#---> R=0.9117216186909112
plt.scatter(emp.salary,emp.churn,color="red")
plt.plot(emp.salary,mod1_pred);plt.xlabel("DT");plt.ylabel("ST")

print(mod1.conf_int(0.01)) 

""" I WANT TO SEE THE SCATTER DIAGRAM FOR RESIDUAL ERROR TO CHECK THE HOMOSCADASTICITY"""

import statsmodels.api as sm
fig = sm.qqplot(mod1_errors)

