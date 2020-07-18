# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:21:17 2019

@author: UX009405
"""
#IT CAN BE  DONE IN 3 WAYS
#using scatter plots
#using Z score
#using the IQR interquartile range

dataset= [10,12,12,13,12,11,14,13,15,10,10,10,100,12,14,13, 12,10, 10,11,12,15,12,13,12,11,14,13,15,10,15,12,10,14,13,15,10]
import numpy as np
import pandas as pd
outliers=[]
def detect_outlier(data_1):
    
    threshold=3
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for y in data_1:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers
outlier_datapoints = detect_outlier(dataset)
print(outlier_datapoints)

#######################  ORRRRRRRRRRRRRRRR ######################

import numpy as np
import pandas as pd
dataset= [500,12,12,13,12,11,14,13,15,10,10,10,100,12,14,13, 12,10, 10,11,12,15,12,13,12,11,14,13,15,10,15,12,10,14,13,15,10]
print(len(dataset))
outliers=[]
mean_1=0
std_1=0
threshold=3
def detect_outlier(data_1):
    
    #mean_1+=1  ### ------->  UnboundLocalError: local variable 'mean_1' referenced before assignment
    #std_1+=1   ### ------->  UnboundLocalError: local variable 'mean_1' referenced before assignment
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for y in data_1:
        z_score= (y - mean_1)/std_1 
        print (" y's zscore is",y,z_score)
        if np.abs(z_score) > threshold:
            outliers.append(y)
            #global outliers
            #outliers+=y
    return outliers

outlier_datapoints = detect_outlier(dataset)
print(outlier_datapoints)


####################   USING IQR METHOD              ################################
dataset= [500,12,12,13,12,11,14,13,15,10,10,10,100,12,14,13, 12,10, 10,11,12,15,12,13,12,11,14,13,15,10,15,12,10,14,13,15,10]
sorted(dataset)
q1, q3= np.percentile(dataset,[25,75])
print (q1, q3)
iqr = q3 - q1
print(iqr)

lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 

print(lower_bound,upper_bound)



import numpy as np 
    
# 1D array  
arr = [20, 2, 7, 1, 34] 
print("arr : ", arr)  
print("50th percentile of arr : ",  
       np.percentile(arr, 50)) 
print("25th percentile of arr : ", 
       np.percentile(arr, 25)) 
print("75th percentile of arr : ", 
       np.percentile(arr, 75)) 





import numpy as np 

array = []
for x in range(3, 6):
    array += [x]
print (array)


##   --------->> VERY VERY IMPORTANT EXAMPLES-------------------------->

counter = 0
def increment():
  
  counter += 1

print(counter)
increment()


counter = 0
print("line1")
def increment():
  global counter
  
  counter += 1
  print("line2")   
  print(counter)
print(counter)
increment()
print(counter)  

x = 10
def foo():
   ## x=1   --------> >>    IF IT WAS ASSIGNED INSIDE BECAUSE HERE READS DATA BEFORE GOING TO MAKE ANY OPERATION 
   ##---------- >> https://eli.thegreenplace.net/2011/05/15/understanding-unboundlocalerror-in-python
    x += 1
    print (x)
foo()


x = 10
def foo():
    global x
    x += 1
    print (x)
foo()



###----------------------->  RANDOM NUMBER GENERATION AND OUTLIERS FINDING

import numpy as np   
print(np.random.randint(20, size=(1, 1000)))
############

# identify outliers with standard deviation
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50
# calculate summary statistics
data_mean, data_std = mean(data), std(data)
# identify outliers
cut_off = data_std * 3
lower, upper = data_mean - cut_off, data_mean + cut_off
# identify outliers
outliers = [x for x in data if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))






x=1.5
y=10

if y > x:
    print("yes")


import numpy as np
####################   USING IQR METHOD              ################################
dataset= [3,500,12,12,13,12,11,14,13,15,10,10,10,100,12,14,13, 12,10, 10,11,12,15,12,13,12,11,14,13,15,10,15,12,10,14,13,15,10]
sorted(dataset)
q1, q3= np.percentile(dataset,[25,75])
print (q1, q3)
iqr = q3 - q1
print(iqr)
outliers=[]
nonoutliers=[]
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
print(type(lower_bound))
print(type(upper_bound))

#print(lower_bound,upper_bound)
for y in dataset:
    if y < lower_bound or y > upper_bound:
      outliers.append(y)
      print(y)    
    if y >= lower_bound and y <= upper_bound:
        nonoutliers.append(y)
print(outliers)          
print(nonoutliers)          



##-------------------------ONE MORE EXAMPLE


# identify outliers with interquartile range
from numpy.random import seed
from numpy.random import randn
from numpy import percentile
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50
# calculate interquartile range
q25, q75 = percentile(data, 25), percentile(data, 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
print(outliers)
# remove outliers
outliers_removed = [x for x in data if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))






import scipy.stats as st

st.norm.ppf(0.80)#---> EQUIVALENT TO QNORM() IN R

import matplotlib.pyplot
import pylab

x = [1,2,3,4]
y = [3,4,8,6]

matplotlib.pyplot.scatter(x,y)

matplotlib.pyplot.show()