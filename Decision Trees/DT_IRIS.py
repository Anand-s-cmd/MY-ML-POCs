import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/EXCELR/NOTES WRITTEN/DECISION TREE/iris.csv")
data.head()
data['Species'].unique()
data.Species.value_counts()
colnames = list(data.columns)
predictors = colnames[:4]
target = colnames[4]

# Splitting data into training and testing data set

import numpy as np

# np.random.uniform(start,stop,size) will generate array of real numbers with size = size
data['is_train'] = np.random.uniform(0, 1, len(data))<= 0.75
data['is_train']
train,test = data[data['is_train'] == True],data[data['is_train']==False]

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
pd.crosstab(test[target],preds)

# Accuracy = train
np.mean(train.Species == model.predict(train[predictors]))

# Accuracy = Test
np.mean(preds==test.Species) # 1