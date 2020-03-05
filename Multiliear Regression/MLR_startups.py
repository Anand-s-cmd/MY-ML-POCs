import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.preprocessing import OneHotEncoder
# loading the data
startups = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\multiliear regression\\startups.csv", usecols = ["R&D Spend", "Administration", "Marketing Spend", "Profit"])
#startups = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\multiliear regression\\startups.csv")
type(startups)
startups.columns
startups.corr()
startups=startups.rename(columns={"R&D Spend": "RD_spend", "Marketing Spend": "Marketing_Spend"})
mod1=smf.ols("Profit~RD_spend+Administration+Marketing_Spend",data=startups).fit()
import seaborn as sns
sns.pairplot(startups)
mod1.summary()
"""
R-squared:                       0.951
Adj. R-squared:                  0.948
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
Intercept        5.012e+04   6572.353      7.626      0.000    3.69e+04    6.34e+04
RD_spend            0.8057      0.045     17.846      0.000       0.715       0.897
Administration     -0.0268      0.051     -0.526      0.602      -0.130       0.076
Marketing_Spend     0.0272      0.016      1.655      0.105      -0.006       0.060
==============================================================================

"""
mod_Administration=smf.ols("Profit~Administration",data=startups).fit()
mod_Administration.summary()
"""
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
Intercept       7.697e+04   2.53e+04      3.040      0.004    2.61e+04    1.28e+05
Administration     0.2887      0.203      1.419      0.162      -0.120       0.698
==============================================================================
"""

mod_Marketing_Spend=smf.ols("Profit~Marketing_Spend",data=startups).fit()
mod_Marketing_Spend.summary()
"""
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
Intercept            6e+04   7684.530      7.808      0.000    4.46e+04    7.55e+04
Marketing_Spend     0.2465      0.032      7.803      0.000       0.183       0.310
==============================================================================
"""

"""SO HERE DROP Administration SINCE IT IS INSIGNIFICANT"""


mod2=smf.ols("Profit~RD_spend+Marketing_Spend",data=startups).fit()
mod2.summary()
 """
 R-squared:                       0.950
 Adj. R-squared:                  0.948
 ===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
Intercept        4.698e+04   2689.933     17.464      0.000    4.16e+04    5.24e+04
RD_spend            0.7966      0.041     19.266      0.000       0.713       0.880
Marketing_Spend     0.0299      0.016      1.927      0.060      -0.001       0.061
==============================================================================
 
"""
import statsmodels.api as sm
""" HERE AVPLOTS IS LIKE sm.graphics.plot_partregress_grid(ml_new)"""
# Added varible plot 
sm.graphics.plot_partregress_grid(mod2)

#TO REMIVE OUTLIERS AS WELL FOR ALL ROWS
sm.graphics.influence_plot(mod1)
startups_new=startups.drop(startups.index[49],axis=0)
 
final_mod=smf.ols("Profit~RD_spend+Marketing_Spend",data=startups_new).fit()
final_mod.summary()

"""
  R-squared:                       0.961
 Adj. R-squared:                  0.959

                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
Intercept        4.979e+04   2341.584     21.261      0.000    4.51e+04    5.45e+04
RD_spend            0.7754      0.035     22.136      0.000       0.705       0.846
Marketing_Spend     0.0274      0.013      2.104      0.041       0.001       0.054
==============================================================================
"""
 
Profit_PRED=final_mod.predict(startups_new)
resid_errors=startups_new.Profit-Profit_PRED
zero_mean_error=np.sum(resid_errors)#---> -1.4260876923799515e-09
Profit_PRED.corr(startups_new.Profit)#  0.980349774695574
rmse = np.sqrt(np.mean(resid_errors*resid_errors)) #7452.700079547002

sm.graphics.plot_partregress_grid(final_mod)

# Observed values VS Fitted values
plt.scatter(startups_new.Profit,Profit_PRED,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")

#CHECKING HOMOHETERSCEDASTICITY
plt.scatter(Profit_PRED,final_mod.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")
#ABOBE CHECKING HOMESCEDASTICITY
# histogram
plt.hist(final_mod.resid_pearson) # Checking the standardized residuals are normally distributed

# QQ plot for residuals 
import pylab          
import scipy.stats as st

# Checking Residuals are normally distributed
st.probplot(final_mod.resid_pearson, dist="norm", plot=pylab)


from sklearn.model_selection import train_test_split
startups_train,startups_test  = train_test_split(startups_new,test_size = 0.2) # 20% size

#TAKING cars_train DATA SET BECAUSE IT HAS NO OUTLIERS
# preparing the model on train data 

model_train = smf.ols("Profit~RD_spend+Marketing_Spend",data=startups_train).fit()

# train_data prediction
train_pred = model_train.predict(startups_train)

# train residual values 
train_resid  = train_pred - startups_train.Profit

# RMSE value for train data 
train_rmse = np.sqrt(np.mean(train_resid*train_resid)) # 7599.661538121529

# prediction on test data set 
test_pred = model_train.predict(startups_test)

# test residual values 
test_resid  = test_pred - startups_test.Profit

# RMSE value for test data 
test_rmse = np.sqrt(np.mean(test_resid*test_resid)) # 7502.589496079839

"""
original rmse is 7452.700079547002
train_rmse     7599.661538121529
test_rmse      7502.589496079839"""


