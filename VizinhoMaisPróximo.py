def vizinho_mais_proximo(G,s):
    u = s
    C = []
    tam = len(G)
    Q = []
    v = 1

    for i in range(tam):
        Q.append(i)
    Q.remove(u)
    print(Q)

    while (Q!=0):
        menor = 99999999
        continua = False
        for i in range(tam):
            if (G[u][i] != 0 and G[u][i] < menor and Q.count(i) != 0):
                menor = G[u][i]
                v = i
                print(v)
                continua = True
        if continua:
            C.append((u,v))
            Q.remove(v)
            u = v
        else:
            break

    C.append((u,s))
    print(C)

grafo = [[0,1,2,5],[1,0,3,0],[2,3,0,4],[5,0,4,0]]
vizinho_mais_proximo(grafo,0)



        