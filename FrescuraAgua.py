# Salidas: Por cada sector, su fuente, nodo mas lejano y la longitud de esa distancia.

from Graph import dijkstra


def max_delay_per_sector(graph):
    sectors = {}

    for node_id, node_info in graph.items():
        if node_info["fuente"]:
            distances_from_node = dijkstra(graph, node_id)

            # Calcular los nodos mas lejanos desde cada fuente y que esten en el mismo sector
            max_distance = float("-inf")
            farthest_node = None
            # Se itera sobre los nodos del grafo auxiliar
            for destination, distance in distances_from_node.items():
                # Si la distancia es mayor a la distancia guardada en el diccionario se actualiza
                if (
                    distance > max_distance
                    and graph[node_id]["sector"] == graph[destination]["sector"]
                ):
                    max_distance = distance
                    farthest_node = destination
            # Se marca el nodo como el mas lejano
            if farthest_node is not None:
                sectors[graph[node_id]["sector"]] = {
                    "fuente": node_id,
                    "nodo_mas_lejano": farthest_node,
                    "distancia": max_distance,
                }

    return sectors


def guardar_resultados_en_archivo(nombre_archivo, resultados):
    # Funcion para guardar los resultados en un archivo de texto
    with open(nombre_archivo, "w") as file:
        for sector, data in resultados.items():
            print(f"Para el sector {sector}:", file=file)
            print(f"Fuente: {data['fuente']}", file=file)
            print(f"Nodo más lejano: {data['nodo_mas_lejano']}", file=file)
            print(f"Distancia: {data['distancia']}\n", file=file)
