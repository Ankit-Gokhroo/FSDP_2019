# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

# Importing dataset
data = pd.read_csv("training_titanic.csv")

# Convert categorical variable to numeric
data["Sex_cleaned"]=np.where(data["Sex"]=="male",0,1)

data["Embarked_cleaned"]=np.where(data["Embarked"]=="S",0,
                                  np.where(data["Embarked"]=="C",1,
                                           np.where(data["Embarked"]=="Q",2,3)
                                          )
                                 )
# Cleaning dataset of NaN
data=data[[
    
    "Fare",
    "Survived"

]].dropna(axis=0, how='any')

"""
data=data[[
    "Survived",
    "Pclass",
    "Sex_cleaned",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_cleaned"
]].dropna(axis=0, how='any')

"""

# Split dataset in training and test datasets
from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(data, test_size=0.5, random_state=0)


gnb = GaussianNB()
used_features =[

    "Pclass",
    "Sex_cleaned",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_cleaned"
   
]

# Train classifier
gnb.fit(
    features_train[used_features].values,
    features_train["Survived"].values
)
labels_pred = gnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(features_test["Survived"], labels_pred)










mnb = MultinomialNB()
used_features =[

    "Pclass",
    "Sex_cleaned",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_cleaned"
   
]

# Train classifier
mnb.fit(
    features_train[used_features].values,
    features_train["Survived"].values
)
labels_pred = mnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_mnb = confusion_matrix(features_test["Survived"], labels_pred)


bnb = BernoulliNB()
used_features =[

    "Pclass",
    "Sex_cleaned",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_cleaned"
   
]

# Train classifier
bnb.fit(
    features_train[used_features].values,
    features_train["Survived"]
)
labels_pred = bnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_bnb = confusion_matrix(features_test["Survived"], labels_pred)
