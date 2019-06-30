# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:40:59 2019

@author: Ankit Gokhroo
"""
"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset=pd.read_csv('kc_house_data.csv')

dataset.info()

dataset['sqft_above']=dataset['sqft_above'].fillna(np.mean(dataset['sqft_above']))

dataset.isnull().any(axis=0)

features = dataset.iloc[:,3:].values
labels = dataset.iloc[:,2].values

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

labels_pred = regressor.predict(features_test) 

#To compare the actual output values for features_test with the predicted values, execute the following script 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print (df) 

"""
1. MAE
2. RMSE
3. MSE
"""

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred))) 


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





score3=lm_lasso.score(features_train,labels_train)
scpre4=lm_ridge.score(features_test,labels_test)







