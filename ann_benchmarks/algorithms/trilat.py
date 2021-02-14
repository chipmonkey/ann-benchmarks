from __future__ import absolute_import
import sklearn.neighbors
import sklearn.preprocessing
from ann_benchmarks.algorithms.base import BaseANN


class Trilat(BaseANN):
    def __init__(self, metric):
        self._metric = metric
        self.name = 'Trilateration'

    def fit(self, X):
        if self._metric == 'angular':
            X = sklearn.preprocessing.normalize(X, axis=1, norm='l2')
        self._tree = sklearn.neighbors.TrilaterationIndex(X)

    def query(self, v, n):
        if self._metric == 'angular':
            v = sklearn.preprocessing.normalize([v], axis=1, norm='l2')[0]
        dist, ind = self._tree.query([v], k=n)
        return ind[0]


class TrilatApprox(BaseANN):
    def __init__(self, metric):
        self._metric = metric
        self.name = 'TrilaterationApprox'

    def fit(self, X):
        if self._metric == 'angular':
            X = sklearn.preprocessing.normalize(X, axis=1, norm='l2')
        self._tree = sklearn.neighbors.TrilaterationIndex(X)

    def query(self, v, n):
        if self._metric == 'angular':
            v = sklearn.preprocessing.normalize([v], axis=1, norm='l2')[0]
        dist, ind = self._tree.query_expand([v], k=n)
        return ind[0]
