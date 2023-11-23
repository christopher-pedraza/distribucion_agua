import Graph
import LongitudTuberias
import FrescuraAgua

def problema_2():
    # Actualiza los grafos con las longitudes entre nodos y los escribre en un archivo de texto
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

def problema_4():
    # Calcula la frescura del agua basada en la distancia a la fuente para cada sector
    grafo_FOS, _ = Graph.create_graph("grafos/FOS.txt")
    resultado_frescura_agua_FOS = FrescuraAgua.frescura_agua(grafo_FOS)
    FrescuraAgua.write_results_to_file(
        resultado_frescura_agua_FOS, "resultados/resultado_frescura_agua_FOS.txt"
    )

    resultado_frescura_agua_HAN = FrescuraAgua.frescura_agua(grafo_HAN)
    FrescuraAgua.write_results_to_file(
        resultado_frescura_agua_HAN, "resultados/resultados_frescura_agua_HAN.txt"
    )

    grafo_NYT, _ = Graph.create_graph("grafos/NYT.txt")
    resultado_frescura_agua_NYT = FrescuraAgua.frescura_agua(grafo_NYT)
    FrescuraAgua.write_results_to_file(
        resultado_frescura_agua_NYT, "resultados/resultados_frescura_agua_NYT.txt"
    )

    grafo_PES, _ = Graph.create_graph("grafos/PES.txt")
    resultado_frescura_agua_PES = FrescuraAgua.frescura_agua(grafo_PES)
    FrescuraAgua.write_results_to_file(
        resultado_frescura_agua_PES, "resultados/resultados_frescura_agua_PES.txt"
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
    problema_4()
    problema_7()
