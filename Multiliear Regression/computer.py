# Multilinear Regression
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.preprocessing import OneHotEncoder
# loading the data
computer = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\multiliear regression\\Computer_Data.csv")
type(computer)
computer.columns

computer.info()
"""from sklearn.preprocessing import OneHotEncoder

onehotencoder=OneHotEncoder(categorical_features=['cd','multi','premium'])
df=onehotencoder.fit_transform(computer).toarray()"""

for col in computer.columns:
    print(col, ': ', len(computer[col].unique()), ' labels;')
pd.get_dummies(computer['multi','cd','premium'], drop_first=True)#[6259 rows x 11 columns]

computer.multi.value_counts().sort_values(ascending=False).head(20)
"""
no     5386
yes     873
Name: multi, dtype: int64
"""
computer.cd.value_counts().sort_values(ascending=False).head(20)
"""
no     3351
yes    2908
Name: cd, dtype: int64
"""
computer.premium.value_counts().sort_values(ascending=False).head(20)
"""
yes    5647
no      612
Name: premium, dtype: int64
"""

"""top_1=[x for x in computer.multi.value_counts().sort_values(ascending=False).head(1).index]"""

"""
for label in top_1:
    computer[label]=np.where(computer['cd']==label, 1,0)
computer[['cd']+top_1].head(10)
df=computer[['cd','no']].head(10)

"""
"""
    cd  no
0   no   1
1   no   1
2   no   1
3   no   1
4   no   1
5   no   1
6  yes   0
7   no   1
8   no   1
9   no   1
"""
computer.head(10)
"""FOR MULTI--------------------------"""
top_1_multi=[x for x in computer.multi.value_counts().sort_values(ascending=False).head(1).index]
def one_hot_top_x(df, variable, top_x_labels):
    for label in top_x_labels:
    #   df['multi'_'no']=np.where(computer['multi']=='no', 1,0)
        df[variable+'_'+label]=np.where(computer[variable]==label,1,0)
one_hot_top_x(computer, 'multi' , top_1_multi)


"""FOR CD--------------------------"""
top_1_cd=[x for x in computer.cd.value_counts().sort_values(ascending=False).head(1).index]

def one_hot_top_x(df, variable, top_x_labels):
    for label in top_x_labels:
    #   df['multi'_'no']=np.where(computer['multi']=='no', 1,0)
        df[variable+'_'+label]=np.where(computer[variable]==label,1,0)
one_hot_top_x(computer, 'cd' , top_1_cd)


"""FOR PREMIUM--------------------------"""
top_1_premium=[x for x in computer.premium.value_counts().sort_values(ascending=False).head(1).index]

def one_hot_top_x(df, variable, top_x_labels):
    for label in top_x_labels:
    #   df['multi'_'no']=np.where(computer['multi']=='no', 1,0)
        df[variable+'_'+label]=np.where(computer[variable]==label,1,0)
one_hot_top_x(computer, 'premium' , top_1_premium)

computer.drop(['premium','cd','multi','Unnamed: 0'],axis=1,inplace=True)
computer.corr()
computer.columns

mod1=smf.ols("price~speed+ hd+ ram+ screen+ ads+ trend+ multi_no+cd_no+ premium_yes",data=computer).fit()
mod1.summary()
"""
R-squared:                       0.776
Adj. R-squared:                  0.775
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept     473.2285     61.874      7.648      0.000     351.935     594.522
speed           9.3203      0.185     50.364      0.000       8.958       9.683
hd              0.7818      0.028     28.311      0.000       0.728       0.836
ram            48.2560      1.066     45.265      0.000      46.166      50.346
screen        123.0890      3.999     30.776      0.000     115.249     130.929
ads             0.6573      0.051     12.809      0.000       0.557       0.758
trend         -51.8496      0.629    -82.470      0.000     -53.082     -50.617
multi_no     -104.3238     11.413     -9.141      0.000    -126.697     -81.951
cd_no         -60.9167      9.516     -6.402      0.000     -79.571     -42.263
premium_yes  -509.2247     12.342    -41.259      0.000    -533.420    -485.030
==============================================================================
"""

rsq_speed = smf.ols('speed~hd+ram+screen+ads+trend+multi_no+cd_no+premium_yes',data=computer).fit().rsquared  
vif_speed = 1/(1-rsq_speed)
rsq_hd = smf.ols('hd~speed+ram+screen+ads+trend+multi_no+cd_no+premium_yes',data=computer).fit().rsquared  
vif_hd = 1/(1-rsq_hd)
rsq_ram = smf.ols('ram~hd+speed+screen+ads+trend+multi_no+cd_no+premium_yes',data=computer).fit().rsquared  
vif_ram = 1/(1-rsq_ram)
rsq_ads = smf.ols('ads~ram+hd+speed+screen+trend+multi_no+cd_no+premium_yes',data=computer).fit().rsquared  
vif_ads = 1/(1-rsq_ads)
rsq_screen = smf.ols('screen~ads+ram+hd+speed+trend+multi_no+cd_no+premium_yes',data=computer).fit().rsquared  
vif_screen = 1/(1-rsq_screen)
rsq_trend = smf.ols('trend~screen+ads+ram+hd+speed+multi_no+cd_no+premium_yes',data=computer).fit().rsquared  
vif_trend = 1/(1-rsq_trend)
rsq_multi_no = smf.ols('multi_no~trend+screen+ads+ram+hd+speed+cd_no+premium_yes',data=computer).fit().rsquared  
vif_multi_no = 1/(1-rsq_multi_no)
rsq_cd_no = smf.ols('cd_no~multi_no+trend+screen+ads+ram+hd+speed+premium_yes',data=computer).fit().rsquared  
vif_cd_no = 1/(1-rsq_cd_no)
rsq_premium_yes = smf.ols('premium_yes~cd_no+multi_no+trend+screen+ads+ram+hd+speed',data=computer).fit().rsquared  
vif_premium_yes = 1/(1-rsq_premium_yes)

d1={'variables':['speed', 'hd', 'ram', 'screen', 'ads', 'trend', 'multi_no', 'cd_no', 'premium_yes'],'VIF':[vif_speed ,vif_hd,vif_ram,vif_ads,vif_screen,vif_trend,vif_multi_no,vif_cd_no,vif_premium_yes]}
vif_frame=pd.DataFrame(d1)


import statsmodels.api as sm
""" HERE AVPLOTS IS LIKE sm.graphics.plot_partregress_grid(ml_new)"""
# Added varible plot 
sm.graphics.plot_partregress_grid(mod1)

sm.graphics.influence_plot(mod1)
computer_new=computer.drop(computer.index[19],axis=0)#cars_new=cars.drop(cars.index[76,70],axis=0)
computer_new=computer.drop(computer.index[24],axis=0)

mod2=smf.ols("price~speed+ hd+ ram+ screen+ ads+ trend+ multi_no+cd_no+ premium_yes",data=computer_new).fit()
mod2.summary()
"""
R-squared:                       0.776
Adj. R-squared:                  0.776
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept     468.1400     61.747      7.582      0.000     347.095     589.185
speed           9.3156      0.185     50.448      0.000       8.954       9.678
hd              0.7791      0.028     28.270      0.000       0.725       0.833
ram            48.3198      1.064     45.420      0.000      46.234      50.405
screen        123.2339      3.991     30.879      0.000     115.410     131.057
ads             0.6643      0.051     12.970      0.000       0.564       0.765
trend         -51.7341      0.628    -82.416      0.000     -52.965     -50.504
multi_no     -104.1628     11.388     -9.147      0.000    -126.487     -81.839
cd_no         -61.0387      9.495     -6.429      0.000     -79.652     -42.425
premium_yes  -509.1134     12.315    -41.339      0.000    -533.256    -484.971
==============================================================================
"""
mod3=smf.ols("np.log(price)~(speed+ hd+ ram+ screen+ ads+ trend+ multi_no+cd_no+ premium_yes)",data=computer_new).fit()
mod3.summary()
"""
R-squared:                       0.783
Adj. R-squared:                  0.783
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept       6.9304      0.027    256.791      0.000       6.878       6.983
speed           0.0042   8.07e-05     52.651      0.000       0.004       0.004
hd              0.0003    1.2e-05     28.189      0.000       0.000       0.000
ram             0.0209      0.000     44.901      0.000       0.020       0.022
screen          0.0543      0.002     31.108      0.000       0.051       0.058
ads             0.0003   2.24e-05     12.204      0.000       0.000       0.000
trend          -0.0236      0.000    -85.891      0.000      -0.024      -0.023
multi_no       -0.0473      0.005     -9.511      0.000      -0.057      -0.038
cd_no          -0.0495      0.004    -11.926      0.000      -0.058      -0.041
premium_yes    -0.2270      0.005    -42.179      0.000      -0.238      -0.216
==============================================================================
"""
computer_Price=mod3.predict(computer_new)
computer_Price_anti_log=np.exp(computer_Price)
computer_Price.corr(computer_new.price)

resid_errors=computer_new.price-computer_Price_anti_log
zero_mean_error=np.sum(resid_errors)

original_rmse = np.sqrt(np.mean(resid_errors*resid_errors))#272.4543235449484

######  Linearity #########
"""WHEN IT COMES TO FIRST LINEARITY THEN WE HAVE TO CHECK
Y AND X1,X2,X3-------- BEFORE BUILDING THE MODEL WE ARE CHECKING WITH SCATTER DIAGRAM
BUT AFTER BUILDING THE MODEL WE SHOULD CHECK FOR THE B0, B1,B2-------
HERE cars_new.MPG IS Y AND  MPG_PRED IS Y^ THAT IS B0, B1...."""
# Observed values VS Fitted values
plt.scatter(computer_new.price,computer_Price_anti_log,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")

#HERE CHECKING HOMESCEDASTICITY
plt.scatter(computer_Price_anti_log,mod3.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")

# histogram
plt.hist(mod3.resid_pearson)

# QQ plot for residuals 
import pylab          
import scipy.stats as st

# Checking Residuals are normally distributed
st.probplot(mod3.resid_pearson, dist="norm", plot=pylab)

from sklearn.model_selection import train_test_split
computer_train,computer_test  = train_test_split(computer_new,test_size = 0.2) # 20% size

model_train = smf.ols("np.log(price)~(speed+ hd+ ram+ screen+ ads+ trend+ multi_no+cd_no+ premium_yes)",data=computer_train).fit()

# train_data prediction
train_pred = model_train.predict(computer_train)

# train residual values 
train_resid  = train_pred - computer_train.price

# RMSE value for train data 
train_rmse = np.sqrt(np.mean(train_resid*train_resid)) # 2288.139523837121

# prediction on test data set 
test_pred = model_train.predict(computer_test)

# test residual values 
test_resid  = test_pred - computer_test.price

# RMSE value for test data 
test_rmse = np.sqrt(np.mean(test_resid*test_resid)) # 2279.411566978164

#original rmse is 3.88888

"""--------------------------NOT CLEAR YET-------------------"""






