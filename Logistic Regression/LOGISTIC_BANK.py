""" LOGISTIC_BANK """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

bank = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Logistic Regression\\solution\\bank_data.csv")
bank.head(5)
bank.shape
bank.isnull().sum()

import statsmodels.formula.api as smf
logit_model = smf.logit('ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data = claimants).fit()
logit_model.summary()

corrmat = bank.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(10,10))
#plot heat map
g=sns.heatmap(bank[top_corr_features].corr(),annot=True,cmap="RdYlGn")
bank["pdays"]=1
bank.pdays
#################################################################################################
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X = bank.iloc[:,0:31]  #independent columns
y = bank.iloc[:,-1]    #target column i.e price range
#apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  #naming the dataframe columns
print(featureScores.nlargest(10,'Score'))  #print 10 best features
####################