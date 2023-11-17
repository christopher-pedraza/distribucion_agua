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
        graph[id1]["vecinos"].append((id2, weight))
        graph[id2]["vecinos"].append((id1, weight))

    # Marcar nodo como oficina
    office_index = lines[4 + int(node_count) + int(edge_count)].strip()
    graph[office_index]["oficina"] = True

    # Guardar los nuevos nodos que se deben agregar luego
    for new_node in lines[6 + int(node_count) + int(edge_count) :]:
        x, y, weight = new_node.strip().split()
        new_nodes.append({"x": float(x), "y": float(y), "weight": float(weight)})

    # Se regresa el grafo y los nuevos nodos
    return graph, new_nodes


if __name__ == "__main__":
    grafo_FOS, new_nodes_FOS = create_graph("grafos/FOS.txt")
    grafo_HAN, new_nodes_HAN = create_graph("grafos/HAN.txt")
    grafo_NYT, new_nodes_NYT = create_graph("grafos/NYT.txt")
    grafo_PES, new_nodes_PES = create_graph("grafos/PES.txt")
