#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:46:07 2018

@author: Newton
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

cereal = pd.read_csv('cereal.csv', delimiter = ';')

### Info about cereal ###
#print(cereal.head())
#print(cereal.describe())
#print(cereal.columns) 
#print(cereal.shape)

### Let's get rid of the first row (since they are all strings)
cereal = cereal.drop(0)
#print(cereal.head())

### One issue: 
#print(cereal.dytpes)

### So we do
for col in cereal.loc[:,'calories':'rating']:
   cereal[col] = pd.to_numeric(cereal[col])
#print(cereal.dtypes)

# remove categorical variables
cereal_num = cereal.loc[:,'calories':'rating']

# normalize by cup amount
for ii in range(cereal.shape[0]):
    cup_amnt = cereal_num.loc[ii+1,'cups']
    cereal_num.iloc[ii,:] = cereal_num.iloc[ii,:]*(1/cup_amnt)

# separate X and y data
X = cereal_num.drop('rating',axis = 1)
y = cereal_num['rating']

# fit linear regression model
reg = LinearRegression().fit(X, y)
print(reg.score(X,y))