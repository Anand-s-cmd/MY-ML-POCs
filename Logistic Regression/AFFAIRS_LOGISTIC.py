""" LOGISTIC BANK ASSIGNMENT USING ExtraTreeClassifier()"""

"""
Feature importance is an inbuilt class that comes with Tree Based Classifiers, 
we will be using Extra Tree Classifier for extracting the top 10 features for the dataset.
"""


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data=pd.read_csv(r"C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Logistic Regression\\affairs.csv")


data.shape
data.columns
data=data.drop('Unnamed: 0',axis=1)
data.tail(5)
"""
HERE AFFAIRS COLUMNS HAS 0,1 AND MORE THAN ONE VALUES SO WE HAVE TO MAKE IT O OR ONLY BY PUTTING CONDITION AS IF >0 THEN 1 ELSE 0
"""
"""for i in data.affairs:
    if i>0:
      i=1 
"""

data["affairs"] = np.where(data["affairs"] == 0, 0, 1)# BESTTHING IS WE CONVERTED 0 AS 0 AND MORE THAN 0 AS 1

""" NOW WE HAVE CHILDREN AND GENDER AGAIN YES AND NO WE HAVE CONVERT THEM INTO 0 AND 1 AGAIN"""
data.gender.value_counts()
"""
female    315
male      286--> so only male and female
"""
# NOW I AM GOING TO REPLACE THEIE ITSELF INSTEAD OF CREATING NEW COLUMNS
data["gender"] = np.where(data["gender"] == "female", 0, 1)

data.children.value_counts()
"""
yes    430
no     171
"""
# NOW I AM GOING TO REPLACE THEIE ITSELF INSTEAD OF CREATING NEW COLUMNS
data["children"] = np.where(data["children"] == "yes", 1, 0)

data.isnull().sum()
"""
affairs          0
gender           0
age              0
yearsmarried     0
children         0
religiousness    0
education        0
occupation       0
rating           0
"""

data.tail(5)
data.columns
x= data.iloc[:,1:9]  #independent columns
y = data.iloc[:,0]    #target column i.e price range
x.columns
y
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model=ExtraTreesClassifier()
model.fit(x,y)

feat_imp=pd.Series(model.feature_importances_,index=x.columns)
feat_imp.nlargest(10).plot(kind='barh')

new_feat=pd.DataFrame(feat_imp.nlargest(8))
new_feat.head(8)#top 10 features
"""

education      0.187553
age            0.165747
rating         0.163233
religiousness  0.159215
occupation     0.146838
yearsmarried   0.123118
gender         0.029957
children       0.024339
"""


""" BUT MY DOUBT IS WHEN I USE UNICARIATE METHOD THERE SCORES WERE LITTLE MORE THAN THESE
AND ALSO GOT SOME DIFFERENT FEATURES"""
data.columns
new_data=data[['education','age','rating','religiousness','occupation','yearsmarried','gender','children']]

new_data.isnull().sum()
"""
education        0
age              0
rating           0
religiousness    0
occupation       0
yearsmarried     0
gender           0
children         0
"""

data.shape
new_data['y']=y
new_data.shape
new_data.columns
"""
(['education', 'age', 'rating', 'religiousness', 'occupation',
       'yearsmarried', 'gender', 'children', 'y'],
      dtype='object')
"""
from sklearn.model_selection import train_test_split 
train,test=train_test_split(new_data,test_size=0.3) 

import statsmodels.formula.api as smf
logit_model = smf.logit('y~education+age+rating+religiousness+occupation+yearsmarried+gender+children',data = train).fit()
logit_model.summary()
"""
LLR p-value:                     0.000
Log-Likelihood:                -200.07
LL-Null:                       -225.77
LLR p-value:                 2.201e-08

=================================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept         2.4451      1.091      2.241      0.025       0.307       4.583
education        -0.0456      0.062     -0.731      0.465      -0.168       0.077
age              -0.0558      0.023     -2.443      0.015      -0.101      -0.011
rating           -0.4970      0.113     -4.411      0.000      -0.718      -0.276
religiousness    -0.2521      0.112     -2.254      0.024      -0.471      -0.033
occupation        0.0046      0.089      0.052      0.958      -0.169       0.178
yearsmarried      0.1264      0.040      3.167      0.002       0.048       0.205
gender            0.7711      0.308      2.500      0.012       0.167       1.376
children          0.0536      0.373      0.144      0.886      -0.677       0.784
=================================================================================

here childern education  and occupation
"""

mod2=smf.logit('y~np.log(education)+age+rating+religiousness+np.log(occupation)+yearsmarried+gender+np.log(children)',data = train).fit()
mod2.summary()

"""
=================================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept        -1.7255      0.289     -5.968      0.000      -2.292      -1.159
duration          0.0040   7.32e-05     54.500      0.000       0.004       0.004
balance        2.769e-05   5.52e-06      5.020      0.000    1.69e-05    3.85e-05
age              -0.0024      0.002     -1.285      0.199      -0.006       0.001
campaign         -0.1200      0.012     -9.995      0.000      -0.144      -0.096
poutsuccess       2.1032      0.110     19.056      0.000       1.887       2.320
np.log(pdays)    -0.0612      0.052     -1.178      0.239      -0.163       0.041
previous          0.0313      0.011      2.878      0.004       0.010       0.053
housing          -1.0570      0.044    -23.901      0.000      -1.144      -0.970
poutfailure      -0.2782      0.102     -2.715      0.007      -0.479      -0.077
poutunknown      -1.1411      0.280     -4.077      0.000      -1.690      -0.592
=================================================================================

STILL PDAYS IS NOT SIGNIFICANT LETS APPLY ON AGE AS WELL
"""


mod3=smf.logit('y~duration+balance+np.log(age)+campaign+poutsuccess+np.log(pdays)+previous+housing+poutfailure+poutunknown',data = train).fit()
mod3.summary()
"""
=================================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept        -0.6375      0.399     -1.598      0.110      -1.419       0.144
duration          0.0040   7.33e-05     54.499      0.000       0.004       0.004
balance         2.92e-05   5.51e-06      5.304      0.000    1.84e-05       4e-05
np.log(age)      -0.3230      0.078     -4.151      0.000      -0.475      -0.170
campaign         -0.1190      0.012     -9.923      0.000      -0.142      -0.095
poutsuccess       2.1126      0.110     19.131      0.000       1.896       2.329
np.log(pdays)    -0.0613      0.052     -1.179      0.238      -0.163       0.041
previous          0.0312      0.011      2.872      0.004       0.010       0.053
housing          -1.0748      0.044    -24.388      0.000      -1.161      -0.988
poutfailure      -0.2700      0.102     -2.635      0.008      -0.471      -0.069
poutunknown      -1.1364      0.280     -4.057      0.000      -1.685      -0.587
=================================================================================
STILL, PDAYS IS NOT SIGNIFICANT SO LETS REMOVE TRHAT VARIABLE AND CHECK
"""

mod4=smf.logit('y~duration+balance+np.log(age)+campaign+poutsuccess++previous+housing+poutfailure+poutunknown',data = train).fit()
mod4.summary()
"""
===============================================================================
                  coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept      -0.9452      0.303     -3.124      0.002      -1.538      -0.352
duration        0.0040   7.33e-05     54.494      0.000       0.004       0.004
balance      2.925e-05    5.5e-06      5.314      0.000    1.85e-05       4e-05
np.log(age)    -0.3230      0.078     -4.151      0.000      -0.475      -0.170
campaign       -0.1192      0.012     -9.939      0.000      -0.143      -0.096
poutsuccess     2.1187      0.110     19.202      0.000       1.902       2.335
previous        0.0315      0.011      2.901      0.004       0.010       0.053
housing        -1.0808      0.044    -24.678      0.000      -1.167      -0.995
poutfailure    -0.2835      0.102     -2.787      0.005      -0.483      -0.084
poutunknown    -0.8258      0.098     -8.435      0.000      -1.018      -0.634
===============================================================================

"""


y_pred = mod4.predict(train)
train["pred_prob"] = y_pred
train.head(2)

train["Att_val"]=0

train.loc[y_pred>=0.5,"Att_val"] = 1
train.head(10)
train.columns

confusion_matrix = pd.crosstab(train.Att_val,train['y'])
"""
y            0     1
Att_val             
0        27287  2563
1          645  1152
"""
acuracy=(27287+1152)/31647#0.8986317818434607

error=1-acuracy# 0.10136821815653929

from sklearn import metrics
# fpr => false positive rate
# tpr => true positive rate
fpr, tpr, threshold = metrics.roc_curve(train.y, y_pred)
plt.plot(fpr,tpr);plt.xlabel("False Positive");plt.ylabel("True Positive")
""" WE GOT BEST CURVE"""
roc_auc = metrics.auc(fpr, tpr) # area under ROC curve 
roc_auc#0.874319853695834


test_pred = mod4.predict(test)
test["pred_prob"] = test_pred
test["Att_val"]=0

test.shape
test.head()

test.loc[test_pred>=0.5,"Att_val"] = 1

confusion_matrix = pd.crosstab(test.Att_val,test['y'])
"""
y            0     1
Att_val             
0        11678  1060
1          312   514
"""
acuracy=(11678+514)/13564#  0.898849896785609

error=1-acuracy#0.101150103214391

from sklearn import metrics
# fpr => false positive rate
# tpr => true positive rate
fpr, tpr, threshold = metrics.roc_curve(test.y, test_pred)
plt.plot(fpr,tpr);plt.xlabel("False Positive");plt.ylabel("True Positive")
""" WE GOT BEST CURVE again for test as well"""
roc_auc_test = metrics.auc(fpr, tpr) # area under ROC curve 
roc_auc_test#0.8801552119354015

"""
train and test
roc_auc=     0.874319853695834
roc_auc_test=0.8801552119354015

accuracy_train=0.8986317818434607

accuracy_test=0.898849896785609


"""