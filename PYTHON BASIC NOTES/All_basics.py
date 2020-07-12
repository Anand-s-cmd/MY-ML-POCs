# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:32:16 2019

@author: UX009405
"""
#############SOME PACKAGES############
import os
import re
import math
import calendar
import sys
######################################
cars=10
print(cars)
cars
print(type(cars))

a,b=1,"anand"
print (a)
print (b)

################
s="anand huded"
ss=s.split(" ")
print (ss[0])
#################

n=input("enter a no")
print ("no is ",n)
type(n)

n1=int(input("enter a no "))
print ("no is ",n1)
n2=float(input("enter a no "))
print ("no is ",n2)
n3=n1+n2
print ("n3 is ",n3)
type(n3)



n1=eval(input("enter a no "))
print ("no is ",n1)
n2=eval(input("enter a no "))
print ("no is ",n2)
n3=n1+n2
print ("n3 is ",n3)
type(n3)


##############################################Strings
n1=eval(input("enter a no "))   # 4
print ("no is ",n1)
n2=eval(input("enter a no "))  # anand 
print ("no is ",n2)
n3=n1+n2                  ####### name error
print ("n3 is ",n3)
type(n3)



n1=eval(input("enter a no "))
print ("no is ",n1)
n2=eval(input("enter a no "))
print ("no is ",n2)
n3=n1+n2
print ("n3 is ",n3)
type(n3)



#####################exception handling ##########################
try:
    n1=eval(input("enter a no "))
    print ("no is ",n1)
    n2=eval(input("enter a no "))
    print ("no is ",n2)
    n3=n1+n2
    print ("n3 is ",n3)
except(ZeroDivisionError,NameError,KeyboardInterrupt,SyntaxError):
    print ("plase enter non zero")
    print ("plase enter VALID NUMBER")
    print ("GOOD BYE ECAPING")
    print ("VALID IP")
    
    
###############         Strings  ########################3333  
##### 12345678910 
name="anandhupeq"
print (name)    
print (name[0])    
print (name[1:9]) 
print (name[0:9])     
print (name[-1])    
print (name[-3 : -1])
#################output
##    anandhupeq
##    a
##    nandhupe
##    q
##    pe
 #####012345678910=11
name="0123456789"
print (name)    
print (name[0])    
print (name[1:9])  
print (name[0:9])    
print (name[-1])    
print (name[-3 : -1])


s="hello world"
print (s) 
print (s[2:5] + " python")

print(s.capitalize())

print(s.center(50))


print(s.count("world"))
substring="l"
count=s.count(substring)
print(count)

s="anandaa huded"
n=1
##### FOR INT %d FOR FLOAT %f
print("my name is %s and no is %d" % (s,n))
print("%s %f" % (s,n))

print(s.capitalize())
count=s.count("n")
print(s.upper())
print(s.replace("a","s",2))### replace with count
help(s.replace)


str1 = "Bob,"
str2 = 1
print("Hello %s hello %s" % (str1, str2))


var = 224 
#print "The var is %d" %(var)

var = 224
print("The var is %d" % var)
print("The var is", var)

## 0,1,2,3,4,5,6
n=[1,2,3,4,5,6,7]
print(n[1:6])


################ DECISION MAKING IFS
val1=True
val2=100

if val1 and val2 > 200:
   print ("val1 is true and val2 > 200")
elif val1 and  not(val2):
    print ("second")
elif val1 and  (val2==100):
    print ("anand")
else:
   print("normal")    
    

######functions
def display(name,age):
    print ("hi", name,age)
display("anand",1)    


################LOOPS#############

travel=input("yes or No : ")
while travel=="Yes":
     No=int(input("no of people "))
     for n in range(1,No+1):
         name=input("name-")
         age=input("age-")
     travel=input("oops forgot someone!! Yes/No-")
else:
    print("good day")
    
    
    
team=input("yes or No\n")    
while team=="yes":
     no=int(input("no of people\n"))
     for n in range(1,no+1):
         name=input("name is ")
         age=input("age is ")
     team=input("forgot any one ")    
else:
    print("good day")     
    
     
##########MODULES#############
    
import math
math.sqrt(16)
math.pow(2,5)

import calendar
cal=calendar.month(2018,1)
cal
print (cal)
calendar.isleap(2019)
dir(calendar)


##to give path for a module########
import sys
sys.path.append("C://python notes")


####call module and use functions

import functions as f
t_area=f.triangle_area(3,4)
print (t_area)

s_area=f.square_area(3,4)
print(s_area)

###############FILE HANDLING###############


import os
 if os.path.exists("C://python notes//aa.txt"):
    os.remove("C://python notes\\aa.txt")
 else:
    print("file does not exist")

###########
f=open("C://python notes\\a.txt","w")
f.write("adding some data to the file. ")
f.close()

f=open("C://python notes//a.txt","r")
print(f.readline())

f=open("C://python notes//a.txt","a")
f.write("Adding some more data!\n yes.")

f=open("C://python notes//a.txt","r")
print(f.readline())

import os
os.rmdir("C://python notes//AA")

import os
if os.path.exists("C://python notes//aa.txt"):
    os.remove("C://python notes//aa.txt")
else:
    print("path doesn't exists")

f=open("C://python notes\\a.txt","r")
for x in f:
    print(x)


############REGULAR EXPRESSIONS"###################

import re
details="""Anand 256 Huded 29 Aman 36"""
age=re.findall(r'\d{1,3}',details)
print (age)
age=re.findall(r'\d{1,2}',details)

name=re.findall(r'[A-Z][a-z]{1,5}*',details)
name=re.findall(r'\w{5}',details)
name=re.findall(r'[A-Z][a-z]*',details)
print (name)

address_dict={}
x=0
for eachname in name:
    address_dict[eachname]=age[x]
    x+=1
print(address_dict)    

import re
s="name"
allname=re.findall(s,",my name is anand and what is ur name")
print(allname)
for name in allname:
    print(name)
    
    
import re
s="name"
allname=("my name is anand and what is ur name")
print(allname)
for i in re.finditer("name",allname):
    loc=i.span()
    print(loc)
    