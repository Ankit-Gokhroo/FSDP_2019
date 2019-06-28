# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:42:31 2019

@author: Ankit Gokhroo
"""

"""
*****
Classification Code Challenge
*****

tree_addhealth.csv

Q1. (Create a program that fulfills the following specification.)

For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set, 
an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina’s Carolina Population Center, 
http://www.cpc.unc.edu/projects/addhealth/data.

 

Import tree_addhealth.csv

 

The attributes are:

 

BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

 

    Build a classification tree model evaluating if an adolescent would smoke regularly or 
    not based on: gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, 
    alcohol use, alcohol problems, marijuana use, cocaine use, inhalant use, availability of cigarettes 
    in the home, depression, and self-esteem.
x=[1,18,1,1,0,0,1,1,1,1,0,1,1,1,40]
    Build a classification tree model evaluation if an adolescent gets expelled or not from school based on their
    Gender and violent behavior.
    Use random forest in relation to regular smokers as a target and explanatory variable specifically 
    with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each and every section)

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('tree_addhealth.csv')

dataset.info()
 
dataset.isnull().any(axis=0)

dataset['age']=dataset['age'].fillna(18)
dataset['ESTEEM1']=dataset['ESTEEM1'].fillna(np.mean(dataset['ESTEEM1']))

features = dataset.loc[:,['BIO_SEX','age','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN','ALCEVR1','ALCPROBS1',
   'marever1','cocever1','inhever1','cigavail','DEP1','ESTEEM1']].values

                         
labels = dataset.loc[:,['TREG1']].values

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

df=pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


score=classifier.score(features_train,labels_train)

x=[1,18,0,1,0,0,1,0,0,1,1,1,1,1,0]
x=[2,28,1,1,0,0,1,1,1,1,0,1,1,1,20]
x=[2,18,0,0,1,0,0,0,0,1,0,0,1,27,35]
x=np.array(x)
x=x.reshape(1,-1)

x= sc.fit_transform(x)
classifier.predict(x)


"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('tree_addhealth.csv')

dataset.info()
 
dataset.isnull().any(axis=0)

dataset['age']=dataset['age'].fillna(18)
dataset['ESTEEM1']=dataset['ESTEEM1'].fillna(np.mean(dataset['ESTEEM1']))

features = dataset.loc[:,['BIO_SEX','age','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN','ALCEVR1','ALCPROBS1',
   'marever1','cocever1','inhever1','cigavail','DEP1','ESTEEM1']].values

labels = dataset.loc[:,['TREG1']].values

# add code to automate the p value removing
import statsmodels.api as sm
import numpy as np

features_obj = features[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
features_obj = sm.add_constant(features_obj)
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else:
        break
features=features_obj     

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

df=pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


score1=classifier.score(features_train,labels_train)

x=[18,1,8,45]
x=np.array(x)
x=x.reshape(1,-1)

x= sc.fit_transform(x)
classifier.predict(x)

"""

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('tree_addhealth.csv')

dataset.info()
 
dataset.isnull().any(axis=0)

dataset['age']=dataset['age'].fillna(18)
dataset['ESTEEM1']=dataset['ESTEEM1'].fillna(np.mean(dataset['ESTEEM1']))

features = dataset.loc[:,['BIO_SEX','age','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN','ALCEVR1','ALCPROBS1',
   'marever1','cocever1','inhever1','cigavail','DEP1','ESTEEM1']].values

labels = dataset.loc[:,['TREG1']].values



from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)



df=pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


score2=classifier.score(features_train,labels_train)

x=[1,18,0,1,0,0,1,0,0,1,1,1,1,1,0]
x=np.array(x)
x=x.reshape(1,-1)

x= sc.fit_transform(x)
classifier.predict(x)

"""















