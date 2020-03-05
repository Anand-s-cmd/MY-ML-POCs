import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


start_ups = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Neural Networks\\50_Startups.csv")
start_ups.columns
start_ups=start_ups.rename(columns={"R&D Spend": "RD_spend", "Marketing Spend": "Marketing_Spend"})

start_ups.isnull().sum()

plt.hist(Y)
start_ups.Profit.value_counts()

start_ups1=pd.get_dummies(start_ups['State'],drop_first=True)
# here 2 cols created by dropping third couln that is California
start_ups1.columns#Index(['Florida', 'New York'], dtype='object')

start_ups=pd.concat([start_ups,start_ups1],axis=1)
start_ups.columns
start_ups=start_ups.rename(columns={"New York": "New_York"})



""" Index(['RD_spend', 'Administration', 'Marketing_Spend', 'State', 'Profit',
       'Florida', 'New York'],
      dtype='object')"""
#so now drp State column since we have created 2 more column out of 3 states
start_ups.columns
start_ups.head()
start_ups=start_ups.drop('State',axis=1)


X = start_ups.drop(["Profit"],axis=1)
Y = start_ups["Profit"]




from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(30,30))

mlp.fit(X_train,y_train)
prediction_train=mlp.predict(X_train)
prediction_test = mlp.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,prediction_test))
np.mean(y_train==prediction_train)# 0.84375
np.mean(y_test==prediction_test)# 0.7552083333333334


