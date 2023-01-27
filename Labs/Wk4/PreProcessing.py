#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 23:02:25 2023

@author: ashiraki
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# REad data

wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")

#Make a small version of the data set named 'df' by selecting 20 random rows of it. 
#Use the small version until instructed otherwise.
df = wine.sample(20)
#Scale the data using Z score normalization.
z_data=(df-df.mean())/df.std()

#In the scaled data, find the column minimums (a vector containing the minimum value for each column).
df.min()

#Repeat, but for the column maximums.  Did you get the kinds of values you expected?
df.max()
# Scale the data again using unit-interval normalization. 
# Scale the original small data set, not the version you just normalized.
unit_data=(df-df.min())/(df.max() - df.min())

#Again, find the column mins and maxes.  Did you get what you expected?
unit_data.min()
unit_data.max()
'''
Min and max for all columns are 0 and 1.
This is expected because we scaled the data to make the lowest data point 0 and the largest 1
'''

#Now we’ll return to the full data set.  Use 'df = wine' to assign 'wine' to variable 'df', 
# then compute the correlation coefficient for  Use function pandas.dataframe.corr(r) to see 
# how the features are correlated.
corr = df.corr()
sns.heatmap(corr, xticks=corr.columns, yticks=corr.columns)
#Looking at the matrix of correlations, which features are the most positively correlated? 
'''
fixed acidity : citric acid
fixed acidity : density
free sulfer dioxide : total sulfer dioxide
'''

#Which are the most negatively correlated?
'''
PH : fixed acidity
citric acid: pH
density: alcohol
citric acid: volitile acidity
'''
#Display the correlations with a plot, and answer the questions of the previous problem again.
sns.heatmap(corr, xticks=corr.columns, yticks=corr.columns)
#Which features are most correlated to the ‘quality’ variable?  Express what you find in plain English?
'''
it looks like there is a positive correlation between quality and alcohol and a negative correlation between volitatil 
acidity and quality
'''
#Is the wine data tidy?