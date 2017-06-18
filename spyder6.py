#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:10:02 2017

@author: bryanpham
"""

import pandas as pd
import statsmodels.api as sm
import numpy as np

#Read data from web

df = pd.read_csv("https://stats.idre.ucla.edu/stat/data/binary.csv")
print(df.describe())
print(df.shape)
#rename
df = df.rename(columns={'rank':'position'})

position_count = df.position.value_counts(ascending=True)
print(position_count)