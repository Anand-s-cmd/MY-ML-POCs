import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\DECISION TREE\\assignments\\Company_Data.csv")

data.head(20)
data.columns

ShelveLoc2=pd.get_dummies(data['ShelveLoc'],drop_first=True)
data=pd.concat([data,ShelveLoc2],axis=1)
data=data.drop('ShelveLoc',axis=1)# REOVING COLUMNS

urban2=pd.get_dummies(data['Urban'],drop_first=True)
data=pd.concat([data,urban2],axis=1)
data=data.drop('Urban',axis=1)# REOVING COLUMNS

US2=pd.get_dummies(data['US'],drop_first=True)
data=pd.concat([data,US2],axis=1)
data=data.drop('US',axis=1)# REOVING COLUMNS

bins=[0,10,20]
labels=['low','high']

data['Sales_bin']=  pd.cut(data['Sales'],bins,labels)
print(pd.value_counts(data['Sales_bin'],sort=False))
data['Sales_categories']= pd.cut(data['Sales'],bins,labels=labels)

data['Sales_categories'].value_counts()
data.shape
data=data.drop('Sales',axis=1)# REOVING COLUMNS
data=data.drop('Sales_bin',axis=1)# REOVING COLUMNS

data.columns
data.shape

colnames = list(data.columns)
predictors = colnames[0:11]
target = colnames[11:12]
"there is blank row in last variable thatv is Sales_categories so lets fill that in mode becuse of that last while predicting got error"
data.isnull().sum()
"""
CompPrice           0
Income              0
Advertising         0
Population          0
Price               0
Age                 0

Education           0
Good                0
Medium              0
Yes                 0
Yes                 0
Sales_categories    1
"""
data['Sales_categories']=data['Sales_categories'].fillna(data['Sales_categories'].mode()[0])
""" NOW CLEARED Sales_categories    0"""
data.to_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\DECISION TREE\\assignments\\COMAPNY_NEW_DATA.csv",encoding="utf-8")

from sklearn.model_selection import train_test_split
train,test = train_test_split(data,test_size = 0.2)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=3,oob_score=True,n_estimators=15,criterion="entropy")

rf.fit(train[predictors],train[target])

rf.estimators_ # 
rf.classes_ # class labels (output)
rf.n_classes_ # Number of levels in class labels 
rf.n_features_  # Number of input features in model 8 here.

rf.n_outputs_ # Number of outputs when fit performed

rf.oob_score_ #0.821875

train['rf_pred'] = rf.predict(train[predictors])


from sklearn.metrics import confusion_matrix
confusion_matrix(train['Sales_categories'],train['rf_pred']) # Confusion matrix

#pd.crosstab(train['Sales_categories'],train['rf_pred'])

print("Accuracy",(56+262)/(2+0+262+56)*100)#Accuracy 99.375

#check for test data now
test['rf_pred'] = rf.predict(test[predictors])
from sklearn.metrics import confusion_matrix
confusion_matrix(test['Sales_categories'],test['rf_pred']) # Confusion matrix

print("Accuracy",(15+59)/(15+59+5+1)*100)#Accuracy 92.5
