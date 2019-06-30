

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

# Predicting the Test set results
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


#check the model performances now

#Accuracy

from sklearn.metrics import accuracy_score 
 
print (accuracy_score(labels_test, labels_pred)) #can be calcuated from cm as well

#precision Score/
"""
given that the classifier predicted a sample as positive, 
what’s the probability of the sample being indeed positive?
"""
from sklearn.metrics import precision_score
#https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall
 
# Take turns considering the positive class either 0 or 1
print (precision_score(labels_test, labels_pred, pos_label=0)  )
print (precision_score(labels_test, labels_pred, pos_label=1)  )


#Recall Score/Sensitivity
"""
given a positive sample, what is the probability that our system will properly 
identify it as positive?
"""
from sklearn.metrics import recall_score
#https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall
 
# Take turns considering the positive class either 0 or 1
print (recall_score(labels_test, labels_pred, pos_label=0)  )
print (recall_score(labels_test, labels_pred, pos_label=1)  )

#f1 Score
"""
A measure that combines the precision and recall metrics is called F1-score. 
This score is, in fact, the harmonic mean of the precision and the recall. 
Here’s the formula for it:
2 / (1 / Precision + 1 / Recall)
"""
from sklearn.metrics import f1_score
#https://en.wikipedia.org/wiki/F1_score
 
# Take turns considering the positive class either 0 or 1
print (f1_score(labels_test, labels_pred, pos_label=0)  )
print (f1_score(labels_test, labels_pred, pos_label=1)  )

"""
A convenient shortcut in scikit-learn for obtaining a readable digest of all the metrics is metrics.classification_report
"""
from sklearn.metrics import classification_report

print (classification_report(labels_test, labels_pred, target_names=['NO', 'YES']))

#The support is the number of samples of the true response that lie in that class.

















"""

Later on: needs some rework

"""





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

#Classification Metric
"""
Following are the types of Classification Metrics :

    Confusion Matrix
    Classification Matrix
    F1 Score
    Area under ROC curve
    Classification Report
    Logarithmic Loss
"""

"""
https://medium.com/usf-msds/choosing-the-right-metric-for-machine-learning-models-part-1-a99d7d7414e4
https://medium.com/usf-msds/choosing-the-right-metric-for-evaluating-machine-learning-models-part-2-86d5649a5428
"""
from sklearn import metrics
fpr, tpr, _ = metrics.roc_curve(labels_test,  labels_pred_proba[:,1])
auc = metrics.roc_auc_score(labels_test, labels_pred_proba[:,1])
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()

"""
https://nlpforhackers.io/classification-performance-metrics/
"""

"""
positive – we predict the disease is present
negative – we predict the disease is not present.
Let’s now define some notations:

TP – True Positives (Samples the classifier has correctly classified as positives)
TN – True Negatives (Samples the classifier has correctly classified as negatives)
FP – False Positives (Samples the classifier has incorrectly classified as positives)
FN – False Negatives (Samples the classifier has incorrectly classified as negatives)
"""

"""
Recall or Sensitivity or TPR (True Positive Rate): Number of items correctly identified as positive out of total true positives- TP/(TP+FN)
Specificity or TNR (True Negative Rate): Number of items correctly identified as negative out of total negatives- TN/(TN+FP)
Precision: Number of items correctly identified as positive out of total items identified as positive- TP/(TP+FP)
False Positive Rate or Type I Error: Number of items wrongly identified as positive out of total true negatives- FP/(FP+TN)
False Negative Rate or Type II Error: Number of items wrongly identified as negative out of total true positives- FN/(FN+TP)
"""
#Accuracy

from sklearn.metrics import accuracy_score
 
print accuracy_score(labels_test, labels_pred)

#precision Score/
"""
given that the classifier predicted a sample as positive, what’s the probability of the sample being indeed positive?
"""
from sklearn.metrics import precision_score
 
# Take turns considering the positive class either 0 or 1
print precision_score(labels_test, labels_pred, pos_label=0)  
print precision_score(labels_test, labels_pred, pos_label=1)  


#Recall Score/Sensitivity
"""
given a positive sample, what is the probability that our system will properly identify it as positive?
"""
from sklearn.metrics import recall_score
 
# Take turns considering the positive class either 0 or 1
print recall_score(labels_test, labels_pred, pos_label=0)  
print recall_score(labels_test, labels_pred, pos_label=1)  

#f1 Score
"""
A measure that combines the precision and recall metrics is called F1-score. This score is, in fact, the harmonic mean of the precision and the recall. Here’s the formula for it:
2 / (1 / Precision + 1 / Recall)
"""
from sklearn.metrics import f1_score
 
# Take turns considering the positive class either 0 or 1
print f1_score(labels_test, labels_pred, pos_label=0)  
print f1_score(labels_test, labels_pred, pos_label=1)  

"""
A convenient shortcut in scikit-learn for obtaining a readable digest of all the metrics is metrics.classification_report
"""

from sklearn.metrics import classification_report

print classification_report(labels_test, labels_pred, target_names=['NO', 'YES'])

#The support is the number of samples of the true response that lie in that class.














#################
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, roc_auc_score



false_positive_rate, true_positive_rate, thresholds = roc_curve(labels_test, classifier.predict(features_test))
print auc(false_positive_rate, true_positive_rate)
# 0.857142857143
print roc_auc_score(labels_test, classifier.predict(features_test))
# 0.857142857143


"""
http://vision.stanford.edu/teaching/cs231n-demos/linear-classify/
"""
"""
