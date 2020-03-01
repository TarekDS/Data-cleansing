# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:34:28 2019

@author: T
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing


#importing Arrhythmia data
url= ("https://archive.ics.uci.edu/ml/machine-learning-databases/arrhythmia/arrhythmia.data")
df = pd.read_csv(url, header = None)

df.head()
df.dtypes

#removing range to columns
df.drop(df.iloc[:, 16:280], inplace=True, axis=1)

# deleting another obsolete column 
df = df.drop(15, axis=1)

#adding column names
df.columns = ['Age','Sex','Height','Weight','QRS','P-R','Q-T','Tinterval','Pinterval','QRS','T','P','QRST','J','Heartrate']

print (df[14])

df.Age.unique()
df.loc[:,"Age"].value_counts().plot(kind='bar')
plt.hist(df.loc[:, "Age"])


df.Height.unique()
df.loc[:,"Height"].value_counts().plot(kind='bar')
plt.hist(df.loc[:, "Height"])
df["Height"].describe()

#calculating median for height
df["Height"].median()

#outlier replacement: storing all values above 200 in toohigh variable
toohigh = df.loc[:, "Height"] > 200
#replacing the above values with median
df.loc[toohigh, "Height"] = 164

df.Weight.unique()
df.loc[:,"Weight"].value_counts().plot(kind='bar')
plt.hist(df.loc[:, "Weight"])

#checking null values 
df.isnull().sum()
df['Age'].where(df['Age'] = '?')

# null or misisng values in J
df.loc[df['J'] == '?']

#since most values are missing removing column J
df = df.drop("J", axis=1)

#Binning & Normalizing 
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
np.shape(df)
df['Age'] = df['Age'].astype('float64') 
pd.options.mode.chained_assignment = None

# Create x, where x the 'scores' column's values as floats
x = df[['P-R']].values.astype(float)

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)
df_normalized
print(x)

#concatinate age and sex
df["AgeSex"] = df["Age"].map(str) + df["Sex"].map(str)


df.to_excel(r'C:\Users\T\Desktop\Python\Data science Uwash\File Name.xlsx')
df_normalized.to_excel(r'C:\Users\T\Desktop\Python\Data science Uwash\TariqAyub-M02-Dataset.csv')

