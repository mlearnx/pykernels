import numpy as np
import unittest
from pykernels.utils import floyd_warshall

class TestFloydWarshall(unittest.TestCase):
    # TODO(kasiajanocha): add test cases
    def setUp(self):
        t = np.ones((100,100))
        np.fill_diagonal(t, 0)
        self.datasets = [np.array([[1,1],[1,1]]),
                         np.ones((100,100))]
        self.results = [np.array([[0,1],[1,0]]),
                        t]

    def tearDown(self):
        pass

    def test_fw(self):
        for i, g in enumerate(self.datasets):
            self.assertTrue((floyd_warshall(g,g) == self.results[i]).all())