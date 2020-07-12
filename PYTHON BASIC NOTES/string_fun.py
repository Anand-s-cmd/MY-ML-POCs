# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:54:49 2019

@author: UX009405
"""

s1="bangalore"
s1=s1.capitalize()
print(s1)

s2="Karnataka"
s2=s2.casefold()
print(s2)

a = "Mushroooom soup" 
print(a.count("O"))
print(a.count("o"))
print(a.count("oo"))
print(a.count("ooo"))
print(a.count("Homer"))
print(a.count("o", 4, 7))
print(a.count("o", 7))

a = "Banana"
print(a.endswith("a"))
print(a.endswith("nana"))
print(a.endswith("z"))
print(a.endswith("an", 1, 3))

a="anand"
print(a.endswith("d"))

c = "Fitness"
print(c.isalnum())

c = "123"
print(c.isalnum())

c = "1.23"
print(c.isalnum())

c = "$*%!!!"
print(c.isalnum())

c = "0.34j"
print(c.isalnum())



c = "Fitness"
print(c.isalpha())

c = "123"
print(c.isalpha())

c = "$*%!!!"
print(c.isalpha())

a="anand"
print(a.islower())

b="ANAND"
b=b.lower();
b=b.upper();
print(b)



