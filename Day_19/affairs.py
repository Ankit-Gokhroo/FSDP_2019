# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:55:00 2019

@author: Ankit Gokhroo
"""
"""
Q1. (Create a program that fulfills the following specification.)
affairs.csv


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 
5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!

    What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)

    Predict the probability of an affair for a random woman not present in the dataset. She's a 25
    -year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as s
    trongly religious, rates her marriage as fair, and her husband is a farmer.

Optional
x=[4,25,3,1,4,16,4,2]
    Build an optimum model, observe all the coefficients.


--------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('affairs.csv')

dataset.info()
 
features = dataset.iloc[:, 0:8].values
labels = dataset.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()
"""
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6])
features = onehotencoder.fit_transform(features).toarray()
features = features[:,1:]
onehotencoder1 = OneHotEncoder(categorical_features = [7])
features = onehotencoder.fit_transform(features).toarray()
"""
dataset['occupation'].value_counts()
dataset['occupation_husb'].value_counts()


from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


score=classifier.score(features_train,labels_train)


x=[4,25,3,1,4,16,4,2]
x=np.array(x)
x = x.reshape(1,-1)
x= onehotencoder.transform(x).toarray()
classifier.predict(x)

# What percentage of total women actually had an affair?
(dataset["affair"]==1).value_counts(normalize=True)*100

dataset['affair'].value_counts()





