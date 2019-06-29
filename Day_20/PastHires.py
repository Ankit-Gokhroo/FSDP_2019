# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:43:14 2019

@author: Ankit Gokhroo
"""
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on 
certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction 
    is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, 
    went to top-tire school, having Bachelor's Degree without Internship.
    
    
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, 
    didn't went to any top-tire school, having Master's Degree with Internship.
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset=pd.read_csv('PastHires.csv')
dataset['Hired']=dataset['Hired'].replace(to_replace =0, 
                 value ="Y")

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,1] = labelencoder.fit_transform(features[:,1])

labelencoder1 = LabelEncoder()
features[:,3] = labelencoder1.fit_transform(features[:,3])

labelencoder2 = LabelEncoder()
features[:,4] = labelencoder2.fit_transform(features[:,4])

labelencoder3 = LabelEncoder()
features[:,5] = labelencoder3.fit_transform(features[:,5])

features=features.astype(float) 


labels=labels.reshape(13,1)
labelencoder4 = LabelEncoder()
labels[:,0] = labelencoder4.fit_transform(labels[:,0])

labels=labels.astype(float)


from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features, labels)

labels_pred = classifier.predict(features) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels, labels_pred))  

score=classifier.score(features,labels)


from sklearn.ensemble import RandomForestClassifier

classifier1 = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier1.fit(features, labels)  
labels_pred1 = classifier1.predict(features)

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels,labels_pred))  

score1=classifier1.score(features,labels)


x=[10,'Y',4,'MS','Y','Y']

x=np.array(x)
x=x.reshape(1,-1)
x[:,1] = labelencoder.transform(x[:,1])
x[:,3] = labelencoder1.transform(x[:,3])
x[:,4] = labelencoder2.transform(x[:,4])
x[:,5] = labelencoder3.transform(x[:,5])

classifier1.predict(x)











