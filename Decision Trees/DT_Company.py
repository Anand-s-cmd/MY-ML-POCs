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
train['Sales_categories']
from sklearn.tree import  DecisionTreeClassifier
help(DecisionTreeClassifier)

model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(train[predictors],train[target])

train_preds=model.predict(train[predictors])
preds = model.predict(test[predictors])
pd.Series(preds).value_counts()

np.mean(train.Sales_categories == model.predict(train[predictors]))# 1.0

# Accuracy = Test
np.mean(preds==test.Sales_categories) # 0.8

""" ABSOLUTELY ITS OVERFITTING MODEL"""
