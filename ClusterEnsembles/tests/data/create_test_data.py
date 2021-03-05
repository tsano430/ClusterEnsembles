# create_test_data.py

import numpy as np
from sklearn.cluster import KMeans

np.random.seed(0)

locs = [-9.0, -4.5, 0, 4.5, 9.0]
for i, loc in enumerate(locs):
    normal = np.random.normal(loc=loc, scale=1.0, size=1600).reshape(200, 8)
    if i == 0:
        normals = normal
    else:
        normals = np.vstack((normals, normal))
normals = normals[np.random.permutation(np.arange(normals.shape[0])), :]

kmeans = KMeans(n_clusters=5)
bcs = []
for i in range(8//2):
    bc = kmeans.fit(normals[:, 2*i:2*(i+1)]).labels_
    bcs.append(bc)
base_clusters = np.array(bcs)

label_true = base_clusters[0]
base_clusters = base_clusters[1:]

np.savetxt('label_true.csv', label_true.reshape(1, len(label_true)), delimiter=',', fmt='%d')
np.savetxt('base_clusters.csv', base_clusters, delimiter=',', fmt='%d')
