# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:51:14 2019

@author: Ankit Gokhroo
"""

"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.
 
Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Female_Stats.Csv')
df.info()

features = df.iloc[:,1:].values
labels = df.iloc[:, 0].values

import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

print(regressor.intercept_)  
print (regressor.coef_)

labels_pred = regressor.predict(features) 
df1 = pd.DataFrame({'actual height':df['Height'],'predictheight': labels_pred})  
print (df1) 

x=[67,73]
x=np.array(x)
x=x.reshape(1,2)
regressor.predict(x)


















