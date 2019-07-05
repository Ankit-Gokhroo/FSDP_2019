# K-Means Clustering
"""
Use Cases
K-Means is widely used for many applications.

Image Segmentation
Clustering Gene Segementation Data
News Article Clustering
Clustering Languages
Species Clustering
Anomaly Detection
"""



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('xclara.csv')
features = dataset.iloc[:, [0, 1]].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()



# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)



# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()



#Silhouette Score calculation to find optimal number of clusters
"""
The Silhouette Coefficient is defined for each sample and is composed of two scores:

a: The mean distance between a sample and all other points in the same class.
b: The mean distance between a sample and all other points in the next nearest cluster.
The Silhouette Coefficient s for a single sample is then given as:

score = (b - a)/max(a, b)
"""

from sklearn.metrics import silhouette_score

for n_clusters in range(2, 11):
    clusterer = KMeans (n_clusters=n_clusters)
    preds = clusterer.fit_predict(features)
    centers = clusterer.cluster_centers_

    score = silhouette_score (features, preds, metric='euclidean')
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", score)
#WIth above values, we can clearly see that the optimal cluster values are 3


#Note that Silhouette Coefficient is only defined if number of labels is 2 <= n_labels <= n_samples - 1
#silhouette_score requires more than 1 cluster labels
#So if you call the silhouette score method for jsut one cluster, it gives error
"""
2.3.9.5.1. Advantages of Silhouette Score
The score is bounded between -1 for incorrect clustering and +1 for highly dense clustering. Scores around zero indicate overlapping clusters.
The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.
2.3.9.5.2. Drawbacks
The Silhouette Coefficient is generally higher for convex clusters than other concepts of clusters, such as density based clusters like those obtained through DBSCAN.
"""


"""
Measuring Performance of K-means
Homogeneity and Completeness – If you have pre-existing class labels that you’re trying to duplicate with k-means clustering, you can use two measures: homogeneity and completeness.

Homogeneity means all of the observations with the same class label are in the same cluster.
Completeness means all members of the same class are in the same cluster.
Scikit-Learn (Python) has an excellent write-up on these two measures.

"""
#We can turn those concept as scores homogeneity_score and completeness_score. Both are bounded below by 0.0 and above by 1.0 (higher is better):

from sklearn import metrics

labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [0, 0, 1, 1, 2, 2]

metrics.homogeneity_score(labels_true, labels_pred)  


metrics.completeness_score(labels_true, labels_pred) 

#Their harmonic mean called V-measure is computed by v_measure_score
metrics.v_measure_score(labels_true, labels_pred) 

#All calculated together
metrics.homogeneity_completeness_v_measure(labels_true, labels_pred)



#https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation

#http://www.learnbymarketing.com/methods/k-means-clustering/

