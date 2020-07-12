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


##### ----------- Iterating over dictionaries

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
    
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}


##############-----------------Removing a value

del phonebook["John"]
print(phonebook)    

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print (Dict["Tiffany"])


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print((Dict['Tiffany']))


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print (studentX)
print (studentY)


#####-----------------Check if a given key already exists in a dictionary
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in Dict.keys():
    if key in Boys.keys():
        print (True)
    else:       
        print (False)
#####-----------------Check if a given value already exists in a dictionary        
for key in Dict.values():
    if key in Boys.values():
        print (True)
    else:       
        print (False)        



Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print(Dict)
Dict



Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict ["Charlie"]
print (Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print ("Students Name: %s" % Dict.items())
