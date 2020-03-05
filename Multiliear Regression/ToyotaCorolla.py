# Multilinear Regression
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# loading the data
ToyotaCorolla = pd.read_csv("C:\\EXCELR\\SOLVING_ASSIGNMENTS\\multiliear regression\\ToyotaCorolla.csv", usecols = ["Price","Age_08_04","KM","HP","cc","Doors","Gears","Quarterly_Tax","Weight"])
type(ToyotaCorolla)

ToyotaCorolla.columns
ToyotaCorolla.shape
ToyotaCorolla.head()

ToyotaCorolla.corr()
import seaborn as sns
sns.pairplot(ToyotaCorolla)

mod1=smf.ols("Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight",data=ToyotaCorolla).fit()
mod1.params
mod1.summary()
"""
==============================================================================
Dep. Variable:                  Price   R-squared:                       0.864
Model:                            OLS   Adj. R-squared:                  0.863
Method:                 Least Squares   F-statistic:                     1131.
Date:                Thu, 17 Oct 2019   Prob (F-statistic):               0.00
Time:                        16:25:29   Log-Likelihood:                -12376.
No. Observations:                1436   AIC:                         2.477e+04
Df Residuals:                    1427   BIC:                         2.482e+04
Df Model:                           8                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept     -5573.1064   1411.390     -3.949      0.000   -8341.728   -2804.485
Age_08_04      -121.6584      2.616    -46.512      0.000    -126.789    -116.527
KM               -0.0208      0.001    -16.622      0.000      -0.023      -0.018
HP               31.6809      2.818     11.241      0.000      26.152      37.209
cc               -0.1211      0.090     -1.344      0.179      -0.298       0.056
Doors            -1.6166     40.006     -0.040      0.968     -80.093      76.859
Gears           594.3199    197.055      3.016      0.003     207.771     980.869
Quarterly_Tax     3.9491      1.310      3.015      0.003       1.379       6.519
Weight           16.9586      1.068     15.880      0.000      14.864      19.054
==============================================================================
"""

mod1_cc=smf.ols("Price~cc",data=ToyotaCorolla).fit()
mod1_cc.summary()
"""
 R-squared:                       0.016
 Adj. R-squared:                  0.015
 ==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   9027.5548    365.576     24.694      0.000    8310.435    9744.675
cc             1.0802      0.224      4.825      0.000       0.641       1.519
==============================================================================

"""
mod1_Doors=smf.ols("Price~Doors",data=ToyotaCorolla).fit()
mod1_Doors.summary()
"""
R-squared:                       0.034
 Adj. R-squared:                  0.034
 ==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   7885.0058    409.438     19.258      0.000    7081.843    8688.168
Doors        705.5586     98.795      7.142      0.000     511.761     899.356
==============================================================================
"""

mod1_Doors_cc=smf.ols("Price~Doors+cc",data=ToyotaCorolla).fit()
mod1_Doors_cc.summary()
"""
R-squared:                       0.047
Adj. R-squared:                  0.046
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   6509.4211    515.773     12.621      0.000    5497.670    7521.173
Doors        671.3973     98.501      6.816      0.000     478.176     864.619
cc             0.9597      0.221      4.340      0.000       0.526       1.393
==============================================================================
"""

rsq_Age_08_04 = smf.ols('Age_08_04~KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=ToyotaCorolla).fit().rsquared
vif_Age_08_04 = 1/(1-rsq_Age_08_04 )   
rsq_KM = smf.ols('KM~Age_08_04+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=ToyotaCorolla).fit().rsquared
vif_KM = 1/(1-rsq_KM )     
rsq_HP = smf.ols('HP~Age_08_04+cc+Doors+Gears+Quarterly_Tax+Weight',data=ToyotaCorolla).fit().rsquared  
vif_HP = 1/(1-rsq_HP )  
rsq_cc = smf.ols('cc~Age_08_04+HP+KM+Doors+Gears+Quarterly_Tax+Weight',data=ToyotaCorolla).fit().rsquared  
vif_cc = 1/(1-rsq_cc )  
rsq_Doors = smf.ols('Doors~Age_08_04+HP+KM+cc+Gears+Quarterly_Tax+Weight',data=ToyotaCorolla).fit().rsquared  
vif_Doors = 1/(1-rsq_Doors )  
rsq_Gears = smf.ols('Gears~Age_08_04+HP+KM+cc+Doors+Quarterly_Tax+Weight',data=ToyotaCorolla).fit().rsquared  
vif_Gears = 1/(1-rsq_Gears )  
rsq_Quarterly_Tax = smf.ols('Quarterly_Tax~Age_08_04+HP+KM+cc+Doors+Gears+Weight',data=ToyotaCorolla).fit().rsquared
vif_Quarterly_Tax = 1/(1-rsq_Quarterly_Tax )  
rsq_Weight = smf.ols('Weight~Age_08_04+HP+KM+cc+Doors+Gears+Quarterly_Tax',data=ToyotaCorolla).fit().rsquared
vif_Weight = 1/(1-rsq_Weight )

d1 = {'Variables':['Age_08_04','KM','HP','cc','Doors','Gears','Quarterly_Tax','Weight'],'VIF':[vif_Age_08_04,vif_KM ,vif_HP,vif_cc,vif_Doors,vif_Gears,vif_Quarterly_Tax,vif_Weight ]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame  


import statsmodels.api as sm
""" HERE AVPLOTS IS LIKE sm.graphics.plot_partregress_grid(ml_new)"""
# Added varible plot 
sm.graphics.plot_partregress_grid(mod1)
sm.graphics.influence_plot(mod1)

ToyotaCorolla_new=ToyotaCorolla.drop(ToyotaCorolla.index[80],axis=0)#cars_new=cars.drop(cars.index[76,70],axis=0)
mod2=smf.ols("Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight",data=ToyotaCorolla_new).fit()
mod2.summary()
"""
R-squared:                       0.869
Adj. R-squared:                  0.869
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept     -6284.7401   1382.748     -4.545      0.000   -8997.180   -3572.301
Age_08_04      -120.4550      2.562    -47.021      0.000    -125.480    -115.430
KM               -0.0178      0.001    -13.973      0.000      -0.020      -0.015
HP               39.3463      2.911     13.516      0.000      33.636      45.057
cc               -2.5242      0.307     -8.216      0.000      -3.127      -1.922
Doors           -27.2285     39.241     -0.694      0.488    -104.206      49.749
Gears           523.9416    192.865      2.717      0.007     145.612     902.271
Quarterly_Tax     9.0440      1.425      6.348      0.000       6.249      11.839
Weight           20.1655      1.116     18.076      0.000      17.977      22.354
==============================================================================
"""

mod3_withot_Doors=smf.ols("Price~Age_08_04+KM+HP+cc+Gears+Quarterly_Tax+Weight",data=ToyotaCorolla_new).fit()
mod3_withot_Doors.summary()
"""
R-squared:                       0.869
Adj. R-squared:                  0.869
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept     -6313.9396   1381.857     -4.569      0.000   -9024.628   -3603.251
Age_08_04      -120.4577      2.561    -47.031      0.000    -125.482    -115.433
KM               -0.0179      0.001    -14.029      0.000      -0.020      -0.015
HP               39.1593      2.898     13.512      0.000      33.474      44.844
cc               -2.5069      0.306     -8.188      0.000      -3.107      -1.906
Gears           549.7311    189.216      2.905      0.004     178.561     920.902
Quarterly_Tax     9.0759      1.424      6.374      0.000       6.283      11.869
Weight           19.9623      1.076     18.547      0.000      17.851      22.074
==============================================================================
"""

PRICE_PRED=mod3_withot_Doors.predict(ToyotaCorolla_new)


resid_errors=ToyotaCorolla_new.Price-PRICE_PRED
zero_mean_error=np.sum(resid_errors)

rmse = np.sqrt(np.mean(resid_errors*resid_errors))#1308.711773669594

# Observed values VS Fitted values
plt.scatter(ToyotaCorolla_new.Price,PRICE_PRED,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")

#CHECKING HOMOHETERSCEDASTICITY
plt.scatter(PRICE_PRED,mod3_withot_Doors.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")

# histogram
plt.hist(mod3_withot_Doors.resid_pearson) # Checking the standardized residuals are normally distributed

# QQ plot for residuals 
import pylab          
import scipy.stats as st

# Checking Residuals are normally distributed
st.probplot(mod3_withot_Doors.resid_pearson, dist="norm", plot=pylab)

### Splitting the data into train and test data 

from sklearn.model_selection import train_test_split
ToyotaCorolla_train,ToyotaCorollas_test  = train_test_split(ToyotaCorolla_new,test_size = 0.2) # 20% size

model_train = smf.ols("Price~Age_08_04+KM+HP+cc+Gears+Quarterly_Tax+Weight",data=ToyotaCorolla_train).fit()
# train_data prediction
train_pred = model_train.predict(ToyotaCorolla_train)

# train residual values 
train_resid  = train_pred - ToyotaCorolla_train.Price

# RMSE value for train data 
train_rmse = np.sqrt(np.mean(train_resid*train_resid)) # 1308.8248021256125

# prediction on test data set 
test_pred = model_train.predict(ToyotaCorollas_test)
# test residual values 
test_resid  = test_pred - ToyotaCorollas_test.Price

# RMSE value for test data 
test_rmse = np.sqrt(np.mean(test_resid*test_resid)) #  1317.295589795736
"""HERE ORIGINAL rmse = 1308.711773669594
train_rmse = 1308.8248021256125
test_rmse=1317.295589795736
THIS IS JUST RIGHT MODEL"""




