import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/EXCELR/NOTES WRITTEN/DECISION TREE/iris.csv")
data.head()
data['Species'].unique()
data.Species.value_counts()
colnames = list(data.columns)
predictors = colnames[:4]
target = colnames[4]


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
confusion_matrix(train['Species'],train['rf_pred']) # Confusion matrix

#pd.crosstab(train['Sales_categories'],train['rf_pred'])
np.mean(train.Species == rf.predict(train[predictors]))#1.0
train.shape#(120, 6)
print("Accuracy",(40+40+40)/(120)*100)#Accuracy  100.0

#check for test data now
test['rf_pred'] = rf.predict(test[predictors])
from sklearn.metrics import confusion_matrix
confusion_matrix(test['Species'],test['rf_pred']) # Confusion matrix
np.mean(test.Species == rf.predict(test[predictors]))#0.9333333333333333
test.shape#(30, 6)

print("Accuracy",(10+10+8)/(30)*100)#Accuracy 93.33333333333333

""" good model"""