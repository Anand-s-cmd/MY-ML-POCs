# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:10:32 2019

@author: UX009405
"""

import pandas as pd
import numpy as np

mba = pd.read_csv("C:\\EXCELR\Excelr Data\\Python Classes\\Basic Statistics _ Visualizations\\mba.csv")

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
