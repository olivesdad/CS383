#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:13:24 2023

@author: ashiraki
"""
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#We’ll explore the 1994 US census summary data that is available here:
file = 'https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv'

#Create a Python file in Spyder, and write code to load the data.  For example:
df = pd.read_csv(file)
#Don't forget to put import statements in your file for numpy, pandas, matplotlib.pyplot, and seaborn.  Record your work for the following problems in a Python file.

# Visually explore the data frame using the Variable explorer tab in Spyder,
# which can be found in the upper right pane.
# Okie dokie

# Which Pandas commands can you use to get a quick overview of the data?
df.info()
df.describe().round(1)
# Remove the 'usid' and 'fnlwgt' columns from the data frame.
df.drop(labels=['usid', 'fnlwgt'], axis=1, inplace=True)
# Use a Pandas command to look at the first rows of the data frame.
df.head(1)
# The ‘education_num’ column records the number of years of education.  Use ‘describe’ to find min, max, median values for education_num.  Plot education_num using a histogram.  Label the x axis with 'years of education'.
df['education_num'].describe()
# Does it make sense to use education_num with a histogram?  
# Try it, and compare with a plot using a bar plot of the count of the rows by 
# education_num (as shown in lecture).
fig, ax = plt.subplots(1,2)
ax[0].bar(df['education_num'].value_counts().keys(), df['education_num'].value_counts().tolist())
ax[0].set_ylabel('count')
ax[0].set_xlabel('years')
ax[0].set_title('bar')
ax[1].hist(df['education_num'])
ax[1].set_ylabel('count')
ax[1].set_xlabel('years')
ax[1].set_title('histogram')
# Plot capital_gain with a density plot.  Did you find anything interesting?  
# Save your plot to a png file.
sns.kdeplot(df['capital_gain'], bw_method=0.5)
# Investigate attribute ‘workclass’.  Plot it in an appropriate way.
df['workclass'].value_counts().plot.bar()

# Use a bar plot to show the distribution of attribute ‘sex’.  Label the 'Male' and 'Female' bars with the fraction of rows associated with each sex (not a count).  Comment on what you find.  Why do you think the distribution is like this?
df['sex'].value_counts().plot.bar()
# Use a horizontal bar plot to visualize attribute marital_status.
df['marital_status'].value_counts().plot.barh()

# If you have time, visualize all the attributes you haven’t explored yet.  Be sure to include 'native_country'.

# If you still have time, do single-variable visualization for the attributes in the contribution campaign data.