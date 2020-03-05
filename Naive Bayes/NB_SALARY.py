import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer

train_sal = pd.read_csv(r"C:\EXCELR\NOTES WRITTEN\SOLVING_ASSIGNMENTS\Naive Bayes\\SalaryData_Train.csv")
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


from sklearn.model_selection import train_test_split

train,test = train_test_split(train_sal,test_size=0.3)

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
word_data = CountVectorizer(analyzer=split_into_words).fit(train_sal)



# Preparing email texts into word count matrix format 
train_bow = CountVectorizer(analyzer=split_into_words).fit(train_sal.drop('target_salary',inplace=True,axis=1))


# For all messages
train_sal_matrix = train_bow.transform(train_sal.drop('target_salary',inplace=True,axis=1))
train_sal_matrix.shape #  (5559, 7429)

# For training messages
train_matrix = train_bow.transform(train.drop('target_salary',inplace=True,axis=1))
train_matrix.shape #  (3891, 7429)



# For testing messages
test_matrix = train_bow.transform(test.drop('target_salary',inplace=True,axis=1))
test_matrix.shape # (1668, 7429)(1668, 7429)