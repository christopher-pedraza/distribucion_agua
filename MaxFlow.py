from collections import deque
from copy import deepcopy


def bfs(grafo, nodo_fuente, nodo_destino):
    q = deque()
    q.append(nodo_fuente)
    visitado = {i: False for i in grafo}
    capacidades = {i: float("inf") for i in grafo}
    predecesor = {i: None for i in grafo}

    while q:
        nodo = q.popleft()
        for vecino in grafo[nodo]["vecinos"]:
            if vecino["capacidad"] > 0 and not visitado[vecino["id"]]:
                capacidades[vecino["id"]] = vecino["capacidad"]
                visitado[vecino["id"]] = True
                predecesor[vecino["id"]] = nodo
                q.append(vecino["id"])

    path = []
    flujo = float("inf")
    i = nodo_destino
    while i != nodo_fuente:
        path.append(i)
        flujo = min(flujo, capacidades[i])
        if not predecesor[i]:
            break
        i = predecesor[i]

    if len(path) > 1:
        path.append(nodo_fuente)
        path.reverse()

        return path, flujo
    else:
        return None, None


def max_flow(grafo, nodo_destino):
    flujos_maximos = {}

    for nodo in grafo:
        if grafo[nodo]["fuente"]:
            flujo_maximo = 0
            R = deepcopy(grafo)

            path, bottleneck = bfs(R, nodo, nodo_destino)
            while path:
                print(path)
                for i in range(len(path) - 1):
                    u = path[i]
                    v = path[i + 1]

                    # Actualizar capacidades en el grafo residual
                    for vecino in R[u]["vecinos"]:
                        if vecino["id"] == v:
                            vecino["capacidad"] -= bottleneck
                            break
                    for vecino in R[v]["vecinos"]:
                        if vecino["id"] == u:
                            vecino["capacidad"] += bottleneck
                            break

                flujo_maximo += bottleneck
                path, bottleneck = bfs(R, nodo, nodo_destino)

            flujos_maximos[nodo] = flujo_maximo
    return flujos_maximos
