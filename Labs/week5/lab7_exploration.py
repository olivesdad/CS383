#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:53:45 2023

@author: ashiraki
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file = 'https://raw.githubusercontent.com/grbruns/cst383/master/College.csv'

df = pd.read_csv(file)
'''
Derive a new column, ‘Size’, from the F.Undergrad variable.  
The possible values of Size should be “small”, “medium”, or “large”.
The value “small” should be assigned to the colleges in the “bottom 3rd” of F.Undergrad values, 
“medium” should be assigned to the “middle 3rd”, and “large” to the “top 3rd”. 
 Use the Pandas ‘quantile’ function to find the corresponding F.Undergrad values. 
 (If you're not sure how to do this, see the hints right away).
  
Create a barplot to make sure the number of small, medium, and large values are about the same.
  When you make a quick plot for yourself, no need for adding a title or axis labels.  
  When you make a plot for a report or to share, it's important to use a good title and axis labels.
'''

df['Size'] =pd.cut(df['F.Undergrad'], bins=df['F.Undergrad'].quantile([0,0.33,0.66,1]), labels=['small','medium','large'])
sns.countplot(data=df, x= 'Size')

'''
Use the faceting (also known as 'conditioning') idea to create three scatter plots, 
one for each value of your new variable size.  
The scatterplot should show PhD on the x axis and Outstate on the y axis.  
Try to make your plot look approximately like this:
'''

fig1=sns.FacetGrid(data=df,col='Size')
fig1.map(plt.scatter, 'PhD','Outstate', color='darkred')

'''
Repeat problem 5, but this time show a single scatterplot,
 with color used to distinguish small, medium, and large schools. 
 Your plot might look something like this:
'''

sns.scatterplot(data=df, x='PhD', y='Outstate', hue='Size')
# I think the scatter plot with different colors indicating size is easier to compare by seeing the colors overlayed

sns.scatterplot(data=df, x='PhD', y='Outstate',style='Size', hue='Size')

#Violin
sns.catplot(y='Outstate', col='Size', data=df, kind='violin', height=4, aspect=0.7)

sns.catplot(y='Outstate', col='Size', data=df, kind='violin', height=4, aspect=0.7, inner='stick')


g = sns.FacetGrid(df, row='Size', height=2.5, aspect=1.8)
g.map(plt.hist, 'PhD', color="darkred")
