# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:45:33 2019

@author: T
"""
# importing numpy
import numpy as np

# data set with good values which can be used to calculate mean or meadian
flaggood = ([1,2,3,4,5,6,7,8])

#data with outliers 
xy = np.array([1,2,3,4,5,6,77,8,9,0])
print(xy)

#calculating target values 2 std above and 2 below the mean
limithi = np.mean(xy) + 2*np.std(xy)
limitlo = np.mean(xy) - 2*np.std(xy)

print(limitlo)

#indexing xy aray with a boolean check 
flagbad = (xy < limitlo) | (xy > limithi)

flagbad

#replacing 77 (which was an outlier) with the mean of flaggood data set
xy[flagbad] = np.mean(xy)
print(xy)