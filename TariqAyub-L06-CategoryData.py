# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:07:58 2019

@author: T
"""

# importing data set
import pandas as pd

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/mammographic-masses/mammographic_masses.data"
dataset = pd.read_csv(url, header = None)
dataset.head()

#decoding categorical data
dataset.columns = ["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"] 
print (dataset["Shape"].unique())

dataset.loc[dataset.loc[:, "Shape"] == "1", "Shape"] = "Triangle"
dataset.loc[dataset.loc[:, "Shape"] == "2", "Shape"] = "oval"
dataset.loc[dataset.loc[:, "Shape"] == "3", "Shape"] = "square"
dataset.loc[dataset.loc[:, "Shape"] == "4", "Shape"] = "round"

#Imputing missing values and consolidating it with round(4)
dataset.loc[dataset.loc[:, "Shape"] == "?", "Shape"] = "round"

# 4 new columns, one for each state in "Shape"
dataset.loc[:, "Triangle"] = (dataset.loc[:, "Shape"] == "Triangle").astype(int)
dataset.loc[:, "oval"] = (dataset.loc[:, "Shape"] == "oval").astype(int)
dataset.loc[:, "square"] = (dataset.loc[:, "Shape"] == "square").astype(int)
dataset.loc[:, "round"] = (dataset.loc[:, "Shape"] == "round").astype(int)


# deleting obsolete column 
dataset = dataset.drop("Shape", axis=1)

#Ploting Triange 

dataset.loc[:,"Triangle"].value_counts().plot(kind='bar')

#Summary: Categorical data was first  analyze to check the 
#unique values. Then each unique value was decoded by assigning
#a value. in the process, missing values were also consolidated
#with round shapes. After that though one-hot encoding, new
#columns were added for each categorical value for the Shapes
#column. These columns have binary value i.e. 1 for yes and 
# 0 for no. data is plotted for Triangle column. 