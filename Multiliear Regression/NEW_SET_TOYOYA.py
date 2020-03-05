# Multilinear Regression
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# loading the data
ToyotaCorolla = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\multiliear regression\\NEW_SET\\ToyotaCorolla.csv", usecols = ["Price","Age_08_04","KM","HP","cc","Doors","Gears","Quarterly_Tax","Weight"])
type(ToyotaCorolla)
from sklearn.model_selection import train_test_split
train,test=train_test_split(ToyotaCorolla,test_size = 0.2) # 20% size

ToyotaCorolla.shape#(1436, 9)
train.shape# (1148, 9)
test.shape#(288, 9)

train.corr()
"""
                  Price  Age_08_04    ...     Quarterly_Tax    Weight
Price          1.000000  -0.881782    ...          0.236949  0.611423
Age_08_04     -0.881782   1.000000    ...         -0.207436 -0.489002
KM            -0.572575   0.522583    ...          0.259310 -0.043893
HP             0.318609  -0.161226    ...         -0.297480  0.100811
cc             0.126712  -0.096390    ...          0.286016  0.327968
Doors          0.170837  -0.139202    ...          0.096252  0.278509
Gears          0.081509  -0.017376    ...         -0.007399  0.042495
Quarterly_Tax  0.236949  -0.207436    ...          1.000000  0.639755
Weight         0.611423  -0.489002    ...          0.639755  1.000000
"""
train_mod1=smf.ols("Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight",data=train).fit()

train_mod1.summary()
"""
R-squared:                       0.864
Adj. R-squared:                  0.863
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

#HERE CC AND DORRS ARE NOT SIGNIFICANT SO WE HAVE TO REMOVE ANY ONE OF THEM
#SO FIRST CHECK COLINERUTY WITH THEM WITH TARGET VARIABLE

mod1_CC=smf.ols("Price~cc",data=train).fit()
mod1_CC.summary()# p value is ok

mod1_DOORS=smf.ols("Price~Doors",data=train).fit()
mod1_DOORS.summary()# p value is ok

mod1_CC_DOORS=smf.ols("Price~Doors+cc",data=train).fit()
mod1_CC_DOORS.summary()# p value is ok

#go to avplot because even both CC and DoORS are significant 

import statsmodel.api as sm
sm.graphics.plot_partregress_grid(mod1)#---> avplots it is

sm.graphics.influence_plot(mod1)
new_train=train.drop(train.index[80],axis=0)
train.shape#(1148, 9)
new_train.shape# (1147, 9)
new_train_mod=smf.ols("Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight",data=new_train).fit()
new_train_mod.summary()
""" STILL DOORS AND CC ARE NOT SIGNIFICANT"""

""" q*** EVEN AFTER REMOVING OUTLIUER C AND DOOR DOES NOT BECOME SIGNIFICANT 
SO LETS KEEP THE SAME OLD DATA MEANS BEFORE REMOVAL OF OUTLIER THAT DATA AND CHECK VIF VALUES"""

rsq_Age_08_04 = smf.ols('Age_08_04~KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=train).fit().rsquared
vif_Age_08_04 = 1/(1-rsq_Age_08_04 )   
rsq_KM = smf.ols('KM~Age_08_04+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=train).fit().rsquared
vif_KM = 1/(1-rsq_KM )     
rsq_HP = smf.ols('HP~Age_08_04+cc+Doors+Gears+Quarterly_Tax+Weight',data=train).fit().rsquared  
vif_HP = 1/(1-rsq_HP )  
rsq_cc = smf.ols('cc~Age_08_04+HP+KM+Doors+Gears+Quarterly_Tax+Weight',data=train).fit().rsquared  
vif_cc = 1/(1-rsq_cc )  
rsq_Doors = smf.ols('Doors~Age_08_04+HP+KM+cc+Gears+Quarterly_Tax+Weight',data=train).fit().rsquared  
vif_Doors = 1/(1-rsq_Doors )  
rsq_Gears = smf.ols('Gears~Age_08_04+HP+KM+cc+Doors+Quarterly_Tax+Weight',data=train).fit().rsquared  
vif_Gears = 1/(1-rsq_Gears )  
rsq_Quarterly_Tax = smf.ols('Quarterly_Tax~Age_08_04+HP+KM+cc+Doors+Gears+Weight',data=train).fit().rsquared
vif_Quarterly_Tax = 1/(1-rsq_Quarterly_Tax )  
rsq_Weight = smf.ols('Weight~Age_08_04+HP+KM+cc+Doors+Gears+Quarterly_Tax',data=train).fit().rsquared
vif_Weight = 1/(1-rsq_Weight )

d1 = {'Variables':['Age_08_04','KM','HP','cc','Doors','Gears','Quarterly_Tax','Weight'],'VIF':[vif_Age_08_04,vif_KM ,vif_HP,vif_cc,vif_Doors,vif_Gears,vif_Quarterly_Tax,vif_Weight ]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame 
"""
HERE ALL ARE LESS THAN 10 THEN WHAT TO DO?????????????
       Variables       VIF
0      Age_08_04  1.978975
1             KM  1.765303
2             HP  1.412163
3             cc  1.147246
4          Doors  1.144156
5          Gears  1.122545
6  Quarterly_Tax  2.411400
7         Weight  2.688538
"""

#SO REMOVE THE DOOR AND CCAND CHECK THE MODEL

train_mod1_no_door=smf.ols("Price~Age_08_04+KM+HP+cc+Gears+Quarterly_Tax+Weight",data=train).fit()
train_mod1_no_door.summary()


new_train=train.drop(train.index[80],axis=0)
train_mod1_no_door2=smf.ols("Price~Age_08_04+KM+HP+cc+Gears+Quarterly_Tax+Weight",data=new_train).fit()
train_mod1_no_door2.summary()

train_mod1_no_cc=smf.ols("Price~Age_08_04+KM+HP+Gears+Quarterly_Tax+Weight",data=new_train).fit()
train_mod1_no_cc.summary()


"""
R-squared:                       0.875
Adj. R-squared:                  0.874
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept     -7391.7501   1631.888     -4.530      0.000   -1.06e+04   -4189.909
Age_08_04      -120.5939      2.884    -41.813      0.000    -126.253    -114.935
KM               -0.0206      0.001    -14.779      0.000      -0.023      -0.018
HP               31.2888      3.022     10.353      0.000      25.359      37.218
Gears           515.9559    234.421      2.201      0.028      56.010     975.902
Quarterly_Tax     2.6733      1.444      1.851      0.064      -0.161       5.507
Weight           18.8934      1.160     16.288      0.000      16.618      21.169
==============================================================================
"""
train_mod_pred=train_mod1_no_cc.predict(new_train)
residual_errors=train_mod_pred-new_train.Price

plt.hist(residual_errors)
#check the correlation between actual and predicted

train_mod_pred.corr(new_train.Price)#0.9353454555371689
zero_mean=np.sum(residual_errors)#3.4722688724286854e-07
rmse_value=np.sqrt(np.mean(residual_errors*residual_errors))#1317.6460418224922

test_mod_pred=train_mod1_no_cc.predict(test)
residual_errors_test=test_mod_pred-test.Price
zero_mean_test=np.sum(residual_errors_test)#-20053.147368076156
rmse_value_test=np.sqrt(np.mean(residual_errors_test*residual_errors_test))#1436.8148560957716



























