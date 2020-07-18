"""PRACTICE OF MLR"""
# Multilinear Regression
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# loading the data
ht = pd.read_csv(r"C:\\EXCELR\NOTES WRITTEN\\HETEROSCADASTICITY\\Heteroscedasticity.csv")
type(ht)

ht.corr()
"""
              Accidents  AccidentRate  Population    Weight
Accidents      1.000000     -0.121857    0.926070 -0.689545
AccidentRate  -0.121857      1.000000   -0.390980  0.208558
Population     0.926070     -0.390980    1.000000 -0.695078
Weight        -0.689545      0.208558   -0.695078  1.000000
"""
import seaborn as sns
sns.pairplot(ht)
ht.columns

mod1=smf.ols("Accidents~AccidentRate+Population+Weight",data=ht).fit()
mod1.summary()
"""
R-squared:                       0.92
Adj. R-squared:                  0.925
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      -12.9112      2.923     -4.416      0.000     -18.709      -7.113
AccidentRate   1.89e+05   1.96e+04      9.635      0.000     1.5e+05    2.28e+05
Population     7.74e-05   3.06e-06     25.276      0.000    7.13e-05    8.35e-05
Weight       -2.501e+05    1.7e+05     -1.469      0.145   -5.88e+05    8.77e+04
==============================================================================
SINCE WEIGHT IS NOT SIGNIFICANT WE ARE REMOVING
"""
mod2=smf.ols("Accidents~AccidentRate+Population",data=ht).fit()
mod2.summary()
"""
R-squared:                       0.926
Adj. R-squared:                  0.924
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      -15.4386      2.376     -6.497      0.000     -20.151     -10.726
AccidentRate  1.917e+05   1.96e+04      9.766      0.000    1.53e+05    2.31e+05
Population    8.047e-05   2.25e-06     35.712      0.000     7.6e-05    8.49e-05
==============================================================================
"""

acc_pred=mod2.predict(ht)
resid_errors=ht.Accidents-acc_pred
acc_pred.corr(ht.Accidents)#0.9621446772017527
rmse = np.sqrt(np.mean(resid_errors*resid_errors)) #5.0687684955228995

# Observed values VS Fitted values
plt.scatter(ht.Accidents,acc_pred,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
"""HERE WE ARE CHECKING LINEARITY BTW Y=B0+B1 THAT IS Y=Y^
AFTER BUILDING THE MODEL THAT PREDICTED VALUES THAT IS AGAIN MPG_PRED"""

#CHECKING HOMOHETERSCEDASTICITY
plt.scatter(acc_pred,mod2.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")

"""here our model has variance in the errors that heteroscadasticity"""

""""LETS DO NORMALIZATION AND CHECK ON BOTH VARIABLES"""
# Normalization function 
def norm_func(i):
    x = (i-i.min())	/	(i.max()	-	i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
#df_norm1 = norm_func(ht.iloc[:,])
df_norm = norm_func(ht.iloc[:,0:3])#--> normalized now on all variable exepct weight
# lets see again
type(df_norm)
df_norm.columns

mod3=smf.ols("Accidents~AccidentRate+Population",data=df_norm).fit()
mod3.summary()
"""
R-squared:                       0.926
Adj. R-squared:                  0.924
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       -0.0920      0.021     -4.372      0.000      -0.134      -0.050
AccidentRate     0.4152      0.043      9.766      0.000       0.331       0.499
Population       0.8049      0.023     35.712      0.000       0.760       0.850
==============================================================================
"""


acc_pred2=mod3.predict(df_norm)
resid_errors2=df_norm.Accidents-acc_pred2
acc_pred2.corr(df_norm.Accidents)# 0.9621446772017526
rmse2 = np.sqrt(np.mean(resid_errors2*resid_errors2)) #0.061069499945898026

# Observed values VS Fitted values
plt.scatter(df_norm.Accidents,acc_pred2,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
"""HERE WE ARE CHECKING LINEARITY BTW Y=B0+B1 THAT IS Y=Y^
AFTER BUILDING THE MODEL THAT PREDICTED VALUES THAT IS AGAIN MPG_PRED"""

#CHECKING HOMOHETERSCEDASTICITY
plt.scatter(acc_pred2,mod3.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")

"""here our model has variance in the errors that heteroscadasticity"""


"""stilll same we got lets do transformation tech on variables and see"""

""" BEFORE THAT CHECK THE HISTOGRAM HOW DATA IS DISTRUBUTED FOR BOTH ACC RATE AND POPULATION""""

import matplotlib.pyplot as plt
plt.hist(df_norm.AccidentRate)#right skewed
plt.hist(df_norm.Population)#neither right not left
#apply transformation   here down i used original population data for log trans
# rather than normalized data because i got error der
df_norm['new']=np.log(ht.Population)
df_norm.columns
plt.hist(df_norm.new)#left skewed now

mod5=smf.ols("Accidents~AccidentRate+new",data=df_norm).fit()
mod5.summary()
"""
R-squared:                       0.872
Adj. R-squared:                  0.870
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       -3.6272      0.156    -23.281      0.000      -3.936      -3.318
AccidentRate     0.3661      0.055      6.619      0.000       0.256       0.476
new              0.3085      0.012     26.408      0.000       0.285       0.332
==============================================================================
"""
 
acc_pred3=mod5.predict(df_norm)
resid_errors3=df_norm.Accidents-acc_pred3
acc_pred3.corr(df_norm.Accidents)#  0.9338918966165611
rmse3 = np.sqrt(np.mean(resid_errors3*resid_errors3)) #0.08011960865047725

# Observed values VS Fitted values
plt.scatter(df_norm.Accidents,acc_pred3,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
"""HERE WE ARE CHECKING LINEARITY BTW Y=B0+B1 THAT IS Y=Y^
AFTER BUILDING THE MODEL THAT PREDICTED VALUES THAT IS AGAIN MPG_PRED"""

#CHECKING HOMOHETERSCEDASTICITY
plt.scatter(acc_pred3,mod5.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")

df_norm.columns
df_norm.drop('new',axis=1,inplace=True)
df_norm.columns


mod6=smf.ols("np.log(Accidents)~AccidentRate+Population",data=ht).fit()
mod6.summary()
"""
R-squared:                       0.843
Adj. R-squared:                  0.840

================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        1.2413      0.130      9.521      0.000       0.983       1.500
AccidentRate  1.013e+04   1077.134      9.402      0.000    7991.750    1.23e+04
Population    2.921e-06   1.24e-07     23.627      0.000    2.68e-06    3.17e-06
==============================================================================
"""

acc_pred4=mod6.predict(ht)
resid_errors4=ht.Accidents-acc_pred4
acc_pred4.corr(ht.Accidents)#  0.9338918966165611
rmse4 = np.sqrt(np.mean(resid_errors3*resid_errors3)) #  0.08011960865047725

# Observed values VS Fitted values
plt.scatter(ht.Accidents,acc_pred4,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
"""HERE WE ARE CHECKING LINEARITY BTW Y=B0+B1 THAT IS Y=Y^
AFTER BUILDING THE MODEL THAT PREDICTED VALUES THAT IS AGAIN MPG_PRED"""

#CHECKING HOMOHETERSCEDASTICITY
plt.scatter(acc_pred4,mod6.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")



#inverse transformation
def inverse_func(i):
    x = 1/i
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm_inverse = inverse_func(ht.iloc[:,-2])
ht['new']=df_norm_inverse
ht.columns
ht.head(5)

def norm_func(i):
    x = (i-i.min())	/	(i.max()	-	i.min())
    return (x)


# Normalized data frame (considering the numerical part of data)
df_norm_1 = norm_func(ht.iloc[:,0])
ht['mew_Accidents']=df_norm_1
ht.columns


mod7=smf.ols("mew_Accidents~np.log(AccidentRate)+new",data=ht).fit()
mod7.summary()

acc_pred5=mod7.predict(ht)
resid_errors5=ht.mew_Accidents-acc_pred5
acc_pred5.corr(ht.mew_Accidents)#  0.6895525501955752
rmse5 = np.sqrt(np.mean(resid_errors5*resid_errors5)) #  0.08011960865047725

# Observed values VS Fitted values
plt.scatter(ht.mew_Accidents,acc_pred5,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
"""HERE WE ARE CHECKING LINEARITY BTW Y=B0+B1 THAT IS Y=Y^
AFTER BUILDING THE MODEL THAT PREDICTED VALUES THAT IS AGAIN MPG_PRED"""

#CHECKING HOMOHETERSCEDASTICITY
plt.scatter(acc_pred5,mod7.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")








