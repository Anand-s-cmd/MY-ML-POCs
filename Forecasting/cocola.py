import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import SimpleExpSmoothing # SES
from statsmodels.tsa.holtwinters import Holt # Holts Exponential Smoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing # 
import statsmodels.graphics.tsaplots as tsa_plots
import statsmodels.tsa.statespace as tm_models
from datetime import datetime,time

data = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Forecasting\\CocaCola_Sales_Rawdata.csv")
Q_vals =['Q1','Q2','Q3','Q4'] 
data.columns

p = data["Quarter"][0]
p[0:2]


data['Q_vals']= 0

for i in range(42):
    p = data["Quarter"][i]
    data['Q_vals'][i]= p[0:2]
data.head()

Q_vals_dummies = pd.DataFrame(pd.get_dummies(data['Q_vals']))
data = pd.concat([data,Q_vals_dummies],axis = 1)

data["t"] = np.arange(1,43)


data.columns
data["log_Sales"] = np.log(data["Sales"])
data["t_Sqr"] = data["t"]*data["t"]

Train = data.head(30)
Test = data.tail(12)

####################### L I N E A R ##########################
import statsmodels.formula.api as smf 

linear_model = smf.ols('Sales~t',data=Train).fit()
pred_linear =  pd.Series(linear_model.predict(pd.DataFrame(Test['t'])))
rmse_linear = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(pred_linear))**2))
rmse_linear#714.0144483818342

##################### Exponential ##############################

Exp = smf.ols('log_Sales~t',data=Train).fit()
pred_Exp = pd.Series(Exp.predict(pd.DataFrame(Test['t'])))
rmse_Exp = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(np.exp(pred_Exp)))**2))
rmse_Exp#552.2821039688088

#################### Quadratic ###############################


Quad = smf.ols('Sales~t+t_Sqr',data=Train).fit()
pred_Quad = pd.Series(Quad.predict(Test[["t","t_Sqr"]]))
rmse_Quad = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(pred_Quad))**2))
rmse_Quad#646.2715428656

################### Additive seasonality ########################

add_sea = smf.ols('Sales~Q1+Q2+Q3',data=Train).fit()
pred_add_sea = pd.Series(add_sea.predict(Test[['Q1','Q2','Q3']]))
rmse_add_sea = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(pred_add_sea))**2))
rmse_add_sea#1778.0065467724

################## Additive Seasonality Quadratic ############################

add_sea_Quad = smf.ols('Sales~t+t_Sqr+Q1+Q2+Q3',data=Train).fit()
pred_add_sea_quad = pd.Series(add_sea_Quad.predict(Test[['Q1','Q2','Q3','t','t_Sqr']]))
rmse_add_sea_quad = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(pred_add_sea_quad))**2))
rmse_add_sea_quad #586.053306842576

################## Multiplicative Seasonality ##################

Mul_sea = smf.ols('log_Sales~Q1+Q2+Q3',data = Train).fit()
pred_Mult_sea = pd.Series(Mul_sea.predict(Test))
rmse_Mult_sea = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(np.exp(pred_Mult_sea)))**2))
rmse_Mult_sea# 1828.923891189194

##################Multiplicative Additive Seasonality ###########

Mul_Add_sea = smf.ols('log_Sales~t+Q1+Q2+Q3',data = Train).fit()
pred_Mult_add_sea = pd.Series(Mul_Add_sea.predict(Test))
rmse_Mult_add_sea = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(np.exp(pred_Mult_add_sea)))**2))
rmse_Mult_add_sea #410.24970605321283

################## Testing #######################################

data = {"MODEL":pd.Series(["rmse_linear","rmse_Exp","rmse_Quad","rmse_add_sea","rmse_add_sea_quad","rmse_Mult_sea","rmse_Mult_add_sea"]),"RMSE_Values":pd.Series([rmse_linear,rmse_Exp,rmse_Quad,rmse_add_sea,rmse_add_sea_quad,rmse_Mult_sea,rmse_Mult_add_sea])}
table_rmse=pd.DataFrame(data)
table_rmse
"""
               MODEL  RMSE_Values
0        rmse_linear   714.014448
1           rmse_Exp   552.282104
2          rmse_Quad   646.271543
3       rmse_add_sea  1778.006547
4  rmse_add_sea_quad   586.053307
5      rmse_Mult_sea  1828.923891
6  rmse_Mult_add_sea   410.249706
"""

""" so here rmse_Mult_add_sea is having least rmse so we are using it for for future predictions """ 