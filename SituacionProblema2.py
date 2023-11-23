import Graph
import LongitudTuberias


def problema_2():
    # Escribe en un archivo de texto
    LongitudTuberias.add_file(grafo_FOS, "resultados/resultado_longitud_FOS.txt")
    LongitudTuberias.add_file(grafo_HAN, "resultados/resultado_longitud_HAN.txt")
    LongitudTuberias.add_file(grafo_NYT, "resultados/resultado_longitud_NYT.txt")
    LongitudTuberias.add_file(grafo_PES, "resultados/resultado_longitud_PES.txt")


def problema_7():
    Graph.add_nodes(grafo_FOS, new_nodes_FOS)
    Graph.add_nodes(grafo_HAN, new_nodes_HAN)
    Graph.add_nodes(grafo_NYT, new_nodes_NYT)
    Graph.add_nodes(grafo_PES, new_nodes_PES)


if __name__ == "__main__":
    # Creacion de los grafos
    grafo_FOS, new_nodes_FOS = Graph.create_graph("grafos/FOS.txt")
    grafo_HAN, new_nodes_HAN = Graph.create_graph("grafos/HAN.txt")
    grafo_NYT, new_nodes_NYT = Graph.create_graph("grafos/NYT.txt")
    grafo_PES, new_nodes_PES = Graph.create_graph("grafos/PES.txt")

    problema_2()
    problema_7()
