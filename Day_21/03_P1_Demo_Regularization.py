
#https://medium.com/@jayeshbahire/lasso-ridge-and-elastic-net-regularization-4807897cb722

"""
L1 Regularization aka Lasso Regularization– This add regularization terms in the model which are function of absolute value of the coefficients of parameters. The coefficient of the paratmeters can be driven to zero as well during the regularization process. Hence this technique can be used for feature selection and generating more parsimonious model
L2 Regularization aka Ridge Regularization — This add regularization terms in the model which are function of square of coefficients of parameters. Coefficient of parameters can approach to zero but never become zero and hence
Combination of the above two such as Elastic Nets– This add regularization terms in the model which are combination of both L1 and L2 regularization.
"""

"""
Part 01 Discussions
"""

#Import packages

import numpy as np 
import pandas as pd 
import sklearn
import seaborn as sns
from sklearn.preprocessing import StandardScaler
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



#Import dataset and create a dataframe

from sklearn import datasets 
boston = datasets.load_boston ()

#Find out more about this dataset

print(boston.DESCR)

#Boston dataset features
boston.keys() 
boston.data.shape
boston.feature_names
boston.target

#Create a dataframe

boston_df	= pd.DataFrame (boston.data, columns= boston.feature_names )
boston_df.head()

#Add dependent Variable

boston_df['House_Price']= boston.target
boston_df.head ()
boston_df.describe()

features = boston_df.drop('House_Price',axis = 1)
labels = boston_df['House_Price']
features.head()
labels.head()

#Create train and test data with 70o/o and 30°/o split
features_train, features_test, labels_train,labels_test	=	train_test_split(features, labels, test_size=0.3, random_state=1)

features_train.shape

features_test.shape

labels_train.shape
labels_test.shape

#Let's import the Lasso, Ridge, Elasticnet regression object and define model



 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 


#Fit a model on the train data


lm.fit(features_train, labels_train)
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)
lm_elastic.fit(features_train, labels_train)


#Evaluate the model
plt.figure (figsize= (15,10))
ft_importances_lm = pd.Series(lm.coef_, index= features.columns)
ft_importances_lm .plot(kind = 'barh')
plt.show()


#R2 Value

print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (lm .score(features_test,labels_test)*100,2))

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (lm_elastic.score(features_test,labels_test)*100,2))

#Predict on test and training data

predict_test_lm =	lm.predict(features_test ) 
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)
predict_test_elastic = lm_elastic.predict(features_test)

#Print the Loss Funtion - MSE & MAE

import numpy as np
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) )

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))

print ("ElasticNet Mean Square Error (MSE) for TEST data is")
print (np.round (metrics .mean_squared_error(labels_test, predict_test_elastic),2))



"""
The benchmark of random guessing should get you an RMSE = standard_deviation. So lower than this, your model is demonstrating some ability to learn; above that number, you haven't even learned to guess the mean correctly.
"""
