# -*- coding: utf-8 -*-
"""
Multidimensional NumPy arrays lab
Enter your Python code after each prompt.

@author: Glenn Bruns
"""

import random
import numpy as np
import pandas as pd

# read student exam score data as a 2D NumPy array
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/sample-grades.csv").values

# print the score for the first student (row 0) and the third problem (column 2)
df[0,3]
# print all scores for student 15 (meaning row 15)
df[14,]
# print all scores for problems 0-3
df[:,0:3]
# print all scores for problems 1, 5, 7
df[:,[0,4,6]]
# assign the number of students to variable 'num_students'
num_students=np.shape(df)[0]
# run the following command to get random data representing scores
# on two additional extra credit problems
ec = np.random.choice(np.array([0,1,2,3], dtype='int64'), size=num_students*2).reshape(num_students, 2)

# print the shape of ec
np.shape(ec)
# update df so that the two rightmost columns are the data in array ec
df=np.hstack((df, ec))
# print the mean value of all the scores
df.sum()/(np.shape(df)[1]*num_students)
# print the number of scores > 2  (np.sum applied to a boolean mask will
# give the number of True values in the mask))
np.size(df[df>2])
# using a list comprehension, compute the total score for each student
# and assign the result to variable 'totals' as a NumPy array
totals=df.sum(axis=1)
# print the dtype of totals; it should be int64
totals.dtype
# assign the number of columns to variable 'num_problems'
num_problems=df.shape[1]
# using a list comprehension, compute the average score for each
# problem and assign the result to variable 'prob_means' as a NumPy array
df.sum(axis=0)/num_problems
# what is the lowest of the average score values?
np.sort(df.sum(axis=0)/num_problems)[0]
# Is it legal to subtract an array with shape (35,) from an
# array with shape (50,35)?  If so, what will happen?  Write
# your answer as a comment.
# No it is not illegal because first it can become (1,35) then it can be stretched to (50,35)
# the array (35,) will become (1,35), and will be subtracted
# from each row of the (50,35) array

# compute a new array df_centered, which is a 2D array with
# the same shape as df, but contains, for each column, the
# column values minus the average value for each column.
df_centered=df - df.sum(axis=0)/num_problems
# What do you expect as the average values of the columns of
# dat_centered?  Print the result to find out.

# consider extending idea about length of student trips, but make a matrix,
# where each row is a student, and 'mpg', 'miles' are columns.  In a separate
# array, show prices of gas at several gas stations.  
