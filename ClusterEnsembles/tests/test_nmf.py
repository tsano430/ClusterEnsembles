# test_nmf.py


import os
import unittest
import numpy as np
from sklearn.metrics import normalized_mutual_info_score
import ClusterEnsembles as CE


class NMFTest(unittest.TestCase):

    def test_missing(self):
        np.random.seed(0)
        base_clusters = np.array([
            [1, 1, 1, 2, 2, 3, 3],
            [2, 2, 2, 3, 3, 1, 1],
            [4, 4, 2, 2, 3, 3, 3],
            [1, 2, np.nan, 1, 2, np.nan, np.nan]
        ])
        label_true = np.array([1, 1, 1, 2, 2, 3, 3])
        label_pred = CE.cluster_ensembles(base_clusters, solver='nmf')
        nmi_score = normalized_mutual_info_score(label_true, label_pred, average_method='geometric')
        self.assertEqual(1.0, nmi_score)

    def test_performance(self):
        np.random.seed(0)
        base_clusters = np.loadtxt(os.path.dirname(__file__) + '/data/base_clusters.csv', delimiter=',', dtype=int)
        label_true = np.loadtxt(os.path.dirname(__file__) + '/data/label_true.csv', delimiter=',', dtype=int)
        label_pred = CE.cluster_ensembles(base_clusters, solver='nmf')
        nmi_score = normalized_mutual_info_score(label_true, label_pred, average_method='geometric')
        self.assertEqual(1.0, nmi_score)

