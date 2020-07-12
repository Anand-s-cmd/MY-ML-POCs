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
a = np.array([1.0,2.0,3.0,4.0,5.0,6.0])  # RIGHT
a
print(a.reshape(2,3))
a.itemsize                  

a.size 

import numpy as np
 a = np.arange(15).reshape(3, 5)
a.dtype.name
a.itemsize

"""
ndarray.itemsize
the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.
"""

a1=np.array([1.0,2.0,3.0,4.0])
a1.reshape(2,2)
a1.dtype.name
a1.itemsize

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
type(a)                     #### <type 'numpy.ndarray'>

a.itemsize                  ###  8
a.size                      ###     15


b = np.array([(1.5,2,3), (4,5,6)])
b
"""
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
"""

 import numpy as np
a = np.array([2,3,4])
a
a.dtype

b = np.array([6, 7, 8])     ### B
b

array([6, 7, 8])
type(b)                     ##### <type 'numpy.ndarray'>

###   Q------>> NUMY LIN
"""
https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/
"""
np.zeros( (3,4) )
"""
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]]) 
"""


np.ones( (2,3,4), dtype=np.int16 )                # dtype can also be specified

"""
TRIED GIVING NODATA TYPE N CHECKED DEFAULT IT SHOWED FLOAT64
array([[[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]],

       [[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]]], dtype=int16)

"""
































