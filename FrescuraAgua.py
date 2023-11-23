# 4.- Frescura del agua en función de la distancia del nodo a la fuente. 
#Una métrica de la calidad del agua es el tiempo que tarda en llegar de la fuente a un nodo. Esto es proporcional a la distancia. Por cada sector, determina cuál seria el nodo que recibe el agua con mayor tardanza.
#Reporta su distancia a la fuente. 

 # Salidas: Por cada sector, su fuente, nodo mas lejano y la longitud de esa distancia. 

# Librerías Ncesarias
import math
import heapq
import Graph
import os

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
        for vecino, peso in grafo[nodo_actual]["vecinos"]:
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



def frescura_agua(grafo):
    # Copia el grafo para no modificar el original
    nuevo_grafo = grafo.copy()
    for fuente in grafo:
        # Se calcula la distancia más corta entre la fuente y todos los demás nodos del grafo
        distancias = dijkstra(grafo, fuente)
        # Se obtiene el nodo más lejano y su distancia
        nodo_mas_lejano = max(distancias, key=distancias.get)
        # Se guarda el nodo más lejano y su distancia en el grafo
        distancia_maxima = distancias[nodo_mas_lejano]
        # Se guarda el nodo más lejano y su distancia en el grafo
        nuevo_grafo[fuente]["nodo_mas_lejano"] = nodo_mas_lejano
        # Se guarda el nodo más lejano y su distancia en el grafo
        nuevo_grafo[fuente]["distancia_maxima"] = distancia_maxima
    return nuevo_grafo

def write_results_to_file(results, file_path):
    # Escribir los resultados en un archivo de texto para cada sector
    file_name = os.path.basename(file_path)
    last_three_words = "_".join(file_name.split('/')[-1].split('_')[-3:])  # Extract the last three words
    try:
        with open(f"resultados/resultados_frescura_agua_{last_three_words}.txt", "w") as file:
            for fuente, detalles in results.items():
                nodo_mas_lejano = detalles["nodo_mas_lejano"]
                distancia_maxima = detalles["distancia_maxima"]
                file.write(f"Sector {last_three_words} - Fuente: {fuente}, Nodo más lejano: {nodo_mas_lejano}, Distancia: {distancia_maxima}\n")
    except Exception as e:
        print(f"Error writing file: {e}")

