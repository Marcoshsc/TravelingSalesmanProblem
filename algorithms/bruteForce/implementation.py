from typing import List
from itertools import permutations
from common.util import getCost


def bruteForceTSP(graph: List[List[float]]) -> List[int]:

    size = len(graph)
    minCost = float('inf')
    bestPath = None

    for p in permutations(range(size)):
        path: List[int] = list(p)
        path.append(path[0])
        cost = getCost(graph, path)
        if minCost > cost:
            minCost = cost
            bestPath = path
    
    return bestPath