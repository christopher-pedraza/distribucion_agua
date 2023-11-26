# Salidas: Por cada sector, su fuente, nodo mas lejano y la longitud de esa distancia.

# Librerías Necesarias
import heapq


# Funcion para calcular la distancia de un nodo a todos los demas nodos
def dijkstra(graph, start):
    # Inicializar las distancias de todos los nodos a infinito
    distances = {node: float("inf") for node in graph}
    # Inicializar la distancia del nodo inicial a 0
    distances[start] = 0
    pq = [(0, start)]

    # Mientras la cola de prioridad no este vacia
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue
        # Para cada vecino del nodo actual
        for neighbor in graph[current_node]["vecinos"]:
            neighbor_id = neighbor["id"]
            edge_weight = neighbor["longitud"]
            distance = current_distance + edge_weight

            # Si la distancia es menor a la distancia actual
            if distance < distances[neighbor_id]:
                distances[neighbor_id] = distance
                heapq.heappush(pq, (distance, neighbor_id))

    return distances


def max_delay_per_sector(graph):
    sectors = {}

    # por cada nodo en el grafo chequear si es fuente y si no lo es, calcular la distancia maxima
    for node_id, node_info in graph.items():
        if node_info["fuente"]:  # Exclude source nodes
            continue

        # Encontrar el sector del nodo actual y crearlo si no existe en el diccionario de sectores
        sector = node_info["sector"]
        if sector not in sectors:
            sectors[sector] = {
                "fuente": None,
                "nodo_mas_lejano": None,
                "distancia": float("-inf"),
            }

        # Encontrar los nodos del sector actual y crear un diccionario de distancias para el sector
        sector_nodes = [
            n_id
            for n_id, n_info in graph.items()
            if n_info["sector"] == sector and not n_info["fuente"]
        ]
        distances = {}

        # Calcular las distancias de cada nodo del sector actual al resto de los nodos
        for sector_node in sector_nodes:
            distances_from_node = dijkstra(graph, sector_node)
            valid_distances = {
                n: distances_from_node[n]
                for n in distances_from_node
                if not graph[n]["fuente"] and graph[n]["sector"] == sector
            }
            distances.update(valid_distances)

        # Encontrar la distancia maxima del sector actual y actualizar el diccionario de sectores
        max_distance = max(distances.values())

        # Si la distancia maxima del sector actual es mayor a la distancia maxima del sector en el diccionario de sectores, actualizar el diccionario de sectores
        if max_distance > sectors[sector]["distancia"]:
            sectors[sector]["fuente"] = sector
            sectors[sector]["nodo_mas_lejano"] = max(distances, key=distances.get)
            sectors[sector]["distancia"] = max_distance

    return sectors


def guardar_resultados_en_archivo(nombre_archivo, resultados):
    # Funcion para guardar los resultados en un archivo de texto
    with open(nombre_archivo, "w") as file:
        for sector, data in resultados.items():
            print(f"Para el sector {sector}:", file=file)
            print(f"Fuente: {data['fuente']}", file=file)
            print(f"Nodo más lejano: {data['nodo_mas_lejano']}", file=file)
            print(f"Distancia: {data['distancia']}\n", file=file)
