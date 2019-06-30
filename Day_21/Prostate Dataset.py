# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:37:21 2019

@author: Ankit Gokhroo
"""
"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')

dataset.info()
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test) 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 



#making predictions
#To make pre-dictions on the test data, execute the following script:

labels_pred = regressor.predict(features_test) 

#To compare the actual output values for features_test with the predicted values, execute the following script 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print (df) 


#Evaluate the algorithm
"""
1. MAE
2. RMSE
3. MSE
"""

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred))) 
#0.734

score1=regressor.score(features_train,labels_train)
score2=regressor.score(features_test,labels_test)


from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge


lm_lasso = Lasso() 
lm_ridge =  Ridge() 



#Fit a model on the train data

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)
predictlasso=lm_lasso.predict(features_test)
predictridge=lm_ridge.predict(features_test)
#R2 Value

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test,predictlasso ),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predictridge),2))

a=np.mean(dataset['lpsa'])

dataset['lpsa1']=''
for i in dataset['lpsa']:
    if i >a:
        dataset['lpsa1'][dataset['lpsa']==i]='H'
    else:
        dataset['lpsa1'][dataset['lpsa']==i]='L'


cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
cities



dataset=pd.read_csv('PastHires.csv')
dataset['Hired']=dataset['Hired'].replace(to_replace =0, 
                 value ="Y")


















