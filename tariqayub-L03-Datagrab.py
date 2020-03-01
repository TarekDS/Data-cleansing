# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:44:49 2019

@author: T
"""

#importing pandas
import pandas as pd
#assigning url variable
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
#reading CSV 
web_data = pd.read_csv(url, header=None)
#printin first 5 rows 
print(web_data.head())
#renaming a few columns
web_data.rename(columns={0:"index", 1:"type", 13:"country"})