# test_hbgf.py


import unittest
import numpy as np
from sklearn.metrics import normalized_mutual_info_score
import ClusterEnsembles as CE


class HBGFTest(unittest.TestCase):

    def test_hbgf(self):
        base_clusters = np.array([
            [1, 1, 1, 2, 2, 3, 3],
            [2, 2, 2, 3, 3, 1, 1],
            [4, 4, 2, 2, 3, 3, 3],
            [1, 2, np.nan, 1, 2, np.nan, np.nan]
        ])
        label_true = np.array([1, 1, 1, 2, 2, 3, 3])
        label_pred = CE.cluster_ensembles(base_clusters, solver='hbgf')
        nmi_score = normalized_mutual_info_score(label_true, label_pred, average_method='geometric')
        self.assertEqual(1.0, nmi_score)
