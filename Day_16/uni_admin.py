# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:05:05 2019

@author: Ankit Gokhroo
"""

"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

df=pd.read_csv('University_data.csv')

df.describe()
df.info()

df['Univercity Name'].value_counts()

df.isnull().any(axis=0)

#dataset= dataset.get_dummies(dataset)
features = df.iloc[:, :-1].values
labels = df.iloc[:, -1].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)


# Predicting the Test set results
Pred = regressor.predict(features_test)

import pandas as pd

print (pd.DataFrame(Pred, labels_test))


# Prediction for a new values 
# make this accorifng to the data csv


import numpy as np
x = [1,0,0,0,320,4,4.5,8,1]
x = np.array(x)
x = x.reshape(1,9)
regressor.predict(x)



le = labelencoder.transform([''])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],ohe[0][3],ohe[0][4],320,4,4.5,8,1]
x = np.array(x)


regressor.predict(x.reshape(1, -1))


# Getting Score for the Multi Linear Reg model
Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)


























