# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:22:23 2019

@author: Ankit Gokhroo
"""

"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. 
The researchers (Cook and Weisberg, 1999) measured and 
recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? 
    Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking 
into account a quadratic function of the age of the fish.

"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('bluegills.csv')
df.info()

features = df.iloc[:,0:1].values
labels = df.iloc[:, 1:].values

plt.scatter(features,labels)

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)



print ("Predicting result with Linear Regression")
print (lin_reg_1.predict(5))

# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('age')
plt.ylabel('length')
plt.show()


# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
 
print ("Predicting result with Polynomial Regression")
print (lin_reg_2.predict(poly_object.transform(5)))

# Visualising the Polynomial Regression results
x=np.arange(min(features),max(features),0.1)
x=x.reshape(-1,1)
plt.scatter(features, labels, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_object.fit_transform(x)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('age')
plt.ylabel('length')
plt.show()


lin_reg_1.score(features, labels)
lin_reg_2.score(features_poly, labels)














