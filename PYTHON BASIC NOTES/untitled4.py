# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:03:17 2019

@author: UX009405
"""

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
for phone in phonebook:
  print(phone)
print(phonebook)

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))