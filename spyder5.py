#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:18:23 2017

@author: bryanpham
"""

import numpy as np
import pandas as pd

mydata = {'productcode': ['AA','AA', 'AA', 'BB', 'BB', 'BB'],
          'sales': [1010, 1025.2, 1404.4, 1251.7, 1160, 1604.8],
          'cost': [1020, 1625.2, 1240, 1003.7, 1020, 1124]}
df = pd.DataFrame(mydata)
#print(df.shape)
#print(df.head(3))
#print("=========")
#print(df.describe())
#df['sales'].hist()
df.boxplot(column='sales')