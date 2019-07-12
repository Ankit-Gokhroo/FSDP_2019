
# PCA

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Wine.csv')
features = dataset.iloc[:, 0:13].values
labels = dataset.iloc[:, 13].values

#df_features = pd.DataFrame(features)
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)




# Visualising the Test set results


x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
# Obtain labels for each point in mesh using the model.
# ravel() is equivalent to flatten method.
# data dimension must match training data dimension, hence using ravel
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# Plot the points, we have three labels (1,2,3)
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'ro', label='Class 1')
plt.plot(features_test[labels_test == 2, 0], features_test[labels_test == 2, 1], 'go', label='Class 2')
plt.plot(features_test[labels_test == 3, 0], features_test[labels_test == 3, 1], 'bo', label='Class 3')

#plot the decision boundary
plt.contourf(xx, yy, Z, alpha=.5)

plt.show()


# Dump components relations with features:
df_pca =  pd.DataFrame(pca.components_,columns=df_features.columns,index = ['PC-1','PC-2'])


