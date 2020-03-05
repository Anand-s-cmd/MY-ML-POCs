"""DELIVERY TIME"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

del_time=pd.read_csv("C:\\EXCELR\\SOLVING_ASSIGNMENTS\\Simple Linear Regression\\delivery_time.csv")
del_time.columns
del_time.shape

del_time=del_time.rename(columns={"Delivery Time": "DT", "Sorting Time": "ST"})
plt.hist(del_time.DT)
plt.hist(del_time.ST)
plt.boxplot(del_time.DT,0,"rs",0)
plt.boxplot(del_time.ST,0,"rs",0)

plt.scatter(del_time.DT,del_time.ST,color="red");plt.xlabel("weight");plt.ylabel("calories")
del_time.ST.corr(del_time.DT)#---> R=0.8259972607955325

mod1=smf.ols("del_time.ST~del_time.DT",data=del_time).fit()
mod1.summary()
"""
R=0.8259972607955325
R-squared:                       0.682
Adj. R-squared:                  0.666
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept      -0.7567      1.134     -0.667      0.513      -3.130       1.617
del_time.DT     0.4137      0.065      6.387      0.000       0.278       0.549
==============================================================================
"""
mod1_pred=mod1.predict(del_time.DT)
mod1_errors=del_time.ST-mod1_pred
mod1_pred.corr(del_time.ST)#R= 0.8259972607955326
plt.scatter(del_time.DT,del_time.ST,color="red")
plt.plot(del_time.DT,mod1_pred);plt.xlabel("DT");plt.ylabel("ST")

#LETS MOVE TOLOG MODEL

#LOG MODEL
plt.scatter(np.log(del_time.DT),del_time.ST,color="green")


mod2=smf.ols("del_time.ST~np.log(del_time.DT)",data=del_time).fit()
mod2.params# GIVES B0 AND B1

mod2.summary()
"""
 R-squared:                       0.711
 Adj. R-squared:                  0.696
 =======================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------
Intercept             -12.4992      2.751     -4.543      0.000     -18.257      -6.741
np.log(del_time.DT)     6.7355      0.985      6.836      0.000       4.673       8.798
==============================================================================
 
"""
mod2_pred=mod2.predict(del_time.DT)
mod2_errors=del_time.ST-mod2_pred
mod2_pred.corr(del_time.ST)#-->  R=0.84317726372241
plt.scatter(del_time.DT,del_time.ST,color="red")
plt.plot(del_time.DT,mod2_pred);plt.xlabel("DT");plt.ylabel("ST")

# EXPONENTIAL METHOD

mod3=smf.ols("np.log(del_time.ST)~del_time.DT",data=del_time).fit()
mod3.params
mod3.summary()

""""
R-squared:                       0.695
Adj. R-squared:                  0.679
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept       0.4372      0.204      2.139      0.046       0.009       0.865
del_time.DT     0.0769      0.012      6.587      0.000       0.052       0.101
==============================================================================
Omnibus:                        0.744   Durbin-Watson:                   1.691
Prob(Omnibus):                  0.689   Jarque-Bera (JB):                0.686
Skew:                          -0.101   Prob(JB):                        0.710
Kurtosis:                       2.138   Cond. No.                         62.1
==============================================================================
"""

mod3_pred=mod3.predict(del_time.DT)
mod3_anti_log=np.exp(mod3_pred)
mod3_errors=del_time.ST-mod3_anti_log
mod3_anti_log.corr(del_time.ST)# --> R=0.7472768828616799

plt.scatter(del_time.DT,del_time.ST,color="red")
plt.plot(del_time.DT,mod3_anti_log);plt.xlabel("DT");plt.ylabel("ST")

# QUADRATIC MODEL
del_time["DT_sq"]=del_time.DT*del_time.DT
quad_mod=smf.ols("np.log(del_time.ST)~del_time.DT+del_time.DT_sq",data=del_time).fit()
plt.scatter(del_time.DT_sq,del_time.ST,color="red")
quad_mod.summary()
"""
 R-squared:                       0.794
 Adj. R-squared:                  0.771
 ==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
Intercept         -0.7780      0.450     -1.730      0.101      -1.723       0.167
del_time.DT        0.2272      0.052      4.346      0.000       0.117       0.337
del_time.DT_sq    -0.0043      0.001     -2.928      0.009      -0.007      -0.001
==============================================================================
 
"""

quad_mod_pred=quad_mod.predict(del_time.DT)
quad_mod_anti_log=np.exp(quad_mod_pred)
quad_mod_errors=del_time.ST-quad_mod_anti_log
quad_mod_anti_log.corr(del_time.ST)#-->R= 0.8413168112143047

plt.scatter(del_time.DT,del_time.ST,color="red")
plt.plot(del_time.DT,quad_mod_anti_log);plt.xlabel("DT");plt.ylabel("ST")

print(quad_mod.conf_int(0.01)) 

""" I WANT TO SEE THE SCATTER DIAGRAM FOR RESIDUAL ERROR TO CHECK THE HOMOSCADASTICITY"""

import statsmodels.api as sm
fig = sm.qqplot(quad_mod_errors)
