from typing import Tuple
from abs.algorithmFactory import AlgorithmFactory
from abs.enumerator import EnumAlgorithms
from common.randomic import getRandomGraph
import time

def getExecutionTime(data: dict) -> Tuple[float, float]:

    randomGraph: List[List[float]] = getRandomGraph(data['vertex'], data['min'], data['max'])
    factory = AlgorithmFactory()
    bruteForce = factory.getAlgorithm(EnumAlgorithms.BRUTE_FORCE)
    nearestNeighbour = factory.getAlgorithm(EnumAlgorithms.NEAREST_NEIGHBOUR)

    bruteForceResult = bruteForce.execute(randomGraph)

    nearestNeighbourResult = nearestNeighbour.execute(randomGraph)

    bruteForceExecutionTime = bruteForceResult.executionTime if bruteForceResult.executionTime is not None else float('inf')
    nearestNeighbourExecutionTime = nearestNeighbourResult.executionTime if nearestNeighbourResult.executionTime is not None else float('inf')

    return (bruteForceExecutionTime, nearestNeighbourExecutionTime)