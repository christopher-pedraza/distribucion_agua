import Graph
import LongitudTuberias


def problema_2():
    # Actualiza los grafos con las longituds entre nodos y los escribre en un archivo de texto
    grafo_FOS_actualizado = LongitudTuberias.longitud_tuberias(grafo_FOS)
    LongitudTuberias.add_file(
        grafo_FOS_actualizado, "resultados/resultado_longitud_FOS.txt"
    )

    grafo_HAN_actualizado = LongitudTuberias.longitud_tuberias(grafo_HAN)
    LongitudTuberias.add_file(
        grafo_HAN_actualizado, "resultados/resultado_longitud_HAN.txt"
    )

    grafo_NYT_actualizado = LongitudTuberias.longitud_tuberias(grafo_NYT)
    LongitudTuberias.add_file(
        grafo_NYT_actualizado, "resultados/resultado_longitud_NYT.txt"
    )

    grafo_PES_actualizado = LongitudTuberias.longitud_tuberias(grafo_PES)
    LongitudTuberias.add_file(
        grafo_PES_actualizado, "resultados/resultado_longitud_PES.txt"
    )


def problema_7():
    Graph.add_nodes(grafo_FOS, new_nodes_FOS)
    Graph.add_nodes(grafo_HAN, new_nodes_HAN)
    Graph.add_nodes(grafo_NYT, new_nodes_NYT)
    Graph.add_nodes(grafo_PES, new_nodes_PES)
    # Graph.display_graph(grafo_FOS)
    # Graph.display_graph(grafo_HAN)
    # Graph.display_graph(grafo_NYT)
    # Graph.display_graph(grafo_PES)


if __name__ == "__main__":
    # Creacion de los grafos
    grafo_FOS, new_nodes_FOS = Graph.create_graph("grafos/FOS.txt")
    grafo_HAN, new_nodes_HAN = Graph.create_graph("grafos/HAN.txt")
    grafo_NYT, new_nodes_NYT = Graph.create_graph("grafos/NYT.txt")
    grafo_PES, new_nodes_PES = Graph.create_graph("grafos/PES.txt")

    problema_2()
    problema_7()
