import Graph
import LongitudTuberias
import FrescuraAgua
import Sectorizacion
import MaxFlow


def problema_2():
    # Escribe en un archivo de texto
    LongitudTuberias.add_file(grafo_FOS, "resultados/resultado_longitud_FOS.txt")
    LongitudTuberias.add_file(grafo_HAN, "resultados/resultado_longitud_HAN.txt")
    LongitudTuberias.add_file(grafo_NYT, "resultados/resultado_longitud_NYT.txt")
    LongitudTuberias.add_file(grafo_PES, "resultados/resultado_longitud_PES.txt")


def problema_3():
    Graph.crear_sector(grafo_FOS)
    tuberias_cerradas_FOS = Sectorizacion.sectores_cerrados(
        grafo_FOS, "resultados/resultado_Sectorizacion_FOS.txt"
    )

    Graph.crear_sector(grafo_HAN)
    tuberias_cerradas_HAN = Sectorizacion.sectores_cerrados(
        grafo_HAN, "resultados/resultado_Sectorizacion_HAN.txt"
    )

    Graph.crear_sector(grafo_NYT)
    tuberias_cerradas_NYT = Sectorizacion.sectores_cerrados(
        grafo_NYT, "resultados/resultado_Sectorizacion_NYT.txt"
    )

    Graph.crear_sector(grafo_PES)
    tuberias_cerradas_PES = Sectorizacion.sectores_cerrados(
        grafo_PES, "resultados/resultado_Sectorizacion_PES.txt"
    )

    return {
        "FOS": tuberias_cerradas_FOS,
        "HAN": tuberias_cerradas_HAN,
        "NYT": tuberias_cerradas_NYT,
        "PES": tuberias_cerradas_PES,
    }


def problema_4():
    Graph.crear_sector(grafo_FOS)
    resultado_FOS = FrescuraAgua.max_delay_per_sector(grafo_FOS)
    FrescuraAgua.guardar_resultados_en_archivo(
        "resultados/resultado_FrescuraAgua_FOS.txt", resultado_FOS
    )
    Graph.crear_sector(grafo_HAN)
    resultado_HAN = FrescuraAgua.max_delay_per_sector(grafo_HAN)
    FrescuraAgua.guardar_resultados_en_archivo(
        "resultados/resultado_FrescuraAgua_HAN.txt", resultado_HAN
    )
    Graph.crear_sector(grafo_NYT)
    resultado_NYT = FrescuraAgua.max_delay_per_sector(grafo_NYT)
    FrescuraAgua.guardar_resultados_en_archivo(
        "resultados/resultado_FrescuraAgua_NYT.txt", resultado_NYT
    )
    Graph.crear_sector(grafo_PES)
    resultado_PES = FrescuraAgua.max_delay_per_sector(grafo_PES)
    FrescuraAgua.guardar_resultados_en_archivo(
        "resultados/resultado_FrescuraAgua_PES.txt", resultado_PES
    )


def problema_7():
    Graph.add_nodes(grafo_FOS, new_nodes_FOS)
    Graph.add_nodes(grafo_HAN, new_nodes_HAN)
    Graph.add_nodes(grafo_NYT, new_nodes_NYT)
    Graph.add_nodes(grafo_PES, new_nodes_PES)
    Graph.save_graph_to_file(grafo_FOS, "FOS")
    Graph.save_graph_to_file(grafo_HAN, "HAN")
    Graph.save_graph_to_file(grafo_NYT, "NYT")
    Graph.save_graph_to_file(grafo_PES, "PES")


def problema_5():
    grafos = [
        (grafo_FOS, "FOS"),
        (grafo_HAN, "HAN"),
        (grafo_NYT, "NYT"),
        (grafo_PES, "PES"),
    ]

    # Se itera sobre los grafos
    for grafo in grafos:
        data = []
        # Se itera sobre los nodos del grafo actual
        for nodo in grafo[0]:
            # Se calcula el max flow para el nodo que sea el mas lejano
            if grafo[0][nodo]["esMasLejano"]:
                resultado = MaxFlow.max_flow(grafo[0], nodo)
                for r in resultado:
                    data.append(
                        {
                            "sector": grafo[0][nodo]["sector"],
                            "origen": r,
                            "destino": nodo,
                            "flujo": resultado[r][0],
                            "path": resultado[r][1],
                        }
                    )

        # Se guarda el resultado en un archivo
        MaxFlow.save_to_file(data, grafo[1], grafo[0])


def desplegar_grafos(tuberias_cerradas):
    Graph.display_graph(grafo_FOS, tuberias_cerradas["FOS"])
    Graph.display_graph(grafo_HAN, tuberias_cerradas["HAN"])
    Graph.display_graph(grafo_NYT, tuberias_cerradas["NYT"])
    Graph.display_graph(grafo_PES, tuberias_cerradas["PES"])


if __name__ == "__main__":
    # Creacion de los grafos
    grafo_FOS, new_nodes_FOS = Graph.create_graph("grafos/FOS.txt")
    grafo_HAN, new_nodes_HAN = Graph.create_graph("grafos/HAN.txt")
    grafo_NYT, new_nodes_NYT = Graph.create_graph("grafos/NYT.txt")
    grafo_PES, new_nodes_PES = Graph.create_graph("grafos/PES.txt")

    problema_2()
    tuberias_cerradas = problema_3()
    problema_4()
    problema_5()
    problema_7()
    desplegar_grafos(tuberias_cerradas)
