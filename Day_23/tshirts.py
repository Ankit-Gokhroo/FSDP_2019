# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:14:09 2019

@author: Ankit Gokhroo
"""

"""
Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and 
weight of a customer.

You want to standardize the production on three sizes: small, medium, and large.
 How would you figure out the actual size of these 3 types of shirt to better fit 
 your customers?

Import the tshirts.csv file and perform Clustering on it to make 
sense out of the data as stated above.

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('tshirts.csv')

features = dataset.iloc[:, [1, 2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans


wcss = []
for i in range(1, 6):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 6), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()



# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)


# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates/height')
plt.ylabel('Y Cordinates/weight')
plt.legend()
plt.show()






















