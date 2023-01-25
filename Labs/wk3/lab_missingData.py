#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:56:40 2023

@author: ashiraki
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#READ data
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv")

#Display first row of data 
df.head()

# What are the types of columns in the data frame?  Write the code to display them.
df.info()

#What is the total number of NA values in the data frame?  #
#What fraction of all the values in the data frame are NA's?
df.isna().sum().sum()
df.isna().sum().sum()/(df.shape[0] * df.shape[1])

#How many rows contain NA values?
(df.isna().sum(axis=1)[lambda x: x>0]).count()

#For each column, what fraction of the column values are NA values?
df.isna().sum()/df.shape[0]

#For each row, what fraction of the row values are NA?
df.isna().sum(axis=1) / df.shape[1]

#Following problem 6, plot, for each column, the fraction of the values in that column that are NA.
(df.isna().sum()/df.shape[0]).plot.bar()

# In this data set, if you decided to remove the NA values, 
# would you do it by removing rows, or by removing columns?
# I would Remove the rows. Removing the columns would remove that sensor for all locations

# Create a new data frame df_cleanrows that is like dat except all rows containing NA values are removed.  
# Verify that there are no NA values in df_cleanrows
df_cleanrows = df[df.isna().sum(axis=1) < 1]

#Create a new data frame df_cleancols that is like dat except all columns containing NA values are removed.
df_cleancols = df[df.columns[df.isna().sum() < 1]]

#Which contains more data, df_cleanrows, or df_cleancols? 
### Clean rows has more data. It contains 666 data points and cleancols contains 612

#Create a new data frame df_med from your original data frame ‘df’ by replacing each NA
# value with the median of its column.
df_med=df
for col in df_med.columns:
    df_med[col].fillna(df[col].mean(), inplace=True)
    
