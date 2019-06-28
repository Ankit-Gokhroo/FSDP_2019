
import pandas as pd

"""
We will look at data regarding coronary heart disease (CHD) in South Africa. 
The goal is to use different variables such as tobacco usage, family history, 
ldl cholesterol levels, alcohol usage, obesity and more.
"""


heart = pd.read_csv('Heart_Disease.csv', sep=',', header=0)  
heart.head()

labels = heart.iloc[:,9].values 
features = heart.iloc[:,:9].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

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

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


#http://vassarstats.net/logreg1.html
