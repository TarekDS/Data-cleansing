# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:30:30 2019

@author: Tariq
"""
# calling all required lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing data set from UCI public site. Setting head to none so that right row isn't considered a header
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/mammographic-masses/mammographic_masses.data"
mam = pd.read_csv(url, header= None)

#naming all the columns in the table
mam.columns = ["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"]

mam.dtypes
#remvoing errors 
mam.loc [:,"BI-RADS"] = pd.to_numeric(mam.loc[:,"BI-RADS"], errors= 'coerce')

#creating a variable hasnan to do a boolean comparision and identify Nan data
hasnan = np.isnan(mam.loc[:, "BI-RADS"])

print(hasnan)

#replacing Nan values with median. 
mam.loc[hasnan,"BI-RADS"] = np.median(mam.loc[:, "BI-RADS"])
#ploting a histogram for BI-RADS column
plt.hist(mam.loc[:, "BI-RADS"])
#calculating mean for the same
mam["BI-RADS"].median()

#outlier replacement: storing all values above 6 in toohigh variable
toohigh = mam.loc[:, "BI-RADS"] > 6
#replacing the above values with 6
mam.loc[toohigh, "BI-RADS"] = 6

#upon checking the data types for all the columns for mam dataframe several columns were non-integers
#these columns need to be convered to integer values to be able to apply math functions
#i have cleaned up BI-RADS by replacing NaNs with median values 
# the distribution of this column has a right tail with outliers on the higher side
#we removed the outliers by limiting the data set to a certain value and replacing the
#execing values with the max limit. 
-----------------------------------------------------------------------------------------
I have questions regarding the difference btw the following statements 
In the earlier lessons we have learned to use Median but in the questions 
the correct answer was nanmedian
Heart.loc[HasNan, "chol"] = np.median(Heart.loc[:,"chol"])
#output  67.65771142295964
Heart.loc[HasNan, "chol"] = np.nanmedian(Heart.loc[:,"chol"])
#output  64.98224504483035
