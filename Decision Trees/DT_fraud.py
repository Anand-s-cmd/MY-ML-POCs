import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\DECISION TREE\\assignments\\Fraud_check.csv")
data=data.rename(columns={"Marital.Status": "Marital_Status","Taxable.Income": "Taxable_Income","City.Population": "City_Population", "Work.Experience": "Work_Experience"})
data.head(20)
data.columns
urban2=pd.get_dummies(data['Urban'],drop_first=True)
data=pd.concat([data,urban2],axis=1)
data=data.drop('Urban',axis=1)# REOVING COLUMNS


Marital_Status2=pd.get_dummies(data['Marital_Status'],drop_first=True)
data=pd.concat([data,Marital_Status2],axis=1)
data=data.drop('Marital_Status',axis=1)# REOVING COLUMNS

Undergrad2=pd.get_dummies(data['Undergrad'],drop_first=True)
data=pd.concat([data,Undergrad2],axis=1)
data=data.drop('Undergrad',axis=1)# REOVING COLUMNS

data['TARGET_Taxable_Income']=data['Taxable_Income']
data=data.drop('Taxable_Income',axis=1)
data.TARGET_Taxable_Income.value_counts()


data.shape


bins=[0,30000,100000]
labels=['risky','good']

data['TARGET_Taxable_Income_bin']=  pd.cut(data['TARGET_Taxable_Income'],bins,labels)
print(pd.value_counts(data['TARGET_Taxable_Income_bin'],sort=False))
data['categories']= pd.cut(data['TARGET_Taxable_Income'],bins,labels=labels)

data['categories'].value_counts()
data.shape
data=data.drop('TARGET_Taxable_Income',axis=1)# REOVING COLUMNS
data=data.drop('TARGET_Taxable_Income_bin',axis=1)# REOVING COLUMNS

colnames = list(data.columns)
predictors = colnames[0:6]
target = colnames[6:7]

# creating a csv file 
data.to_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\DECISION TREE\\assignments\\data_fraud.csv",encoding="utf-8")


data.shape

from sklearn.model_selection import train_test_split
train,test = train_test_split(data,test_size = 0.2)

from sklearn.tree import  DecisionTreeClassifier
help(DecisionTreeClassifier)

model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(train[predictors],train[target])

train_preds=model.predict(train[predictors])
preds = model.predict(test[predictors])
pd.Series(preds).value_counts()

pd.crosstab(train[target],train_preds)
"""HERE I AM GETTING ERROR AS"""
"""Shape of passed values is (2, 1), indices imply (2, 480)"""
pd.crosstab(test[target],preds)

# Accuracy = train
np.mean(train.categories == model.predict(train[predictors]))#1

# Accuracy = Test
np.mean(preds==test.categories) # 0.6083333333333333
""" ABSOLUTELY ITS OVERFITTING MODEL"""
