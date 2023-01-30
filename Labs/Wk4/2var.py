#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:06:27 2023

@author: ashiraki
"""

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

file = 'https://raw.githubusercontent.com/grbruns/cst383/master/College.csv'

df = pd.read_csv(file, index_col=(0))        # use the 'index_col=0'


'''
3. Create scatter plots to compare some of the variables.  Here are some questions to help you get started.  Follow your curiosity.
    Do smaller colleges spend more?  (variables F.Undergrad and Expend)
    Do smaller colleges charge more?  (variables F.Undergrad and Outstate)
    
    Define two new variables: perc.accept and perc.enroll. 
        The first is the percentage of students who accepted out of those who applied 
        (use variables Accept and Apps).  The second is the percentage of students who enrolled 
        out of those where were accepted (use variables Enroll and Accept).
Now use the new variables in scatter plots.  
For example: are more selective colleges more expensive, generally?

For each scatter plot that you create, write something about the form/shape, 
the direction, and the strength.  Think about the possible meaning of the scatterplot.

Don't just stick to my suggestions, choose some of your own variables to explore.  Think of questions that you find interesting. 
'''
# Add column for total students
df['tot_stud'] = df['F.Undergrad'] + df['P.Undergrad']
#plot expendetures as a function of total students enrolled
sns.scatterplot(data=df, x= 'F.Undergrad' , y='Expend')
# Looks like there might be a weak correlation between smaller colleges and higher spending
sns.scatterplot(data=df, x= 'F.Undergrad' , y='Outstate')
plt.title('Size vs cost')
#Cost at smaller colleges seems to be evenly distributed accross the cost axis so no correlation

# percentage stuff created columns
df['p.accept'] = df['Accept'] / df['Apps']
df['p.enroll'] = df['Enroll'] / df['Accept']
#scatter plots

sns.scatterplot(data=df, x='p.accept' , y='Outstate')
# It looks like the very selective colleges (acceptance < 30%) are more expensive.
# The cost seems to be lower for colleges with acceptance rates > ~85% 
# Between 30%-85% seems to be pretty evelny distributed

# Do private colleges have different acceptance rates? 
sns.catplot(data=df, x="Private", y="p.accept")
# Looks like no

#Do Private colleges cost more?
sns.catplot(data=df, x="Private", y="Outstate")
# Looks like yes

#try pairplot
sns.pairplot(data=df, hue='Private',vars=['Grad.Rate', 'tot_stud', 'Accept', 'Outstate'] )






