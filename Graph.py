import matplotlib.pyplot as plt


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
        }

    # Guardar las aristas no dirigidas
    for edge in lines[3 + int(node_count) : 3 + int(node_count) + int(edge_count)]:
        id1, id2, weight = edge.strip().split()
        id1 = int(id1)
        id2 = int(id2)
        graph[id1]["vecinos"].append((id2, weight))
        graph[id2]["vecinos"].append((id1, weight))

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
        graph[closest_node[1]]["vecinos"].append((new_index, n_node["capacidad"]))
        graph[new_index]["vecinos"].append((closest_node[1], n_node["capacidad"]))


def display_graph(graph):
    x = []
    y = []
    x_fuente = []
    y_fuente = []
    labels = []
    labels_fuente = []

    for node_id, values in graph.items():
        if values["fuente"]:
            x_fuente.append(values["x"])
            y_fuente.append(values["y"])
            labels_fuente.append(node_id)
        else:
            x.append(values["x"])
            y.append(values["y"])
            labels.append(node_id)

    fig, ax = plt.subplots()
    ax.scatter(x, y, color="black")
    ax.scatter(x_fuente, y_fuente, color="blue")

    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i], y[i]))
    for i, txt in enumerate(labels_fuente):
        ax.annotate(txt, (x_fuente[i], y_fuente[i]))
    plt.show()
