import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


forest = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Neural Networks\\fireforests.csv")
forest.columns
forest.isnull().sum()
forest['target_area']=forest['area']
forest=forest.drop('area',axis=1)

month2=pd.get_dummies(forest['month'],drop_first=True)
forest=pd.concat([forest,month2],axis=1)
forest=forest.drop('month',axis=1)# REOVING COLUMNS

day2=pd.get_dummies(forest['day'],drop_first=True)
forest=pd.concat([forest,day2],axis=1)
forest=forest.drop('day',axis=1)# REOVING COLUMNS


forest.shape#(517, 45)


"""
we have 30 variable we should go for feature selections now
"""
x=forest.iloc[:,0:29]
x
y=forest.iloc[:,-1]
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model=ExtraTreesClassifier()
model.fit(x,y)

feat_imp=pd.Series(model.feature_importances_,index=x.columns)
feat_imp.nlargest(10).plot(kind='barh')

new_feat=pd.DataFrame(feat_imp.nlargest(10))
new_feat.head(10)#top 10 features

new_forest=forest[['daywed','daysun','daysat','dayfri','daythu','daymon','temp','daytue','RH','DC']]

forest.shape#(517, 45)
new_forest['y']=y
new_forest.shape#(517, 11)
new_forest.columns
from sklearn.model_selection import train_test_split 


X_train, X_test, y_train, y_test = train_test_split(x, y)

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
np.mean(y_train==prediction_train)#  1.0
np.mean(y_test==prediction_test)#  1.0


