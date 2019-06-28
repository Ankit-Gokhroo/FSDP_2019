# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:02:59 2019

@author: Ankit Gokhroo
"""

"""
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
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.

"""
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

#polynomial
import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [ 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

# add code to automate the p value removing
import statsmodels.api as sm
import numpy as np

features_obj = features[:, [0,1,2,3]]
features_obj = sm.add_constant(features_obj)
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else: 
        break
    
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 4)
features_poly = poly_object.fit_transform(features_obj)
  

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

x=106
x=np.array(x)
x.reshape(-1,1)
print ("Predicting result with Polynomial Regression")
print (lin_reg_2.predict(poly_object.transform(x)))
 
lin_reg_2.score(features_poly, labels)

x=np.arange(min(features_obj),max(features_obj),0.1)
x=x.reshape(-1,1)
plt.scatter(features_obj, labels, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_object.fit_transform(x)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('brainsize')
plt.ylabel('iq')
plt.show()


















