import matplotlib.pyplot as plt
import math
import heapq


# Funcion para leer un archivo de texto y crear un grafo a partir de el
# Recibe: Nombre del archivo
# Regresa: El grafo y los nuevos nodos que se deben agregar
def create_graph(file_name):
    graph = {}
    new_nodes = []

    # Abre el archivo y lee las lineas
    with open(file_name, "r") as file:
        lines = file.readlines()

    # Conteo de nodos y aristas
    node_count, edge_count = lines[0].split()

    # Guardar los nodos
    for node in lines[2 : 2 + int(node_count)]:
        id, x, y, fuente = node.strip().split()
        id = int(id)
        graph[id] = {
            "x": float(x),
            "y": float(y),
            "fuente": True if fuente == "1" else False,
            "vecinos": [],
            "sector": None,
            "oficina": False,
            "esMasLejano": False,
        }

    # Guardar las aristas no dirigidas
    for edge in lines[3 + int(node_count) : 3 + int(node_count) + int(edge_count)]:
        id1, id2, weight = edge.strip().split()
        id1 = int(id1)
        id2 = int(id2)
        longitud = math.sqrt(
            (graph[id2]["x"] - graph[id1]["x"]) ** 2
            + (graph[id2]["y"] - graph[id1]["y"]) ** 2
        )
        graph[id1]["vecinos"].append(
            {"id": id2, "capacidad": weight, "longitud": longitud}
        )
        graph[id2]["vecinos"].append(
            {"id": id1, "capacidad": weight, "longitud": longitud}
        )

    # Marcar nodo como oficina
    office_index = lines[4 + int(node_count) + int(edge_count)].strip()
    office_index = int(office_index)
    graph[office_index]["oficina"] = True

    # Guardar los nuevos nodos que se deben agregar luego
    for new_node in lines[6 + int(node_count) + int(edge_count) :]:
        x, y, weight = new_node.strip().split()
        new_nodes.append({"x": float(x), "y": float(y), "capacidad": float(weight)})

    # Se regresa el grafo y los nuevos nodos
    return graph, new_nodes


def add_nodes(graph, new_nodes):
    for n_node in new_nodes:
        closest_node = [float("inf"), None]
        for node_id, values in graph.items():
            if not values["fuente"]:
                distance = (
                    (n_node["x"] - values["x"]) ** 2 + (n_node["y"] - values["y"]) ** 2
                ) ** 0.5
                if distance < closest_node[0]:
                    closest_node = [distance, node_id]

        new_index = max(graph) + 1
        graph[new_index] = {
            "x": n_node["x"],
            "y": n_node["y"],
            "fuente": False,
            "vecinos": [],
            "sector": None,
            "oficina": False,
        }
        graph[closest_node[1]]["vecinos"].append(
            {
                "id": new_index,
                "capacidad": n_node["capacidad"],
                "longitud": closest_node[0],
            }
        )
        graph[new_index]["vecinos"].append(
            {
                "id": closest_node[1],
                "capacidad": n_node["capacidad"],
                "longitud": closest_node[0],
            }
        )


def dijkstra(grafo, fuente):
    # Implementación del algoritmo de Dijkstra para encontrar la distancia más corta entre un nodo y todos los demás nodos en un grafo.
    distancias = {nodo: math.inf for nodo in grafo}
    distancias[fuente] = 0
    cola_prioridad = [(0, fuente)]

    # Mientras la cola de prioridad no esté vacía se sigue iterando sobre los nodos
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        # Si la distancia actual es mayor a la distancia guardada en el diccionario se ignora
        if distancia_actual > distancias[nodo_actual]:
            continue
        # Se itera sobre los vecinos del nodo actual
        for neighbor in grafo[nodo_actual]["vecinos"]:
            vecino = neighbor["id"]
            peso = neighbor["longitud"]

            peso = float(peso)
            # Se calcula la nueva distancia
            nueva_distancia = distancia_actual + peso
            # Si la nueva distancia es menor a la distancia guardada en el diccionario se actualiza
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                # Se agrega el vecino a la cola de prioridad
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    # Se regresa el diccionario con las distancias
    return distancias


def crear_sector(grafo):
    grafo_distancias = {}
    for nodo, detalles in grafo.items():
        if detalles["fuente"] == True:
            grafo_distancias[nodo] = []
            detalles["sector"] = nodo

    grafo_extra = {}
    for nodo, detalles in grafo.items():
        if detalles["fuente"] == True:
            grafo_extra = dijkstra(grafo, nodo)
            grafo_distancias[nodo] = grafo_extra

    for nodo in grafo.keys():
        distancia = math.inf
        for nodo2 in grafo_distancias.keys():
            if distancia > grafo_distancias[nodo2][nodo]:
                grafo[nodo]["sector"] = nodo2
                distancia = grafo_distancias[nodo2][nodo]

    # Calcular los nodos mas lejanos desde cada fuente y que esten en el mismo sector
    for fuente, distances in grafo_distancias.items():
        max_distance = float("-inf")
        farthest_node = None
        for destination, distance in distances.items():
            if (
                distance > max_distance
                and grafo[fuente]["sector"] == grafo[destination]["sector"]
            ):
                max_distance = distance
                farthest_node = destination
        if farthest_node is not None:
            grafo[farthest_node]["esMasLejano"] = True


def display_graph(graph, tuberias_cerradas=[]):
    # Coordenadas de los nodos
    x = {}
    y = {}
    # Coordenadas de las fuentes
    x_fuente = []
    y_fuente = []
    # Etiquetas de los nodos y fuentes
    labels = {}
    labels_fuente = []

    # Separar las coordenadas de los nodos por sector
    for node_id, values in graph.items():
        # Si el nodo es una fuente se agrega a la lista de fuentes
        if values["fuente"]:
            x_fuente.append(values["x"])
            y_fuente.append(values["y"])
            labels_fuente.append(node_id)
        # De lo contrario se agrega a la lista de nodos
        else:
            temp = x.get(values["sector"], [])
            temp.append(values["x"])
            x[values["sector"]] = temp
            temp = y.get(values["sector"], [])
            temp.append(values["y"])
            y[values["sector"]] = temp
            temp = labels.get(values["sector"], [])
            temp.append(node_id)
            labels[values["sector"]] = temp

    fig, ax = plt.subplots()

    # Desplegar las conexiones entre nodos
    for node_id, values in graph.items():
        # Recorrer los vecinos del nodo
        for neighbor in values["vecinos"]:
            neighbor_id = neighbor["id"]
            # Para solo hacer la conexión una vez
            # Se checa tambien que la tuberia no este cerrada
            if (
                node_id < neighbor_id
                and (node_id, neighbor_id) not in tuberias_cerradas
            ):
                x_values = [values["x"], graph[neighbor_id]["x"]]
                y_values = [values["y"], graph[neighbor_id]["y"]]
                ax.plot(x_values, y_values, color="black", linewidth=0.5)
            # Para las tuberias cerradas
            elif node_id < neighbor_id:
                x_values = [values["x"], graph[neighbor_id]["x"]]
                y_values = [values["y"], graph[neighbor_id]["y"]]
                ax.plot(x_values, y_values, color="gray", linewidth=0.5, linestyle=":")

    # Desplegar las fuentes
    ax.scatter(x_fuente, y_fuente, color="blue", marker="^")

    # Colorear los nodos por sector y agregar etiquetas
    for sector, values in x.items():
        ax.scatter(values, y[sector])
        for i, txt in enumerate(labels[sector]):
            ax.annotate(txt, (values[i], y[sector][i]))

    # Agregar etiquetas a las fuentes
    for i, txt in enumerate(labels_fuente):
        ax.annotate(txt, (x_fuente[i], y_fuente[i]))

    plt.show()
