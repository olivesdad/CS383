# -*- coding: utf-8 -*-
"""
Pandas dataframes

@author: Glenn Bruns
"""
import numpy as np
import pandas as pd


# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# =============================================================================
# Read data
# =============================================================================

# read 1994 census summary data
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv")
df.set_index('usid', inplace=True)
df.drop('fnlwgt', axis=1, inplace=True)

# =============================================================================
# Simple aggregation
# =============================================================================

# print the average age
df['age'].mean()
# get the min, max, and avg value for each numeric column
df.select_dtypes(include='number').agg(['min', 'max', 'mean'])
# for a dataframe you get the aggregate for each column by default

# =============================================================================
# Aggregation with grouping
# =============================================================================

# how many people in each category of education?
# Try using pandas function value_counts().
df['education'].value_counts()
# for each native country, what is the average education num?
df.groupby('native_country').agg({'education_num':'mean'})
# repeat the previous problem, sorting the output by the average
# education num value
df.groupby('native_country').agg({'education_num':'mean'}).sort_values(by='education_num')
# for each occupation, compute the median age
df.groupby('occupation').agg({'age':'median'})
# repeat the previous problem, but sort the output
df.groupby('occupation').agg({'age':'median'}).sort_values(by='age')
# find average hours_per_week for those with age <= 40, and those with age > 40
# (this uses something labeled 'advanced' in the lecture)
df.groupby(df['age']<=40).agg({'hours_per_week':'mean'})
# do the same, but for age groups < 40, 40-60, and > 60
df.groupby([df['age']< 40, df['age'] > 60]).agg({'hours_per_week':'mean'})
# get the rows of the data frame, but only for occupations
# with an average number of education_num > 10
# Hint: use filter
df.groupby('occupation').agg({'education_num':'mean'})[lambda x: x['education_num'] >10]
# =============================================================================
# Vectorized string operations
# =============================================================================

# create a Pandas series containing the values in the native_country column.
# Name this series 'country'.
country=df['native_country']
# how many different values appear in the country series?
country.value_counts().shape[0]
# create a Series containing the unique country names in the series.
# Name this new series 'country_names'.
country_names= pd.Series(country.value_counts().index)
# modify country_names so that underscore '_' is replaced
# by a hyphen '-' in every country name.  Use a vectorized operation.
# (See https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
country_names=country_names.str.replace('_','-')
# modify country_names to replace 'Holand' with 'Holland'.
country_names=country_names.str.replace('Holand','Holland')
# modify country_names so that any characters after 5 are removed.
# Again, use a vectorized operation
country_names=country_names.str.slice(0,5)
# Suppose we were to use only the first two letters of each country.
# Write some code to determine if any two countries would then share
# a name.
country_names[country_names.str.slice(0,2).isin((country_names.str.slice(0,2).value_counts()[lambda x: x > 1].keys()))].sort_values()
# If you still have time, write code to determine which countries
# do not have a unique name when only the first two characters are
# used.  Hint: look into Pandas' Series.duplicated().

# =============================================================================
# Handling times and dates
# =============================================================================

# read gas prices data
gas = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/Gasoline_Retail_Prices_Weekly_Average_by_Region__Beginning_2007.csv")

# create a datetime series and make it the index of the dataset

# plot the gas prices for NY city

# plot gas prices for NY city and Albany on the same plot

# if you still have time, see if you can find and plot California
# gas prices



