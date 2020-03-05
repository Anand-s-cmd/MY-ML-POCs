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
computer.multi.dtype

computer.info()

for col in computer.columns:
    print(col, ': ', len(computer[col].unique()), ' labels;')
    
"""Q*** MAKE A NOTE THAT
IF WE GIVE --> len(computer[col].unique() WE GET YES OR NO AND LEN OF THAT THAT IS 2
IF WE GIVE -->computer.multi.value_counts() WE WILL GET HOW MANY YES ARE THER AND NO AS WELL LIKE
no     5386
yes     873
"""
# EVEN FOR 2 CAT TYPES WE WILL GO WITH ONE HOT CODING NOW
    
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

computer.columns
computer.drop(['multi','cd','premium','Unnamed: 0'],axis=1,inplace=True)


from sklearn.model_selection import train_test_split

train,test=train_test_split(computer,test_size=0.2)

train.corr()
import seaborn as sns
sns.pairplot(train)

#lets bui dthe model first

mod1=smf.ols("price~speed+ hd+ ram+ screen+ ads+ trend+ multi_no+cd_no+ premium_yes",data=train).fit()
mod1.summary()
"""
All are significant variable all are less than 0.5
R-squared:                       0.774
Adj. R-squared:                  0.774
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
"""
  variables       VIF
0        speed  1.265364
1           hd  4.207395
2          ram  2.974628
3       screen  1.217218
4          ads  1.081644
5        trend  2.022790
6     multi_no  1.290568
7        cd_no  1.859370
8  premium_yes  1.109388
again all are less than 10 then what we can do is check for outliers as well
"""
import statsmodels.api as sm
sm.graphics.influence_plot(mod1)

train.shape
sm.graphics.plot_partregress_grid(mod1)

#lets go to log transformatin
mod2=smf.ols("np.log(price)~speed+ hd+ ram+ screen+ ads+ trend+ multi_no+cd_no+ premium_yes",data=train).fit()
mod2.summary()
"""
R-squared:                       0.783
Adj. R-squared:                  0.783
All are significant
"""
mod3=smf.ols("price~speed+ np.log(hd)+ ram+ np.log(screen)+ ads+ trend+ multi_no+cd_no+ premium_yes",data=train).fit()
mod3.summary()
"""
R-squared:                       0.794
Adj. R-squared:                  0.794
all are significant
"""
mod4=smf.ols("price~np.log(speed)+ np.log(hd)+ ram+ np.log(screen)+ ads+ trend+ multi_no+cd_no+ premium_yes",data=train).fit()
mod4.summary()
"""
R-squared:                       0.801
Adj. R-squared:                  0.800
all are significant
"""

train_mod_pred=mod4.predict(train)
train_errors=train.price-train_mod_pred
train_rmse = np.sqrt(np.mean(train_errors*train_errors)) # 259.9402717802632

#check corr with actual and predicted
train_mod_pred.corr(train.price)  #0.8947078788268926

"""MODEL ASSUMPTIONS"""
#LINEARITY THAT IS 
"""WHEN IT COMES TO FIRST LINEARITY THEN WE HAVE TO CHECK
Y AND X1,X2,X3-------- BEFORE BUILDING THE MODEL WE ARE CHECKING WITH SCATTER DIAGRAM
BUT AFTER BUILDING THE MODEL WE SHOULD CHECK FOR THE B0, B1,B2-------
HERE cars_new.MPG IS Y AND  MPG_PRED IS Y^ THAT IS B0, B1...."""
# Observed values VS Fitted values
plt.scatter(train.price,train_mod_pred,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")

#HERE CHECKING HOMESCEDASTICITY
plt.scatter(train_mod_pred,mod4.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")
#perfect homoscadasticity

# histogram
plt.hist(mod4.resid_pearson)#perfect normality as +ve skewed

# QQ plot for residuals 
import pylab          
import scipy.stats as st

# Checking Residuals are normally distributed
st.probplot(mod4.resid_pearson, dist="norm", plot=pylab)#perfect

"""NOW TEST FOR TEST DATA"""
test_pred=mod4.predict(test)
test_errors=test.price-test_pred
test_rmse = np.sqrt(np.mean(test_errors*test_errors)) # 254.05281005602123

#check corr for actual and predicted in test data
test_pred.corr(test.price)# 0.8974977324550488


"""MODEL ASSUMPTIONS"""
#LINEARITY THAT IS 
"""WHEN IT COMES TO FIRST LINEARITY THEN WE HAVE TO CHECK
Y AND X1,X2,X3-------- BEFORE BUILDING THE MODEL WE ARE CHECKING WITH SCATTER DIAGRAM
BUT AFTER BUILDING THE MODEL WE SHOULD CHECK FOR THE B0, B1,B2-------
HERE cars_new.MPG IS Y AND  MPG_PRED IS Y^ THAT IS B0, B1...."""
# Observed values VS Fitted values
plt.scatter(test.price,test_pred,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")

#HERE CHECKING HOMESCEDASTICITY--> gave error as x and y must be same rest all worked fine
plt.scatter(test_pred,mod4.resid_pearson,c="r");plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")
#perfect homoscadasticity

# histogram
plt.hist(mod4.resid_pearson)#perfect normality as +ve skewed

# QQ plot for residuals 
import pylab          
import scipy.stats as st

# Checking Residuals are normally distributed
st.probplot(mod4.resid_pearson, dist="norm", plot=pylab)#perfect


""" train accuracy=0.8947078788268926
    test accuracy =0.8974977324550488
    
    train_rmse = 259.9402717802632
    test_rmse =  254.05281005602123
"""

"""
POINTS TO BE NOTED IN LINEAR AND MULTIPLE LINEAR REGRESSION ARE

CHECK MODEL FIRST
CHECK VIF AND AVPLOTS
THEN OUTLIERS ANY
THEN CHECK LOG TRANSFOMATION EVEN IF MODEL IS NOT GOOD
R2 VALUE 
ADJ R2 VALUE
 
RMSE

THEN MODEL ASSUMPTIONS MUST
LINEARITY
ASSUMTIONS ABOUT ERROS
ASSUMTIONS ABOUT OBSERVATIONS
"""