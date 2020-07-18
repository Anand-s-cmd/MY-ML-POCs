# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:00:26 2019

@author: UX009405
"""

################     Numpy details

###      https://docs.scipy.org/doc/numpy/user/quickstart.html
###      NumPy’s main object is the homogeneous multidimensional array. 
###     It is a table of elements (usually numbers), all of the same type,
###     indexed by a tuple of positive integers. In NumPy dimensions are called axes.

import numpy as np
#a = np.array(1,2,3,4)    # WRONG
import numpy as np
a = np.array([1,2,3,4,5,6])  # RIGHT
print(a.reshape(2,3))

import numpy as np
a = np.arange(15)
a
print(a)
a.shape                   

print(a.shape)
a
print(a.reshape(3,5))
a.shape                     ###(3, 5)

a.ndim                      ### 2

a.dtype.name                ### 'int64'

a.itemsize                  ###  8

a.size                      ###     15

type(a)                     #### <type 'numpy.ndarray'>

b = np.array([6, 7, 8])     ### B
b

array([6, 7, 8])
type(b)                     ##### <type 'numpy.ndarray'>
 