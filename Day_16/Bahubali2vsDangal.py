# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:34:08 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

df=pd.read_csv('Bahubali2_vs_Dangal.csv')

df.describe()
df.info()

features = df.iloc[:, :-2].values  
labels = df.iloc[:, 1:].values 


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.4, random_state=0)  

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 

print(regressor.intercept_)  
print (regressor.coef_)

labels_pred = regressor.predict(features_test) 

df1 = pd.DataFrame({'Actualbahubali2': labels_test[0],'actualdangal':labels_test[1], 'Predictedbahubali2': labels_pred[0],'Predicteddangal':labels_pred[1]})  
print (df1) 

regressor.predict(10) 

plt.scatter(features_test, labels_test[:,0], color = 'red')
plt.scatter(features_test, labels_test[1], color = 'green')

plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.plot(features_train, regressor.predict(features_train), color = 'green')
plt.title('movie collection')
plt.xlabel('day')
plt.ylabel('collection')
plt.show()

























