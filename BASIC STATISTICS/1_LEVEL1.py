"""
Q3) Three Coins are tossed, find the probability that two heads and one tail are obtained?

HHH
HHT-------------------->1
HTH-------------------->2
TTH
HHT-------------------->3
THT
TTH
TTT
 
SO TOTAL 8, PROB = NO OF INTERSTED EVENTS/TOTAL EVENTS= 3/8===0.375

ASK HOW THIS QUESTION MEANS AND WHAT EXACTLY EXPECTS?
Q6) Calculate the Expected number of candies for a randomly selected child 
Below are the probabilities of count of candies for children (ignoring the nature of the child-Generalized view)
CHILD	Candies count	Probability
A	1	0.015
B	4	0.20
C	3	0.65
D	5	0.005
E	6	0.01
F	2	0.120
Child A – probability of having 1 candy = 0.015.
Child B – probability of having 4 candies = 0.20
Here they are asking expected value so that is,
μ= ∑Xp(x)
so that is, 
FOR A PROBABILITY DISTRUBUION THE MEAN OF THE DISTRUBUTION IS KNOW AS EXEPCTED VALUE SO NOW

(1*0.015+4*0.20+3*0.65+5*0.005+6*0.01+2*0.120)
= 3.09


Q7) Calculate Mean, Median, Mode, Variance, Standard Deviation, Range &     comment about the values / draw inferences, for the given dataset
-	For Points,Score,Weigh>
Find Mean, Median, Mode, Variance, Standard Deviation, and Range and also Comment about the values/ Draw some inferences.

import pandas as pd
x = {"POINTS":pd.Series([1,2,3,4,5,7,8]),"SCORE":pd.Series(["A","B","C","D","E","F","G"]),"WEIGHT":pd.Series([1,2,3,4,5,7,8]),"D":pd.Series([1,2,3,4,5,7,8,11])}
new_x = pd.DataFrame(x) ## MAKING HERE ALSO DATA FRAME---pandas.core.frame.DataFrame
type(new_x)
new_x

1. POINTS
new_x['Points'].mean() # mba.gmat.mean()
new_x['Points'].median()
new_x['Points'].mode()
new_x['Points'].var()
new_x['Points'].std()

max(new_x['POINTS'])
min(new_x['POINTS'])

range = max(new_x['POINTS'])-min(new_x['POINTS']) 
range

2. SCORES

new_x['SCORES'].mean() # mba.gmat.mean()
new_x['SCORES'].median()
new_x['SCORES'].mode()
new_x['SCORES'].var()
new_x['SCORES'].std()

max(new_x['SCORES'])
min(new_x['SCORES'])

range = max(new_x['SCORES'])-min(new_x['SCORES']) 
range

3. WEIGHTS
new_x['WEIGHTS'].mean() # mba.gmat.mean()
new_x['WEIGHTS'].median()
new_x['WEIGHTS'].mode()
new_x['WEIGHTS'].var()
new_x['WEIGHTS'].std()

max(new_x['WEIGHTS'])
min(new_x['WEIGHTS'])

range = max(new_x['WEIGHTS'])-min(new_x['WEIGHTS']) 
range

"""
### ---> HERE I AM USING NUMPY TO CALCULATE MEAN LIKE NP.MEAN() THEN PANDAS?
https://www.geeksforgeeks.org/python-pandas-dataframe-skew/ ----> ask this here how it calulats the skew when axis=0 and 1
#https://www.geeksforgeeks.org/python-pandas-dataframe-skew/
import numpy as np
import pandas as pd
mtcars = pd.read_csv("C:\\EXCELR\\MY PYTHON SCRIPTS\\Cars.csv")
type(mtcars)
mtcars.columns


mtcars['SP'].skew(axis=1, skipna=True)#ValueError: No axis named 1 for object type <class 'pandas.core.series.Series'>



#https://www.geeksforgeeks.org/python-pandas-dataframe-skew/
"""
SKEWNESS FORMULA=E[(X-mU/SIGMA)]3
KURTOSIS FORMULA=E[(X-mU/SIGMA)]4
""""
"""mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
   """ 
"""
VV IMP LINK    http://www.datasciencemadesimple.com/get-maximum-value-column-python-pandas/
SO HEREWE HAVE TO TAKE CARS.CSV FILE BUT WE SHOULD SIOME COLUMNS SO USE DF METHODS TO SKIW COLUMNS"""
        
mtcars = pd.read_csv("C:\\EXCELR\\MY PYTHON SCRIPTS\\Cars1.csv", usecols = lambda column : column not in ["HP" , "MPG", "VOL"])
mtcars.columns
mtcars.skew(axis=0, skipna=True)
still ans is different we took in CArs1.csv same as their values but
""" MY QUESTION IF I WANT TO FIND SKEW FOR INDIVIDUAL COLUMNS LIKE MTCARS['SP'].SKEW() THEN?"""



NEXT NOW KURTOSIS
pd.Series([10, 25, 3, 25, 24, 6])
mtcars = pd.read_csv("C:\\EXCELR\\MY PYTHON SCRIPTS\\Cars1.csv", usecols = lambda column : column not in ["HP" , "MPG", "VOL"])
sr=pd.Series(mtcars)

mtcars.kurt(axis = 0) 


#Q11)
#34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56
import pandas as pd
df=pd.Series([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
df
df.mean()
df.median()
df.var()
df.std()
range = max(df)-min(df) 
range
