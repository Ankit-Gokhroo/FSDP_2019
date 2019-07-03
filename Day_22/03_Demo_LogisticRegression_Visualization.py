

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:39:40 2018

@author: Kunal
"""

# Logistic Regression ( Classification)


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


#version 4 for decision boundary
#http://yooooh.net/2016/02/11/plot-classification-decision-boundary/

# Step size of the mesh. Decrease to increase the quality of the VQ.
#h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].    

# Plot the decision boundary. For that, we will assign a color to each
   
"""
The purpose of meshgrid function in Python is to create a rectangular grid out of an array of x values and an array of y values. Suppose you want to create a grid where you have a point at each integer value between 0 and 4 in both the x and y directions.
"""

x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))
# Obtain labels for each point in mesh using the model.
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the points
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'bo', label='Class 2')
plt.plot(features_test[labels_test == 0, 0], features_test[labels_test == 0, 1], 'ro', label='Class 1')

plt.contourf(xx, yy, Z, alpha=0.3)
plt.show()



# -*- coding: utf-8 -*-
"""
The Iris flower data set or Fisher's Iris data set is a multivariate
data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper
The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.
"""
#We import this dataset already in sklearn, and perform logisitic regression based on petals and sepals properties to classify the iris species
from sklearn.datasets import load_iris

iris = load_iris() # Loading Iris Dataset
print iris.feature_names  # Column Names for the iris dataset

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(iris.data, iris.target, test_size = 0.25, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
logClassifier = LogisticRegression(random_state=0)
logClassifier.fit(features_train, labels_train)

# Printing Score for the Regression Model
print logClassifier.score(features_train,labels_train)

# Predicting the Test set results for first item in the test set
labels_pred = logClassifier.predict(features_test[0].reshape(1,-1))
print labels_pred

# Predicting the Test set results for the entire test set
labels_pred = logClassifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

#Why we are not able to visualize the data, as the data is not two dimensional


