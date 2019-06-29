# -*- coding: utf-8 -*-

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#DT for classfication
"""
Data Set Information:

Data were extracted from images that were taken from 
genuine and forged banknote-like specimens. 
For digitization, an industrial camera usually used for 
print inspection was used. The final images have 400x 400 
pixels. Due to the object lens and distance to the 
investigated object gray-scale pictures with a 
resolution of about 660 dpi were gained. 
Wavelet Transform tool were used to extract 
features from images.

"""

dataset = pd.read_csv("bill_authentication.csv")  

#data analysis

dataset.shape
dataset.head()

#Preparing the dataset

features = dataset.drop('Class', axis=1)  
labels = dataset['Class']  

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

"""
from sklearn import tree
#tree.plot_tree(classifier) #works with version 0.21.1


#to run below code: pip install graphviz
import graphviz 
dot_data = tree.export_graphviz(classifier, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("decision_tree") 
"""


#-------------------------------------------#
#DT for Regression

import pandas as pd

dataset = pd.read_csv('petrol_consumption.csv')  

dataset.head()

features = dataset.drop('Petrol_Consumption', axis=1)  
labels = dataset['Petrol_Consumption'] 

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  


"""
from sklearn import tree
#tree.plot_tree(regressor)  #works with version 0.21.1

#to run below code: pip install graphviz
import graphviz
dot_data = tree.export_graphviz(regressor, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("decision_tree") 



"""








#classification
#from sklearn.metrics import classification_report
#print(classification_report(labels_test, labels_pred))


#Evaluation
#To evaluate performance of the regression algorithm, the commonly used metrics are mean absolute error, mean squared error, and root mean squared error.
from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred))) 

"""
The mean absolute error for our algorithm is 54.7, which is less than 10 percent of the mean of all the values in the 'Petrol_Consumption' column. This means that our algorithm did a fine prediction job.
"""



