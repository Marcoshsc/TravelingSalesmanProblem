from typing import List, Tuple
import random

def getRandomGraph(vertexes: int, minimumWeight: float, maximumWeight: float) -> List[List[float]]:
    
    if minimumWeight >= maximumWeight:
        raise Exception('Range de valores inválido.')

    matrix: List[List[float]] = [[0 for j in range(vertexes)] for i in range(vertexes)]

    for i in range(vertexes):
        for j in range(i):
            value = random.uniform(minimumWeight, maximumWeight)
            matrix[i][j] = value
            matrix[j][i] = value
    
    return matrix