from typing import List
from abs.genericAlgorithm import GenericAlgorithm, AlgorithmResult
from algorithms.nearestNeighbour.implementation import vizinhoMaisProximo
from common.util import getCost
import time


class NearestNeighbourTSP(GenericAlgorithm):

    def execute(self, graph) -> AlgorithmResult:
        initialTime = time.time()
        path = vizinhoMaisProximo(graph)
        executionTime = time.time() - initialTime
        cost = getCost(graph, path)
        return AlgorithmResult(path, cost, executionTime)