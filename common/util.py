from typing import List

def getCost(graph: List[List[float]], path: List[int]) -> float:

    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    return cost