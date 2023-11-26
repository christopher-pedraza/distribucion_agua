# 4.- Frescura del agua en función de la distancia del nodo a la fuente.
# Una métrica de la calidad del agua es el tiempo que tarda en llegar de la fuente a un nodo. Esto es proporcional a la distancia. Por cada sector, determina cuál seria el nodo que recibe el agua con mayor tardanza.
# Reporta su distancia a la fuente.

# Salidas: Por cada sector, su fuente, nodo mas lejano y la longitud de esa distancia.


import math

# Lista para almacenar las fuentes

def max_delay_per_sector(graph, nombre_archivo):
    fuentes = []
    # Funcion para calcular el nodo mas lejano de cada sector y su distancia a la fuente usando dijkstra
    sectors = {}
    for node_id, node_info in graph.items():
        if node_info["fuente"]:  # Excluir nodos fuentes
            fuentes.append(node_id)
        
    distancia = 0
    nodo_mas_lejano = 0
    for index in range(len(fuentes)):
        for node_id, node_info in graph.items():
            if node_info["fuente"]:  # Excluir nodos fuentes
                continue
            result = math.sqrt(
                (graph[node_id]["x"] - graph[fuentes[index]]["x"]) ** 2
                + (graph[node_id]["y"] - graph[fuentes[index]]["y"]) ** 2
            )

            if result > distancia:
                distancia = result
                nodo_mas_lejano = node_id
        

        # Guardar los resultados en un archivo de texto
        with open(nombre_archivo, "a") as file:
            file.write(f"Para el sector {fuentes[index]}:\n")
            file.write(f"Fuente: {fuentes[index]}\n")
            file.write(f"Nodo más lejano: {nodo_mas_lejano}\n")
            file.write(f"Distancia: {distancia}\n\n")

        # Reiniciar variables
        distancia = 0
        nodo_mas_lejano = 0
