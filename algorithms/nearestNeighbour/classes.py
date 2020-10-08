from typing import List
from abs.genericAlgorithm import GenericAlgorithm, AlgorithmResult
from algorithms.nearestNeighbour.implementation import vizinhoMaisProximo
from common.util import getCost
from common.timer import executeWithTimeOut
import time


class NearestNeighbourTSP(GenericAlgorithm):

    def execute(self, graph) -> AlgorithmResult:
        initialTime = time.time()
        path = executeWithTimeOut(vizinhoMaisProximo, graph)
        executionTime = time.time() - initialTime
        cost = getCost(graph, path)
        return AlgorithmResult(path, cost, executionTime)