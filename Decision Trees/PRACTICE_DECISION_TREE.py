""" DECISION TREE PRACTICE"""

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\DECISION TREE\\iris.csv")
data.head()
data['Species'].unique()
""" ITS 3 CLASS PROBLEM, SO WE HAVE CATEGARIZED ON 3 CLASSES
array(['setosa', 'versicolor', 'virginica'], dtype=object)"""

"""
Q*** very important thing is
since it is 3 class classifier problem at the end our 
crosstab or confusion matrix looks like 3 by 3 matrix
"""

data.Species.value_counts()
"""
versicolor    50
virginica     50
setosa        50

EQUAL PROPORTION OF DATA
Q*** WHAT IF UNEQUAL PROPORTION OF DATA WAS PRESENT?
"""

colnames=list(data.columns)
predictors=colnames[:4]
target=colnames[4]

# Splitting data into training and testing data set

import numpy as np

from sklearn.model_selection import train_test_split
train,test = train_test_split(data,test_size = 0.3)

from sklearn.tree import DecisionTreeClassifier
help(DecisionTreeClassifier)

model=DecisionTreeClassifier(criterion='entropy')
""" NOW DECISION CLASSIFIER OBJECT IS CREATED NOW FIT THE DATA BELOW"""
model.fit(train[predictors],train[target]) 
"""
Q***
HERE ABOVE THE MODEL TAKES GAIN AND CONCLUDES WHICH IS ROOT NODE AND PERFORMS DECISION TREE CLASSIFICATION
AND MAKES THE MODEL READY
"""

""" X, Y ABOVE"""
""" HERE ABOVE MODEL TAKES ALL INPUTS VARIABLE FROM TRAIN DATA
AS WELL AS TAKES OUTPUT VARIABLE FROM TRAIN DATA"""

# NOW MODEL IS READY GO FOR TRAIN TEST PREDICTIONS

pred_train=model.predict(train[predictors])
pred_test=model.predict(test[predictors])
""" FOR ABOVE TRAIN TEST PREDICTIONS MODEL MAKE USE OF TRAIN AND TEST DATA TO PREDICT"""

pd.crosstab(train[target],pred_train)
"""
col_0       setosa  versicolor  virginica
Species                                  
setosa          35           0          0
versicolor       0          37          0
virginica        0           0         33
"""
""" ACCURACY FOR TRAIN MODEL"""
train_accuracy=np.mean(train.Species==model.predict(train[predictors])) #1.0
train_accuracy#1.0


pd.crosstab(test[target],pred_test)
"""
col_0       setosa  versicolor  virginica
Species                                  
setosa          15           0          0
versicolor       0          13          0
virginica        0           0         17
"""
""" ACCURACY FOR TEST MODEL"""
test_accuracy=np.mean(pred_test==test.Species) #1.0
test_accuracy#1.0
""" ACTUALLY IT WILL GIVE OVERFITTING MODEL MOST AND MOST OF THE TIMES
BUT NOW IT HAS GIVEN BOTH TEST AND TRAIN ACCURACY MEANS GOOD MODEL"""

