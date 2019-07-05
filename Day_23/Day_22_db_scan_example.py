#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:46:29 2019

@author: ajoyfern
"""

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


# #############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
features, labels = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

features = StandardScaler().fit_transform(features)

# #############################################################################
# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(features)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
labels_pred = db.labels_



# #############################################################################
# Plot result
import matplotlib.pyplot as plt


plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+' )
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o' )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s' )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*' )


#measure the performance of the dbscan

"""
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))

"""


#http://www.sthda.com/english/wiki/print.php?id=246
