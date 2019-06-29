# -*- coding: utf-8 -*-

"""
https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/
"""

"""
How the Random Forest Algorithm Works
The following are the basic steps involved in performing the random forest algorithm:

Pick N random records from the dataset.
Build a decision tree based on these N records.
Choose the number of trees you want in your algorithm and repeat steps 1 and 2.
In case of a regression problem, for a new record, each tree in the forest predicts a value for Y (output). The final value can be calculated by taking the average of all the values predicted by all the trees in forest. Or, in case of a classification problem, each tree in the forest predicts the category to which the new record belongs. Finally, the new record is assigned to the category that wins the majority vote.
"""

"""
Advantages of using Random Forest
As with any algorithm, there are advantages and disadvantages to using it. In the next two sections we'll take a look at the pros and cons of using random forest for classification and regression.

The random forest algorithm is not biased, since, there are multiple trees and each tree is trained on a subset of data. Basically, the random forest algorithm relies on the power of "the crowd"; therefore the overall biasedness of the algorithm is reduced.
This algorithm is very stable. Even if a new data point is introduced in the dataset the overall algorithm is not affected much since new data may impact one tree, but it is very hard for it to impact all the trees.
The random forest algorithm works well when you have both categorical and numerical features.
The random forest algorithm also works well when data has missing values or it has not been scaled well (although we have performed feature scaling in this article just for the purpose of demonstration).

Disadvantages of using Random Forest
A major disadvantage of random forests lies in their complexity. They required much more computational resources, owing to the large number of decision trees joined together.
Due to their complexity, they require much more time to train than other comparable algorithms.
"""


"""
Part 1: Using Random Forest for Classification
"""

"""
Problem Definition
The task here is to predict whether a bank currency note is authentic or not based on four attributes i.e. variance of the image wavelet transformed image, skewness, entropy, and curtosis of the image.
"""

import pandas as pd

dataset = pd.read_csv("bill_authentication.csv")  

dataset.head()

features = dataset.iloc[:, 0:4].values  
labels = dataset.iloc[:, 4].values 

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test) 

#train the model

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))

#To improve the accuracy, I would suggest you to play around with other parameters of the RandomForestClassifier class and see if you can improve on our results.





#Part 2: Using Random Forest for Regression

"""
Problem Definition
The problem here is to predict the gas consumption (in millions of gallons) in 48 of the US states based on petrol tax (in cents), per capita income (dollars), paved highways (in miles) and the proportion of population with the driving license.
"""

#Import libraries
import pandas as pd  
import numpy as np  

#import database
dataset = pd.read_csv('petrol_consumption.csv') 

#Data Analysis
print dataset.head()

#Preparing the data for training
features = dataset.iloc[:, 0:4].values  
labels = dataset.iloc[:, 4].values  

#Traing test split
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

#feature scaling
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  

#train the model
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

#Evaluating the algorithm
from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))  

print np.mean(labels)

"""
With 20 trees, the root mean squared error is 64.93 which is greater than 10 percent of the average petrol consumption i.e. 576.77. This may indicate, among other things, that we have not used enough estimators (trees).
"""

#Change the number of estimators
regressor = RandomForestRegressor(n_estimators=300, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

#Evaluating the algorithm with 300 trees

print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))  


#############################################

  
