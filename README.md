# ClusterEnsembles

[![CircleCI](https://circleci.com/gh/tsano430/ClusterEnsembles.svg?style=shield)](https://app.circleci.com/pipelines/github/tsano430/ClusterEnsembles)
[![codecov](https://codecov.io/gh/tsano430/ClusterEnsembles/branch/main/graph/badge.svg?token=CT0WEH2O5T)](https://codecov.io/gh/tsano430/ClusterEnsembles)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package for cluster ensembles. Cluster ensembles generate a single consensus cluster using base clusters obtained from multiple clustering algorithms. The consensus cluster stably achieves a high clustering performance. 

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/60049342/107722358-17c47a00-6d22-11eb-9040-b13b92f97ba1.png">
</p>

Installation
------------

```
pip install ClusterEnsembles
```

Usage
-----

Simple example of cluster ensembles in the reference [1]

```python
>>> import numpy as np

>>> import ClusterEnsembles as CE 

>>> base_cluster1 = np.array([1, 1, 1, 2, 2, 3, 3])

>>> base_cluster2 = np.array([2, 2, 2, 3, 3, 1, 1])

>>> base_cluster3 = np.array([4, 4, 2, 2, 3, 3, 3])

>>> base_cluster4 = np.array([1, 2, np.nan, 1, 2, np.nan, np.nan]) # `np.nan`: missing value

>>> base_clusters = np.array([base_cluster1, base_cluster2, base_cluster3, base_cluster4])

>>> celabel = CE.cluster_ensembles(base_clusters, nclass=3, solver='hbgf')

>>> print(celabel)
[1 1 1 2 2 0 0]
```

- `nclass`: Number of classes in a consensus cluster
- `solver`: {'cspa', 'mcla', 'hbgf', 'nmf', 'all'}
    
    `cspa`: Cluster-based Similarity Partitioning Algorithm [1]

    `mcla`: Meta-CLustering Algorithm [1]
    
    `hbgf`: Hybrid Bipartite Graph Formulation [2]

    `nmf`: NMF-based consensus clustering [4]

    `all`: Use all solvers, and then return the consensus clustering label that gives the smallest objective function value. 

    **Note:** Please use `hbgf` for large-scale `base_clusters`.

Similar Package
---------------

`GGiecold/Cluster_Ensembles`: https://github.com/GGiecold/Cluster_Ensembles

References
----------

[1] A. Strehl and J. Ghosh, 
"Cluster ensembles -- a knowledge reuse framework for combining multiple partitions,"
Journal of Machine Learning Research, vol. 3, pp. 583-617, 2002.

[2] X. Z. Fern and C. E. Brodley, 
"Solving cluster ensemble problems by bipartite graph partitioning,"
In Proceedings of the Twenty-First International Conference on Machine Learning, p. 36, 2004.

[3] J. Ghosh and A. Acharya, 
"Cluster ensembles," 
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, vol. 1, no. 4, pp. 305-315, 2011. 

[4] T. Li, C. Ding, and M. I. Jordan, 
"Solving consensus and semi-supervised clustering problems using nonnegative matrix factorization," 
In Proceedings of the Seventh IEEE International Conference on Data Mining, pp. 577-582, 2007.
