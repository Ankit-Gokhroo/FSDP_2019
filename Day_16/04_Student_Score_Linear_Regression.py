# -*- coding: utf-8 -*-

#Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('student_scores.csv')  

#explore the dataset
print (dataset.shape)
print (dataset.ndim)
print (dataset.head())
print (dataset.describe())

#check data types for each column
print (dataset.dtypes)

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)

# Check for outlier values
plt.boxplot(dataset.values)

#let's plot our data points on 2-D graph to eyeball our dataset 
# and see if we can manually find any relationship between the data. 
dataset.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()

#prepare the data to train the model
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

"""
train the model now 
"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)

#what would be prediction of score if someone studies 9 hours
print (regressor.coef_*9 + regressor.intercept_)
print (regressor.predict(9))


#Visualize the best fit line
import matplotlib.pyplot as plt

# Visualising the  results
plt.scatter(features, labels, color = 'red')
plt.plot(features, regressor.predict(features), color = 'blue')
plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
plt.show()


#Now explain the best fit line
# and gradient descent

#and then the train test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 


"""
This means that for every one unit of change in hours studied, the change in the score is about 9.91%. 
"""

#making predictions
#To make pre-dictions on the test data, execute the following script:

labels_pred = regressor.predict(features_test) 

#To compare the actual output values for features_test with the predicted values, execute the following script 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print (df) 


#Now explain the random state by pring features_test with and without random state set


# DO NOT TAKE THIS EXAMPLE TODAY

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

print (np.mean(dataset.values[:,1]))
#You can see that the value of root mean squared error is 4.64, which is less than 10% of the mean value of the percentages of all the students i.e. 51.48. This means that our algorithm did a decent job.



#Visualize the best fit line
import matplotlib.pyplot as plt

# Visualising the Test set results
plt.scatter(features_test, labels_test, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
plt.show()


#http://setosa.io/ev/ordinary-least-squares-regression/
# https://medium.com/@ml.at.berkeley/machine-learning-crash-course-part-1-9377322b3042

#Show the animation using learning rate, cost functions and best fit line
#https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9





#Model accuracy
print (regressor.score(features_test, labels_test))
print (regressor.score(features_train, labels_train))

# Now lets talk about two terms - overfitting and underfitting the data
# best reference available is 
# https://medium.com/towards-data-science/train-test-split-and-cross-validation-in-python-80b61beca4b6


# Do we have case of underfitting?
# Do we have case of overfitting?


"""
If the training score is POOR and test score is POOR then its underfitting

If the training score is GOOD and test score is POOR then its overfitting
"""


# Explain the logic of Best Teacher 100 question story


"""
# Underfitting = no padai

It means that the model does not fit the training data and therefore misses 
the trends in the data
this is usually the result of a very simple model (not enough predictors/independent variables).
"""
 


"""
# Overfitting = ratoo tota

This model will be very accurate on the training data but will probably be very 
not accurate on untrained or new data

This usually happens when the model is too complex (i.e. too many features/variables 
compared to the number of observations). 

It is because this model is not generalized 
Basically, when this happens, the model learns or describes the “noise” in the 
training data instead of the actual relationships between variables in the data.

"""



"""
Solution to Underfitting
    Increase Training Data
    Change the Model from simpler to Complex 
    

Solution to Overfitting
 There are two types of regularization as follows:

    L1 Regularization or Lasso Regularization
    L2 Regularization or Ridge Regularization
    Elastic Net is hybrid of both L1 and L2
"""
