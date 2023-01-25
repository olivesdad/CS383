#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

"""
1. I found some interesting data with Elecgtric vehicle charger locations. I downloaded the CSV but didnt  know what to do with it
¯\_(ツ)_/¯
"""
#Import data using pd.read_excel
df=pd.read_excel('Unemployment.xlsx', header=4)

#read old data
df_old=pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/unemployment.csv")

"""
How does the work you’re doing with this data to get it into pandas data frame relate to the need to have your results be replicable? 
How would you document the source of the data set, and what you did to get it into a format that Python can use?
~~~
I think documenting the  process used to import the data  into pandas is important because if someone uses a different
tool or different import steps, they may not be able to replicate your results / analysis.
It seems like this data set is being continuously updated which could also cause peers to be unable to replicate your 
results in the future. I think if possible, it would be a good idea to take a dataset freeze frame to present with you research
~~~
"""

"""
Data sets often come with associated data dictionaries that explain where the data comes from, 
what the attributes mean, etc.  Where is the documentation for this data set?
~~~
The source of the data and instructions on how to access the "definitions" are provided in the first 4 rows of the original xlsx file
These rows were removed by the dataimport as they are not needed for analysis 
~~~
"""
