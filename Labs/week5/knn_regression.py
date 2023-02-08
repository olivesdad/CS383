#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:57:30 2023

@author: ashiraki
"""

import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)
df.apply(zscore)

X = df[['Top10perc', 'F.Undergrad']].values

y = df['Outstate'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.33, random_state=42 )

#create scalar obj
scaler = StandardScaler()

#scale data
#X_train = scaler.fit_transform(X_train)
#X_test = scaler.transform(X_test)

##Build the model thing
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)

predictions[:10]
y_test[:10]

MSE = ((predictions - y_test)**2).mean()
RMS = math.sqrt(MSE)