# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:11:47 2018

@author: madis
"""

a= 29.5/22.1
type(a)


b=( "Shelf","Controller","Computer",20, "TRUE", 18.23) 
type(b)


c = "Hello, EXCELR!"
print(c[1])
type(c)


d = "Hello, EXCELR!"
print(d[2:5])
d

#The strip() method removes any whitespace from the beginning or the end
e = " Hello, EXCELR! "
print(e.strip()) # returns "Hello, World!"


#The len() method returns the length of a string:

f = "You can find elements in a tuple since this doesn't change the tuple!"
print(len(f))
len(f)

#pip install camelcase
import camelcase

#if you want to uninstall a package
#open anaconda prompt and use a syntax pip uninstall camelcase


Bc =open("E://Excelr Data//Datasets//Datasets_BA 2//affairs.csv","r")
print(Bc.read())

Bp =open("E://Excelr Data//Datasets//Datasets_BA 2//affairs.csv","r")
print(Bp.readline())

Bs =open("E://Excelr Data//Datasets//Datasets_BA 2//py_test.txt","r")
print(Bs.read(10))

# os package used to delete a file from the local drive
import os
os.remove("E://Excelr Data//Datasets//Datasets_BA 2//fitness5.txt")


# To delete entire folder use os.rmdir()
os.rmdir("C://Users//madis//NAVIE BAYES")


###Variables
# Python programming don't have any command to declare a variable
# It can be assigned using = Symbol 

x=4 # its Integer
x="America" # Here its Str
x
#In the above a variable cannot be declared with any particular type and even you can
#over ride the data in that variable

#To combine both text and a variable, Python uses the + character:
x = "DATA SCIENCE"
print("Python with " + x)

#we can also use the + character to add a variable to another variable:
x = "Python with "
y = "DATA SCIENCE"
z =  x + y
print(z)

#If we try to combine a string and a number together, Python will throw you an error:
r = 28
type(r)
s = "DATA SCIENCE"
print(r + s ) ## error

#By specifying a variable with Type of the data- this can be done using Python Casting
x = int(1)   
y = int(2.8) 
z = int("3")
print(x+y+z)
type(y)


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
s = float("3")   # z will be 3.0
d = float("6.2")  # w will be 4.2
print(x)
print(x+y+z+w)

p="straight12" # combination of character with numeric gives you the data type str
type(p)

#List is a collection which is ordered and changeable. Allows duplicate members.
# and it's with square brackets
list = ["Apple", "Banana", "Kiwi"]
print(list)

#we can access the list items by referring to index number:
#Print the second item of the list:
list1 = ["Apple", "Banana", "Kiwi"]
print(list1[1])


#To change the value of a specific item, we have to refer index number:
list2 = ["Apple", "Banana", "Kiwi"]
list2[2]=" Grapes"
print(list2)

#To determine if a specified item is present in a list use the in keyword:
list3 = ["Apple", "Banana", "Kiwi"]
if "Apple" in list3:
  print("Yes, 'Apple' is in the fruits list")

# Print the number of items in the list:
list = [781, 232.3, 144.8,-993]
print(len(list))


#To add an item to the end of the list, use the append() method:

list = [12.8,153,-893,243, 456,-675]
list.append("orange")
print(list)

#To add an item at the specified index, use the insert() method:
#Insert an item as the third position:
list = [12.8,153,-893,243, 456,-675]
list.insert(2, "orange")
print(list)

#The remove() method removes the specified item:
list = [12.8,153,-893,243, 456,-675]
list.remove(153)
print(list)

# pop() method removes the specified index,(or the last item if index is not specified):
list = [12.8,153,-893,243, 456,-675]
list.pop(1)
print(list)

#The del keyword removes the specified index:
list = [12.8,153,-893,243, 456,-675]
del list[1]
print(list)

#The clear() method empties the list:
list = [12.8,153,-893,243, 456,-675]
list.clear()
print(list)

# reverse() Reverses the order of the list
list = [12.8,153,-893,243, 456,-675]
list.reverse()
print(list)

#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
tuple = (18.5,-223,45.5,54.3,332,789,432)
print(tuple)

tuple = (18.5,-223,45.5,54.3,332,789,432)
print(tuple[1])

#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
tuple = (18.5,-223,45.5,54.3,332,789,432)
tuple[2]= 123
print(tuple) # The values will remain the same:

#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
tuple = (18.5,-223,45.5,54.3,332,789,432)
del tuple
print(tuple)


##A set is a collection which is unordered and unindexed. 
#In Python sets are written with curly brackets.
set = {12, "note", 13.5,555, "tender"}
print(set)  #Sets are unordered, so the items will appear in a random order.


# To Add multiple items to a set, we will use update() method:
set = {12, "note", 13.5,555, "tender",-245,567,"Enter"}
set.update([18.5,-223,45.5," Data Science",54.3,332,789,432,"Python"])
print(set)

# remove() to remove an item from set
set = {12, "note", 13.5,555, "tender",-245,567,"Enter"}
set.remove("tender")
print(set)

# discard() 
set = {12, "note", 13.5,555, "tender",-245,567,"Enter"}
set.discard("Enter")
print(set)  # you wont get any error even if we give a false selected item to discard

import pandas as pd
import numpy as np
 x= np.array([2,1,3,0])
type(x)
x=np.arange(10)
type(x)

#creates arrays with a specified number of elements, 
#and spaced equally between the specified beginning and end values
x=np.linspace(2,4.,8.)
print(x)

x=np.random.random((4,8))
print(x)


