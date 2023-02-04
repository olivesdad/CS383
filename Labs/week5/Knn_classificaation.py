#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:59:43 2023

@author: ashiraki
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
#%%

df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)

# 3. How would you get an overview of the data?
# use info(), describer() andn the spyder variable explorer

#4 Okay!
X = df[['Outstate', 'F.Undergrad']].values
#returns 1 for true 0 for false array
y = (df['Private']=='Yes').values.astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.30, random_state=42)

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

#check scaled
X_train[:10,:]

#6. Build a KNN classifier and train it. 
# Use the default value of k (which is parameter n_neighbors KNeighborsClassifier). 
# See lecture slides.
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predictions=knn.predict(X_test)
accuracy = (predictions==y_test).mean()

'''
7. Make predictions using the training set, and save the predictions as variable 'predictions'.

8. Compare the first ten predictions with the first ten correct (test set) values.

9. Which two variables do you need to compute the accuracy of your classifier on the test set?
I guess I compare predictions to y_test
10. Compute and print the test set accuracy of your classifier.
'''
y_test[:10] == predictions[:10]

