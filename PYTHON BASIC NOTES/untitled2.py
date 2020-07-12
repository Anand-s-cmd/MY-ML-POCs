# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 00:05:10 2019

@author: UX009405
"""

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
