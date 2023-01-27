#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:32:25 2023

@author: ashiraki
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import 
infile = 'https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv'
df = pd.read_csv(infile)

#1 Look at some of the data using the variable explorer in the upper right pane of Spyder.
# (Select the 'Variable explorer' tab and double click on 'df'.)
'''
 √ check
'''

#2 Look at the type of each column in df.  (We'll sometimes refer to the columns as 'variables', 'attributes', or 'features'.) 
# How many columns are shown as numeric?  Do you think some of the columns should be numeric but aren't?
'''
There are 2 numeric types. recieptt_amt is a float64 and file_nunm is an int64
Potentially zipcodes could be converted to numeric for speed but I'm not sure if performing arithmetic operations or comparisons on zipcodes is useful
'''

#3 Which of the columns contain NA values?  Use Python to figure out the total number of NA values in the data set. 
df.isna().sum() #<~~per columb
df.isna().sum().sum()  #<-- total in df

#4 Can you find values (besides 'nan') that indicate missing data?  
# You can try doing this with Python or by searching manually through df.
# High-level hint: you might expect an NA value in a column to appear many times.
top5=df.apply(lambda x: x.value_counts().index[0:5])
bottom5=df.apply(lambda x: x.value_counts().index[-5:])
'''
Created top5 and bottom5 lists from columns but didnt find anything. I manually found "NONE" but not sure if that counts as missing data
'''

#5 Does missing data exist in attribute contbr_employer? 
# If so, how is it encoded?  Would it make sense to change it?
df['contbr_employer'].isna().sum()
#I dont know if we should change it. Seems to work as it is. Do we gain anything by changing it to 'NA' string?

#6 Look more at contbr_employer.  Do you see any other data quality issues?
'''
I notice that there are multiple terms that seem to imply unemployed (NA None, Not EMployed, nan)
'''
#7 How many different values are there in attribute ‘memo_cd’? 
# What are the values?  What fraction of the values are empty?
df['memo_cd'].isna().sum()
df['memo_cd'].value_counts()
'''
there is X and nan. Above lists the counts
'''

#8 Attribute ‘contb_receipt_amt’ is the amount of the contribution. 
# Produce a histogram of the values.  Be sure your plot has a good title and good axis labels.
plt.hist(df['contb_receipt_amt'])
plt.ylabel('Count')
plt.xlabel('Amount ($)')
plt.title('Contribution Amount')

#9 What is the range of ‘contb_receipt_amt’ values? 
# Do any of them look suspicious?  How should you deal with negative campaign contributions? 
# Do negative contributions tend to be paired with positive contributions?
df['contb_receipt_amt'].min()
df['contb_receipt_amt'].min()
'''
-5400 to 10800
I dont understand how there could be negative receipt amounts 
'''
#10 Attribute contbr_zip has the zip code of a contributor. 
# Are all zip codes in the same format? 
# If not, do you think it would be appropriate to process the zip code data?
df['contbr_zip'][lambda x : x.str.match(r'[0-9]{8}')!=True]
df['contbr_zip'][lambda x : x.str.match(r'[0-9]{8}')==True]
df.shape[0]
'''
looks like there are 19402 that are 8numbers long and 598 that are 5 digets long. Maybe we should clip them all at 5?
'''
#11 Create a histogram of the lengths of contbr_employer values (i.e., the length of the values as strings). 
# Is the distribution unusual? 
# Give an explanation, based on working with the data, of why some employer length values seem to be very popular.

#12 If we scale a vector of numeric values using 0-1 scaling,
# then the smallest value in the vector will become 0, the largest will become 1,
# and the others will be scaled linearly between 0 and 1.  Create a new attribute, s_amt1,
# from ‘contb_receipt_amt’ by using 0-1 scaling. 

#13 What do memo_cd values mean?  How do they relate to the values in ‘memo_text’? 
# Note: an "earmarked" contribution is one that's not given directly to a candidate 
# but marked to indicate the candidate to which the contribution will be given.

#14 If you still have time, try some of the other methods discussed in the lecture for finding 
# and fixing bad data.

#15 If you still have time, try creating a new attribute s_am2 from the same attribute by using Z-score normalization.  In Z-score normalization of a numeric vector, the mean value in the vector will become 0, a value 1 standard deviation about the mean will become 1, a value 1 standard deviation below the mean will become -1, etc.