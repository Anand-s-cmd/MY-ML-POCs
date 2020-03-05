import pandas as pd 
import numpy as np 
import seaborn as sns

forest = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\SVM\\forestfires.csv")
forest.head()
forest.describe()
forest.columns


forest['size_category']=np.where(forest['size_category']=='small',0,1)
forest.head()
forest.columns

forest1=pd.get_dummies(forest['month'],drop_first=True)
forest1.columns
forest=pd.concat([forest,forest1],axis=1)
forest=forest.drop('month',axis=1)

forest1=pd.get_dummies(forest['day'],drop_first=True)
forest1.columns
forest=pd.concat([forest,forest1],axis=1)
forest=forest.drop('day',axis=1)

forest['target_size']=forest['size_category']
forest=forest.drop('size_category',axis=1)
forest.columns

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
train,test = train_test_split(forest,test_size = 0.3)
test.head()
forest.shape
train_X = train.iloc[:,0:45]
train_X.columns
train_y = train.iloc[:,-1]
test_X  = test.iloc[:,0:45]
test_y  = test.iloc[:,-1]

model_linear = SVC(kernel = "linear")
model_linear.fit(train_X,train_y)
pred_test_linear = model_linear.predict(test_X)


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



