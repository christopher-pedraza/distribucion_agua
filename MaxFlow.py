from collections import deque
from copy import deepcopy


# Función para encontrar un camino desde el nodo fuente al nodo destino
# Recibe: grafo, nodo fuente, nodo destino
# Retorna: camino, flujo
def bfs(grafo, nodo_fuente, nodo_destino):
    q = deque()
    # Agregar nodo fuente a la cola
    q.append(nodo_fuente)
    visitado = {i: False for i in grafo}
    capacidades = {i: float("inf") for i in grafo}
    predecesor = {i: None for i in grafo}

    # Mientras que la cola no esté vacía
    while q:
        # Sacar el primer elemento de la cola
        nodo = q.popleft()
        # Iterar sobre los vecinos del nodo que salió de la cola
        for vecino in grafo[nodo]["vecinos"]:
            # Si el vecino no ha sido visitado y tiene capacidad
            if vecino["capacidad"] > 0 and not visitado[vecino["id"]]:
                # Actualizar capacidades, predecesores, y visitados
                capacidades[vecino["id"]] = vecino["capacidad"]
                visitado[vecino["id"]] = True
                predecesor[vecino["id"]] = nodo
                # Agregar el vecino a la cola
                q.append(vecino["id"])

    # Reconstruir el camino y encontrar el bottleneck
    path = []
    flujo = float("inf")
    i = nodo_destino
    while i != nodo_fuente:
        path.append(i)
        flujo = min(flujo, capacidades[i])
        if not predecesor[i]:
            break
        i = predecesor[i]

    # Si el camino tiene más de un nodo, agregar el nodo fuente y revertir el camino
    if len(path) > 1:
        path.append(nodo_fuente)
        path.reverse()

        return path, flujo
    # Si no, no hay camino
    else:
        return None, None


# Función para encontrar el flujo máximo desde cada fuente del grafo al nodo más lejano
# en el sector
# Recibe: grafo, nodo destino
# Regresa: diccionario con el flujo máximo desde cada fuente al nodo destino, al igual que
# el uso de capacidad de cada tubería
def max_flow(grafo, nodo_destino):
    flujos_maximos = {}

    for nodo in grafo:
        # Si el nodo es una fuente y está en el mismo sector que el nodo destino, se calcula
        # el flujo máximo desde este nodo fuente al nodo destino
        if (
            grafo[nodo]["fuente"]
            and grafo[nodo]["sector"] == grafo[nodo_destino]["sector"]
        ):
            flujo_maximo = 0
            R = deepcopy(grafo)

            usos = {}

            # Encontrar el camino más corto desde el nodo fuente al nodo destino
            # Si path regresa None, no hay camino y se termina de buscar. Esto lo estara
            # haciendo varias veces, alterando las capacidades de las tuberias hasta que
            # no haya más caminos
            path, bottleneck = bfs(R, nodo, nodo_destino)
            while path:
                # Iterar sobre el camino recibido por el BFS
                for i in range(len(path) - 1):
                    u = path[i]
                    v = path[i + 1]

                    # Actualizar capacidades de las aristas en ambas direcciones
                    for vecino in R[u]["vecinos"]:
                        if vecino["id"] == v:
                            vecino["capacidad"] -= bottleneck
                            break
                    for vecino in R[v]["vecinos"]:
                        if vecino["id"] == u:
                            vecino["capacidad"] += bottleneck
                            key = tuple(sorted([u, v]))
                            usos[key] = usos.get(key, 0) + bottleneck
                            break

                # Actualizar el flujo máximo y encontrar un nuevo camino
                flujo_maximo += bottleneck
                path, bottleneck = bfs(R, nodo, nodo_destino)

            # Guardar el flujo máximo y el uso de capacidad de cada tubería
            flujos_maximos[nodo] = (flujo_maximo, deepcopy(usos))
    return flujos_maximos


# Función para guardar los resultados de Maxflow en un archivo
# Recibe: Lista con diccionarios con los resultados de Maxflow, nombre del archivo, grafo
# Regresa: Nada
def save_to_file(data, name, grafo):
    prev_sector = ""
    # Abrir el archivo
    with open(f"resultados/resultado_MaxFlow_{name}.txt", "w") as f:
        # Iterar sobre los resultados
        for d in data:
            origen = d["origen"]
            destino = d["destino"]
            flujo = d["flujo"]
            path = d["path"]
            # Si el sector del resultado es diferente al anterior, escribir el sector
            if prev_sector != d["sector"]:
                f.write(f"Sector: {d['sector']}\n")
                prev_sector = d["sector"]
            f.write(f"Origen: {origen} | Destino: {destino} | Flujo Máximo: {flujo}\n")

            for p in path:
                for vecino in grafo[p[0]]["vecinos"]:
                    if vecino["id"] == p[1]:
                        f.write(
                            f"\tTubería: {p[0]}->{p[1]}\t|\tCapacidad: {round(path[p], 2)}/{vecino['capacidad']}\n"
                        )
                        break

            f.write("\n")
        f.write(
            "*Las aristas que no aparecen representan tuberías que no se usaron, y por ende, su capacidad seguiría siendo la misma\n"
        )
