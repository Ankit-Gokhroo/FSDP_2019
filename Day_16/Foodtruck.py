# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:09:42 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

df=pd.read_csv('Foodtruck.csv')

df.describe()
df.info()

df.plot(x='Population', y='Profit', style='o')  
plt.title('population vs profit')  
plt.xlabel('population')  
plt.ylabel('Profit')  
plt.show()

features = df.iloc[:, :-1].values  
labels = df.iloc[:, 1].values 

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 

print(regressor.intercept_)  
print (regressor.coef_)

labels_pred = regressor.predict(features_test) 

df1 = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print (df1) 

regressor.predict(3.073) 
plt.scatter(features_test, labels_test, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('population vs profit')
plt.xlabel('population')
plt.ylabel('profit')
plt.show()
















