
# Multiple Linear Regression

# Importing the libraries

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Classification.csv')
#temp = dataset.values
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

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


# Building the optimal model using Backward Elimination

#import statsmodels.formula.api as sm
#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)

#adds a constant column to input data set.
import statsmodels.api as sm
features = sm.add_constant(features)

"""
Unlike SKLearn, statsmodels doesn’t automatically 
fit a constant, so you need to use the method 
sm.add_constant(features) in order to add a constant. 
Adding a constant, while not necessary, 
makes your line fit much better. 
For example, if you have a line with an intercept of 
-2000 and you try to fit the same line through the 
origin, you’re going to get an inferior line. 
Once we add a constant (or an intercept if you’re 
thinking in line terms), you’ll see that the 
coefficients are the same in SKLearn and statsmodels.
"""





features_opt = features[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
#regressor_OLS.pvalues




features_opt = features[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
#regressor_OLS.pvalues




features_opt = features[:, [0, 1, 3, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()




features_opt = features[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()



features_opt = features[:, [0, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
print (regressor_OLS.summary())


# add code to automate the p value removing
import statsmodels.api as sm
import numpy as np

features_obj = features[:, [0,1,2,3,4]]
features_obj = sm.add_constant(features_obj)
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else:
        break
    


"""
Few comments about OLS for dummy variable values

Case Study
Suppose you are building a linear (or logistic) regression 
model. In your independent variables list, you have a 
categorical variable with 4 categories (or levels). 
You created 3 dummy variables (k-1 categories) and 
set one of the category as a reference category. 
Then you run stepwise / backward/ forward regression 
technique and you found only one of the category coming 
out statistically significant based on p-value and the 
remaining 3 categories are insignificant. 
The question arises - should we remove or keep these 3 
categories having insignificant difference? should we 
include the whole categorical variable or not?

Solution
In short, the answer is we can ONLY choose whether we 
should use this independent categorical variable as a 
whole or not. In other words, we should only see whether 
the categorical variable as a whole is significant or not. 
We cannot include some categories of a variable and exclude 
some categories having insignificant difference.

Ref: https://www.listendata.com/2016/07/insignificant-levels-of-categorical-variable.html
"""



"""
In most of the cases library takes care of dummy variable trap and feature scaling as well.
//Explain the sample code

// Compare the prediction with actual data points.

// Now how you can improve the model?
//By checking which independent variables has highest impact?
// For this we use method  called backward elimination
// Explain the backward elimination
//Steps
1. Start with all the predictors in the model
2. Remove the predictor with highest p-value greater than 5%
3. Refit the model and goto 2
4. Stop when all p-values are less than 5%.

// Need to use library for this (import stats_models.formula.api as sm)

//Using this libarary, we remove predictors(independent variables) iteratively by looking at p value (remove if p is more than 5%)

// Most important

https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/


"""