""" ELECTION"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


"""
SINCE IN THE CSV FILE AS FIRST ROW IS NAN WE ARE DROPPING HE FIRST ROW NOW

"""

election = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Logistic Regression\\solution\\election_data.csv", skiprows=[1],dtype={"Result":"int64","Year":"int64","Popularity Rank":"int64"})
election.head(10)

election.columns

election=election.rename(columns={"Election-id": "Electionid", "Amount Spent": "AmountSpent", "Popularity Rank": "PopularityRank"})
election.shape

corrmat = election.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(10,10))
#plot heat map
g=sns.heatmap(election[top_corr_features].corr(),annot=True,cmap="RdYlGn")
sns.heatmap(election.isnull(),yticklabels=False,cbar=False,cmap='viridis')

election.head(10)

import statsmodels.formula.api as smf
import seaborn as sns
sns.heatmap(election.isnull(),yticklabels=False,cbar=False,cmap='viridis')
sns.heatmap(election.isnull(),yticklabels=False,cbar=False,cmap='viridis')
election.isnull().sum()
"""
Electionid        0
Result            0
Year              0
AmountSpent       0
PopularityRank    0
"""

election.corr()
election.columns
#Model building 
import statsmodels.formula.api as smf
#import statsmodels.formula.api as smf
#logit_model = smf.logit('ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data = claimants).fit()
#""" DONT CO SIDER ELECTION_D SINCE IT IS UNIQUE"""
logit_model = smf.logit('Result~Year+AmountSpent+PopularityRank',data = election).fit()
logit_model.summary()

election.head(10)

