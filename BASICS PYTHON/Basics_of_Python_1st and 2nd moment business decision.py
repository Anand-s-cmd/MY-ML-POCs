# Python Basics
name = "Awesome "
type(name)
len(name)

name.lower()
name.capitalize()
"thisis".capitalize()
name.upper()

name[1]
name[-6:]   ##--> esome
# String conversion
str(9)
str(213)
# Adding strings 
"this "+"is "+"awesome"

name.replace("e","t")

# String manipulation 
import re

re.sub("[^A-Za-z' ']"," ","ada 1231zxdq #@$@zxfsd312")
       
re.sub("[A-Za-z]"," ","ada 1231zxdq #@$@zxfsd312")
name
re.sub("[Aes]","x",name)

name.replace("e","FF")
name.endswith("e")

re.sub("[ABE]"," ","ACBDEETWERW")


name[0]="B" # string does not support assignment operator
# Explore more string functions 

# And, or, not => and, or, not operators for operating between different conditions 

# Loops and Conditional programming 
# if elif else key words


x = [1,2,3,4,5,611,100,100,12,1231,101,5,-1]
x
type(x)

x.insert(1,1000)
x.sort(reverse=True)
x
x.reverse()
x
x.append(["E","Y","E"])
x.append("ASDDASDAS")
x.extend("this")
x
x.extend([100,200,400,500])

x
print(x)
x.extend("123")
x
x = [1,2,3,4]
y=["A","B","C"]

x+y

#######################################

if not (3>4):
    print ("yes")

per = 100

if per < 3:
    print ("A")
elif per <5:
    print ("B")
elif per < 6:
    print ("C")
elif per < 7:
    print ("D")
else:
    print ("None")

    


if (12%3==0) and (12%2==0):
    print ("first")
    print ("this")
elif 6%2==0:
    print ("second")
    
elif 10%5==10:
    print ("No")
else:
    print ("no other conditions satisfying")
    


x

for i in x:
    if (i%2==0):
            print (i)
            print ("even")
    else:
        print (i)
        print("odd")

range(10)
range(10,20)
range(10,20,4)




x
for i in x:
    if i%2==0:
        print ("even")
    elif not i%2==0:
        print ("odd")
    else:
        print ("IDK")



for i in x:
    for j in y:
        if (j>i):
            print ("yes")
        elif j==i:
            print ("hi")
        else:
            print ("yes")
            print ("this ")
   
         
print ("hello")
            
for i in range(10,100,2):
    print (i)



i = 10


while i<20:
    i = i+1
    print (i)



print ("hello")


# Creating our custom functions - syntax 
        
def sum(i,j=100):
    add = 0
    for k in i:
        add = add+k+j
    print (add)
    


sum([1,2,3,4,56,7])

sum([1,2,3,4,5,6,100])



import math

def confirm_prime(i):
    j=2
    if i < 2:
        print ("IDK")
    elif i == 2:
        print ("Yes")
    else:
        j=2
        a = int(math.sqrt(i))
        while (j<a):
            if i%j==0:
                #print ("No")
                break
            else:
                j=j+1
    if j >= int(math.sqrt(i)):
        print("Yes")
    else: print ("NO")



# Enter only whole numbers 
confirm_prime(100)
confirm_prime(120)
confirm_prime(7)

k = [2,3,5,7,11,13,1,100,143,12,17,19,20]
len(k)




for i in k:
    confirm_prime(i)


# type gets you type of data or type of data structure 
# lists and dictionaries 
x = [1,2,3,5,6]
len(x)            
for i in x:
    print (i)

y = [11,12,13,14]
x+y
# list functions
x.append(100)
x.append([101,102,103])
x.extend([104,105])
x.index(100)
y.insert(13,200)

x*2
x = [-100,20,53,25,-6,17,80,9]
x.sort(reverse=True)
x
y=[]
for i in x:
    if i<30:
        y.append(i*10)
        
[i*10 for i in x if i<30]


[z for z in range(2,4) if z<5]## TRIAL
[i*10 for i in x if not i%2==0]

j=[1,2,3,4,6,8]

x = [i+5 for i in j]
x
x = [1,2,100,10,-5,-20,53,32,23]
x.sort(reverse=False)
x
x.sort(reverse=True)
x


import pandas as pd
# dictionaries 
x = {"A":[10],"C":[-12],"B":[30],"E":[5],"F":[120],"I":[6],"G":[12],"H":[100]}

type(x)
import pandas as pd
pd.DataFrame(x)





x
type(x)

x.keys()

x.values()

x["H"] = 100
x["F"] = 1000
x["C"] = 2018
x
del x["I"]
x["Z"] =121
x
#stop_words = 
# sorting dictionary 
x.items()
z = list(x.items())
z

"+".join([i for i in "IAM" if not i in "I"])
" ".join("this is".split(" "))

for i in x.items():
    print ("key "+i[0]+" and its value is "+ str(i[1]))

x = {"Z":100,"X":1000,"G":300,"A":1000,"C":1000}
x
x.items()
for i in x.items():
    print (i[0])
    print (i[1])

y = x
y = sorted(x.items(),key = lambda p:p[1])

y
y.reverse()
y
dict(y)


z = dict(y)
z

if "i" in "this":
    print ("yes")
    
"thisiseawsome"
["t","h","s",...]

[i for i in "thisiseawsome" if i in "i"]

"".join([i for i in "thisiseawsome" if not i in "i"])



"+".join(["this","is","awsome"])
"".join([i for i in "thisiseawsome" if i not in "i"])

############ Usage of lambda function #################



# [i for i in x if i%2==0]



######## Numpy ############
import numpy as np
import matplotlib.pyplot as plt

x = [10,21,3,14,15,16]
y = np.array(x)
type(y)
y[0:5]
y.shape
y>10
y[y>10]


y**2
y+1
y[y%2!=0]

x = [1,2,3,4,5,6]
y = [7,8,9,10,11,12]

np.array(y).shape
z = np.array([x,y])
z = z.reshape(4,3)
z
z[0]
z.shape
z[0:1]
z[0:2]
z[0:3]
z[1:0]
z[1:1]
z[1:2]
z[:,1]  
z[:,0,]

"""
trickyyyyyyyyy
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
"""
z
z[:,1]  ## array([ 2,  5,  8, 11])
z[1,:]  ## array([4, 5, 6])

# Statistics on numpy array 
np.mean(z)
np.median(z)
np.mean(z[1,:])
np.mean(z[:,1])
np.std(z)
np.var(z)

np.corrcoef(z[1,:],z[3,:]) ##  Q---> DIDNT UNERSTAND
"""
z[1,:] 1th row and z[3,:] 3rd row
"""


# Few functions in numpy 
np.round(1.21212,2)

temp1 = np.random.normal(10,2,5)
temp2 = np.random.normal(-10,2,5)

temp2
temp1
temp3 = np.column_stack((temp1,temp2))
""" column_stack() --> https://www.geeksforgeeks.org/numpy-column_stack-in-python/ """
temp3
m1 = np.random.random((2,3))
m2 = np.random.random((2,3))
m1
m2
m1+m2
"""
DIFFERENCE BETWEEN np.random.normal vs np.random.randn

https://www.geeksforgeeks.org/rand-vs-normal-numpy-random-python/

"""
############################################
# Importing necessary libraries
import pandas as pd # importing pandas = > useful for creating dataframes
import numpy as np   # importing numpy = > useful for creating numpy arrays 


x1 = [1, 2, 3, 4,5] # list format 
x2 = [10, 11, 12,100]  # list format 

x3 = list(range(5))

# Creating a data frame using explicits lists
X = pd.DataFrame(columns = ["X1","X2","X3"]) 
X

X["X1"] = x1 # Converting list format into pandas series format
X["X2"] = x2 # Converting list format into pandas series format
X["X3"] = x3

X["X1"] = pd.Series(x1)  # Converting list format into pandas series format
X["X2"] = pd.Series(x2) # Converting list format into pandas series format
X["X3"] = pd.Series(x3)

# accessing columns using "." (dot) operation
X.X1
# accessing columns alternative way
X["X1"]

# Accessing multiple columns : giving column names as input in list format
X[["X1","X2"]]

# Accessing elements using ".iloc" : accessing each cell by row and column 
# index values

"""
iloc---Q------------> 
"""
X.iloc[0:3,1]
X.iloc[0:3,1]
X.iloc[:,:] # to get entire data frame 
X.loc[0:2,["X1","X2"]]
# checking the type of variable 
type(X.X1) # pandas series object

# to create a data frame 
x = pd.DataFrame(columns=["A","B","C"])

# np.random.randint(a,b,c) 
# a - > starting number
# b - > Ending number
# c - > no. of numbers to be generated 
x["A"] = pd.Series(list(np.random.randint(1,100,50)))

# np.random.choice([a,b],size=c)
# a and b = > choosing elements from a or b 
# c = > number of elements to be generated choosing from a or b
x["B"] = pd.Series(list(np.random.choice([0,1],size = 50)))

x["C"] = 10 # going to fill all the rows in "C" with value 10


import pandas as pd
help(pd.read_csv)
# Import data (.csv file) using pandas. We are using mba data set
mba = pd.read_csv("C:\\EXCELR\Excelr Data\\Python Classes\\Basic Statistics _ Visualizations\\mba.csv")
mba[45:51]
type(mba) # pandas data frame

mba.mean()


mba.columns # accessing column names 
mba.datasrno # Accessing datasrno using "." (dot) operation

mba["workex"]
mba[["datasrno","workex"]] #  accessing multiple columns 
mba.iloc[45:51,1:3] # mba.iloc[i,j] 
# i => row index values  | j => column index values
mba.loc[45:51,["workex","datasrno"]]

mtcars = pd.read_csv("C:\\EXCELR\Excelr Data\\Python Classes\\Basic Statistics _ Visualizations\\mtcars.csv")
mtcars
mtcars.cyl.value_counts()
mtcars.cyl.value_counts().plot(kind="pie")
mtcars.carb.value_counts().plot(kind="pie")


# to get the count of each category from a specific column 
mtcars.gear.value_counts()

# Accessing elements using conditional input 
import pandas as pd

mtcars.gear==3

temp = mtcars[(mtcars.gear==3) | (mtcars.cyl==4)]
temp.shape
temp.gear.value_counts()
temp.carb.value_counts()

# and operation (&) 
mtcars_19_2_4 = mtcars[(mtcars.gear==3) & (mtcars.mpg > 19.2)] #  and operation (&)

# or operation (or)
mtcars_5 = mtcars[(mtcars.gear==4) | (mtcars.gear==5)]

# Gear 4 and 5 cars only 
mtcars_4_5 = mtcars[(mtcars.gear==5) | (mtcars.gear==4) | (mtcars.gear==6)]


# isin operator which functions similar to that of "or" operator 
list(range(15,21,2))
mtcars_4_5 = mtcars.loc[mtcars.mpg.isin(list(range(15,25,1))),["cyl","mpg"]]
mtcars_4_5


list(range(15,21,1))
mtcars_2_4_5 = mtcars.loc[mtcars.carb.isin([1,4,2]),["mpg","carb"]]


x = mtcars[(mtcars.mpg >19) & (mtcars.mpg<25)]
mtcars_15_19 = mtcars[(mtcars.mpg>15) & (mtcars.mpg<19)]

# line 76 and 79 will return same output 
                    
# Creating custom function 

def MEAN(i): # taking only one parameter 
    a = sum(i)  
    b =len(i)
    print (a/b)

x = [1,2,3,4,5,6,8]
MEAN(x)  



# using if and else conditional statements 
def check_even(i):
    # function body
    if i%2==0:
        print ("even")
    else:
        print ("odd")

check_even(10)
check_even(101)

# using if, elif and else conditional statements 
def is_even_odd(i):
    if i<5:
        print ("<5")
    elif i<10:
        print ("<10")
    elif i<20:
        print ("<20")
    else:
        print ("None")
    


x = [1,2,[1,2,4],43,54] # list format 


# For loop syntax 
for i in x:
    print (i)
    
for i in range(10):
    print (i)

for i in range(1,10,1):
    print (i)
    
# range(a,b,c)

for i in range(1,10,3):
    print (i)

# while loop syntax 
i = 1
while i < 10:
    print (i)
    i= i+1
    

x = [[1,2],[1,2,4],[43],[54],[2,3,4]]

# using break operation to terminate any for loop in middle
for i in x:
    if len(i)>2:
        break
    else:
        print (i)
    
a = [] # creating empty list 
a.append(1) # appending new element to list variable "a"

a.append([1,2]) # appending new list to list variable "a"
a.extend([1,2,3]) # appending each element separately using extend 
a


# Giving input from the console at the time of execution of python code
# and appending each elements when we enter from console 


def even_num(i):
    for j in i:
        if j%2==0:
            print ("even")
        else:
            print ("odd")
            


            
even_num([1,2,3,4,5,6])

    
    
mtcars.std()

for i in range(1,10):
    a.append(int(input()))

# Creating a data frame manually from lists 
new_df = pd.DataFrame(columns=["A","B","C"])
new_df["A"] = pd.Series([1,2,3,4,5,6])    
new_df["B"] = pd.Series(["A","B","C","D"])   
new_df["C"] = pd.Series([True,False,True,False])

# Dropping rows and columns 

new_df.drop(["A"],axis=1,inplace=True) # Dropping columns 
# axis = 1 represnts drop the columns 
# new_df.drop(["A","B"],axis =1, inplace=True) # Dropping columns 
# inplace = True  = > action will be effective on original data 


# Dropping rows => axis =0
mba.drop(mba.index[[5,9,19]],axis=0) # ,inplace=True) # Dropping rows 
# selecting specific rows using their index values in list format
#  X.index[[1,2,3,4,5]] => dropping 1,2,3,4,5 rows 

# X.drop(X.index[[5,9,19]],axis=0, inplace = True)

#X.drop(["X1","X2"],aixs=1) # Dropping columns
#X.drop(X.index[[0,2,3]],axis=0) # Dropping rows 

# Creating a data frame using dictionary object 
x = {"A":pd.Series([1,2,3,4,5,7,8,10]),"B":pd.Series(["A","B","C","D","E","F","G"]),"C":pd.Series([1,2,3,4,5,7,8]),"D":pd.Series([1,2,3,4,5,7,8,11])}
new_x = pd.DataFrame(x)
new_x
##--> Q--> IF THERE ARE NOT ENOUGH ELEMTS IN THE SERIES THEN IN THE OLUMN "NaN" VALUE WILL BE FILLED AND 
##--> FLOAT VALUES WILL BE FILLED LIKE  "1.00" IF ALL VALES ARE THERE THEN THE CLOUMN WIL BE FILLED WITH INTEGER VALUS 
##--> AS WECAN SEE IN THE COLUMN D
# Dictionary object
dict_new = {"A":pd.Series([1,2,3,4,5,7,8]),"B":pd.Series(["A","B","C","E","F","G"]),"C":pd.Series([1,2,3,4,7,8])}
pd.DataFrame(dict_new)
dict_new.keys() 
dict_new.values()
dict_new["A"] # accessing values using the key
# In any dictionary object we have unique keys and keys must not be repeated
# values can be of any size and can be repeated 


# Finding mean,median,mode
mba.mean()
mba['gmat'].mean() # mba.gmat.mean()
mba['gmat'].median()
mba['gmat'].mode()
mba['gmat'].var()
mba['gmat'].std()

# variance & Standard Deviation for Sample
mba['gmat'].var() # 860
mba['gmat'].std() # 29.39

# Variacne & Standard Deviation for Population
import numpy as np
np.var(mba['gmat']) # 859.70
np.std(mba['gmat']) # 29.32


# calculating the range value 
range = max(mba['gmat'])-min(mba['gmat']) # max(mba.gmat)-min(mba.gmat)
range

# calculating the population standard deviation and variance 
np.var(mba.gmat) # population variance 
np.std(mba.gmat)  # population standard deviation