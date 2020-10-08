from typing import List


def vizinhoMaisProximo(G: List[List[float]], s: int) -> List[int]:
    u = s
    C: List[int] = [s]
    tam = len(G)
    Q: List[int] = []
    v = None

    for i in range(tam):
        Q.append(i)
    Q.remove(u)

    while (Q!=0):
        menor = float('inf')
        continua = False
        for i in range(tam):
            if G[u][i] != 0 and G[u][i] < menor and Q.count(i) != 0:
                menor = G[u][i]
                v = i
                continua = True
        if continua:
            C.append(v)
            Q.remove(v)
            u = v
        else:
            break

    C.append(s)
    return C
        