
# Multiple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Classification.csv')
#temp = dataset.values

#dataset= dataset.get_dummies(dataset)
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)


#check data types for each column
print (dataset.dtypes)


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

"""
With linear regression, or generalized linear models 
estimated by maximum likelihood (or least squares) 
you need to leave out one column. 
Otherwise you will get a message about some 
columns "left out because of singularities".

But if you estimate such models with regularization, 
for example ridge, lasso er the elastic net, 
then you should not leave out any columns. 
The regularization takes care of the singularities, 
and more important, the prediction obtained 
may depend on which columns you leave out. 
That will not happen when you do not use regularization.
"""

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
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
# Development is replaced by 1,0,0 to 0,0 to remove dummy trap

import numpy as np
x = [0,0, 1500, 1, 2]
x = np.array(x)
x = x.reshape(1,5)
regressor.predict(x)



le = labelencoder.transform(['Development'])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],1100,1,3]
x = np.array(x)


regressor.predict(x.reshape(1, -1))


# Getting Score for the Multi Linear Reg model
Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)


"""
Evaluating the Algorithm
The final step is to evaluate the performance of algorithm. We'll do this by finding the values for MAE, MSE and RMSE. Execute the following script:
"""
from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, Pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, Pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, Pred)))  

print (np.mean(labels))
"""
You can see that the value of root mean squared error is 4379.8, which is lower than 10% of the mean value of the salaries (760038x10/100 = 7600). This means that our algorithm was not very accurate but can still make reasonably good predictions.

There are many factors that may have contributed to this inaccuracy, a few of which are listed here:

Need more data: Only one year worth of data isn't that much, whereas having multiple years worth could have helped us improve the accuracy quite a bit.
Bad assumptions: We made the assumption that this data has a linear relationship, but that might not be the case. Visualizing the data may help you determine that.
Poor features: The features we used may not have had a high enough correlation to the values we were trying to predict.
"""

"""
What is multiple regression?
//same as simple regression but multiple independent variables

//Assumptions of linear regression - do not blindly follow but check if the given problem is linear regression problem

// In above problem, profit is our dependent variables and others are independent variables

//but state (location) is a categorical variable and we need to handle this.
//For this you need to create dummy variables
//Dummy variables trap ( include one less dummy variables in predictor)
// Whenever you are building a model, always omit one dummy variables.
// So beware of dummy variable trap
//Show the image (dummy variable trap)
// Now lets start buidling a the model

// Some times you have to miss some of independent variable for model buidling (elimination) [selecting the right variables)
// All possible methods are given below
1. All in
2. Backward elimination
3. Forward selection
4. Bidirection elimination
5. Score comparison

"""
"""
About one hot encoding

Most of the machine learning algorithms such as linear regression, logistic regression, neural network, support vector machine works better with numerical features.

Quantitative features come with a numerical value and they can be directly used (Sometimes data preprocessing, normalization may have to use) as the input features of ML algorithms.

Ordinal features can be easily represented in numbers (Ex. First = 1, Second = 2, Third = 3 …). This is called Integer Encoding. Representing ordinal features using numbers makes sense because the dependency between each representation can be notated in a numerical way.

There are some algorithms that can directly deal with joint discrete distribution such as Markov chain / Naive Bayes / Bayesian network, tree based, etc. These algorithms can work with categorical data without any encoding; while we should encode the categorical features in a way to represent in a numerically to use as the input features for other ML algorithms. That means it’s better to change the categorical features to numerical most of the times 
"""

#https://stackoverflow.com/questions/24458645/label-encoding-across-multiple-columns-in-scikit-learn
