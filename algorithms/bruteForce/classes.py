from typing import List
from abs.genericAlgorithm import GenericAlgorithm, AlgorithmResult
from algorithms.bruteForce.implementation import bruteForceTSP
from common.util import getCost
import time

class BruteForceTSP(GenericAlgorithm):

    def execute(self, graph) -> AlgorithmResult:
        initialTime = time.time()
        path = bruteForceTSP(graph)
        executionTime = time.time() - initialTime
        cost = getCost(graph, path)
        return AlgorithmResult(path, cost, executionTime)