import pandas as pd 
import numpy as np 
import seaborn as sns

train_sal = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\SVM\\SalaryData_Train.csv")
train_sal.head()
train_sal.describe()
train_sal.columns
train_sal.shape



Salary1=pd.get_dummies(train_sal['Salary'],drop_first=True)
Salary1.columns
train_sal=pd.concat([train_sal,Salary1],axis=1)
train_sal=train_sal.drop('Salary',axis=1)
train_sal.columns
"""  ['age', 'workclass', 'education', 'educationno', 'maritalstatus',
       'occupation', 'relationship', 'race', 'sex', 'capitalgain',
       'capitalloss', 'hoursperweek', 'native', ' >50K' """
train_sal=train_sal.rename(columns={" >50K": "salary"})
train_sal.tail()


workclass1=pd.get_dummies(train_sal['workclass'],drop_first=True)
workclass1.columns
train_sal=pd.concat([train_sal,workclass1],axis=1)
train_sal=train_sal.drop('workclass',axis=1)

train_sal1=pd.get_dummies(train_sal['education'],drop_first=True)
train_sal1.columns
train_sal=pd.concat([train_sal,train_sal1],axis=1)
train_sal=train_sal.drop('education',axis=1)

train_sal1=pd.get_dummies(train_sal['maritalstatus'],drop_first=True)
train_sal1.columns
train_sal=pd.concat([train_sal,train_sal1],axis=1)
train_sal=train_sal.drop('maritalstatus',axis=1)

train_sal1=pd.get_dummies(train_sal['occupation'],drop_first=True)
train_sal1.columns
train_sal=pd.concat([train_sal,train_sal1],axis=1)
train_sal=train_sal.drop('occupation',axis=1)

train_sal1=pd.get_dummies(train_sal['relationship'],drop_first=True)
train_sal1.columns
train_sal=pd.concat([train_sal,train_sal1],axis=1)
train_sal=train_sal.drop('relationship',axis=1)

train_sal1=pd.get_dummies(train_sal['race'],drop_first=True)
train_sal1.columns
train_sal=pd.concat([train_sal,train_sal1],axis=1)
train_sal=train_sal.drop('race',axis=1)

train_sal1=pd.get_dummies(train_sal['sex'],drop_first=True)
train_sal1.columns
train_sal=pd.concat([train_sal,train_sal1],axis=1)
train_sal=train_sal.drop('sex',axis=1)

train_sal1=pd.get_dummies(train_sal['native'],drop_first=True)
train_sal1.columns
train_sal=pd.concat([train_sal,train_sal1],axis=1)
train_sal=train_sal.drop('native',axis=1)


train_sal['target_salary']=train_sal['salary']
train_sal.drop('salary',axis=1,inplace=True)
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
train,test = train_test_split(train_sal,test_size = 0.3)
test.head()
train_sal.shape#(30161, 90)
train_sal.columns

x=train_sal.iloc[:,0:89]
x
y=train_sal.iloc[:,-1]
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model=ExtraTreesClassifier()
model.fit(x,y)

feat_imp=pd.Series(model.feature_importances_,index=x.columns)
feat_imp.nlargest(10).plot(kind='barh')

new_feat=pd.DataFrame(feat_imp.nlargest(10))
new_feat.head(10)#top 10 features

new_train_sal=train_sal[['hoursperweek','age','capitalgain',' Farming-fishing',' Unmarried',' Male',' Married-spouse-absent',' Machine-op-inspct',' Married-civ-spouse',' 7th-8th']]

train_sal.shape#(30161, 95)
new_train_sal['y']=y
new_train_sal.shape#(30161, 10)
new_train_sal.columns

train_X = new_train_sal.iloc[:,0:10]
train_X.columns
train_y = new_train_sal.iloc[:,-1]
#test_X  = test.iloc[:,0:45]
#test_y  = test.iloc[:,-1]

model_linear = SVC(kernel = "linear")
model_linear.fit(train_X,train_y)
pred_train = model_linear.predict(train_X)

train_acuracy=np.mean(pred_train==train_y)
np.mean(pred_test_linear==test_y) # Accuracy = 1.0


# Kernel = poly
model_poly = SVC(kernel = "poly")
model_poly.fit(train_X,train_y)
pred_test_poly = model_poly.predict(test_X)

np.mean(pred_test_poly==test_y) # Accuracy = 1.0

# kernel = rbf
model_rbf = SVC(kernel = "rbf")
model_rbf.fit(train_X,train_y)
pred_test_rbf = model_rbf.predict(test_X)

np.mean(pred_test_rbf==test_y) # Accuracy =  0.75



