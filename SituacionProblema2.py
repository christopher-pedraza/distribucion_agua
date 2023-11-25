import Graph
import LongitudTuberias
import FrescuraAgua
import Sectorizacion
import FrescuraAgua

def problema_2():
    # Escribe en un archivo de texto
    LongitudTuberias.add_file(grafo_FOS, "resultados/resultado_longitud_FOS.txt")
    LongitudTuberias.add_file(grafo_HAN, "resultados/resultado_longitud_HAN.txt")
    LongitudTuberias.add_file(grafo_NYT, "resultados/resultado_longitud_NYT.txt")
    LongitudTuberias.add_file(grafo_PES, "resultados/resultado_longitud_PES.txt")

def problema_3():
    Graph.crear_sector(grafo_FOS)
    Sectorizacion.sectores_cerrados(grafo_FOS, "resultados/resultado_Sectorizacion_FOS.txt")

    Graph.crear_sector(grafo_HAN)
    Sectorizacion.sectores_cerrados(grafo_HAN, "resultados/resultado_Sectorizacion_HAN.txt")

    Graph.crear_sector(grafo_NYT)
    Sectorizacion.sectores_cerrados(grafo_NYT, "resultados/resultado_Sectorizacion_NYT.txt")

    Graph.crear_sector(grafo_PES)
    Sectorizacion.sectores_cerrados(grafo_PES, "resultados/resultado_Sectorizacion_PES.txt")



def problema_4():
    Graph.crear_sector(grafo_FOS)
    resultado_FOS = FrescuraAgua.max_delay_per_sector(grafo_FOS)
    FrescuraAgua.guardar_resultados_en_archivo("resultados/resultado_FrescuraAgua_FOS.txt", resultado_FOS)
    Graph.crear_sector(grafo_HAN)
    resultado_HAN = FrescuraAgua.max_delay_per_sector(grafo_HAN)
    FrescuraAgua.guardar_resultados_en_archivo("resultados/resultado_FrescuraAgua_HAN.txt", resultado_HAN)
    Graph.crear_sector(grafo_NYT)
    resultado_NYT = FrescuraAgua.max_delay_per_sector(grafo_NYT)
    FrescuraAgua.guardar_resultados_en_archivo("resultados/resultado_FrescuraAgua_NYT.txt", resultado_NYT)
    Graph.crear_sector(grafo_PES)
    resultado_PES = FrescuraAgua.max_delay_per_sector(grafo_PES)
    FrescuraAgua.guardar_resultados_en_archivo("resultados/resultado_FrescuraAgua_PES.txt", resultado_PES)



   
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
    Graph.crear_sector(grafo_FOS)
    Graph.crear_sector(grafo_HAN)
    Graph.crear_sector(grafo_NYT)
    Graph.crear_sector(grafo_PES)

    problema_2()
    problema_3()
    problema_4()
    problema_7()

