# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:45:58 2019

@author: UX009405
"""

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
    
    # Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)
    
count = 0
while count <= 5:
    print(count)
    count += 1  # This is the same as count = count + 1


##########-----------------"break" and "continue" statements
    
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    
    
    # Prints out only odd numbers --- 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)