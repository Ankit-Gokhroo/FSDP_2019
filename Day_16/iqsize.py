# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:16:48 2019

@author: Ankit Gokhroo
"""
'''
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 
Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

df=pd.read_csv('iq_size.csv')

df.describe()
df.info()


features = df.iloc[:, 1:].values
labels = df.iloc[:,0].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

print(regressor.intercept_)  
print (regressor.coef_)

Pred = regressor.predict(features_test)

import pandas as pd

print (pd.DataFrame(Pred, labels_test))


import numpy as np
x = [90,70,150]
x = np.array(x)
x = x.reshape(1,3)
regressor.predict(x)

Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)



















