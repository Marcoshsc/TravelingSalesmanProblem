from typing import List
from itertools import permutations


def bruteForceTSP(graph: List[List[float]]) -> List[int]:

    size = len(graph)
    minCost = float('inf')
    bestPath = None

    for p in permutations(range(size)):
        path: List[int] = list(p)
        path.append(path[0])
        cost = 0
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]
        if minCost > cost:
            minCost = cost
            bestPath = path
    
    return bestPath