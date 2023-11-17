# Problema 2  Longitud de las tuberías.
#Utiliza las coordenadas x,y de cada nodo para determinar la longitud de la tubería que conecta dos nodos. 
# Salidas: un listado de aristas, agregando la longitud a sus atributos preexistentes. 

# Librerías Ncesarias
import math
from SituacionProblema2 import create_graph


# Funcion para leer un archivo de texto y crear un grafo a partir de el

def longitud_tuberias(grafo):
    # Copia el grafo para no modificar el original
    nuevo_grafo = grafo.copy()
    # Calcula la longitud entre cada nodo y sus vecinos usando la longitud euclidiana
    for nodo in grafo:
        # Crea una lista vacia para guardar los vecinos con su longitud
        nuevos_vecinos = []
        # Calcula la longitud entre el nodo y cada uno de sus vecinos
        for vecino in grafo[nodo]["vecinos"]:
            x1 = grafo[nodo]["x"]
            y1 = grafo[nodo]["y"]
            x2 = grafo[vecino[0]]["x"]
            y2 = grafo[vecino[0]]["y"]
            # Calcula la longitud euclidiana entre los dos nodos
            longitud = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            # Agrega el vecino con su longitud a la lista de vecinos
            nuevos_vecinos.append((vecino[0], vecino[1], {"longitud": longitud}))
        # Actualiza los vecinos del nodo
            nuevo_grafo[nodo]["vecinos"] = nuevos_vecinos
    # Regresa el grafo con las longituds actualizadas
    return nuevo_grafo

# Funcion para escribir el grafo a un archivo de texto

def add_file(grafo, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        # Escribe el numero de nodos y aristas
        for nodo, detalles in grafo.items():
            archivo.write(f"Nodo {nodo}:\n")
            archivo.write(f"  Coordenadas: ({detalles['x']}, {detalles['y']})\n")
            archivo.write("  Vecinos:\n")
            for vecino in detalles['vecinos']:
                archivo.write(f"    - Nodo: {vecino[0]}, Peso: {vecino[1]}, longitud: {vecino[2]['longitud']}\n")
            archivo.write("\n")


if __name__ == "__main__":

    # Crea los grafos
    grafo_FOS, new_nodes_FOS = create_graph("grafos/FOS.txt")
    grafo_HAN, new_nodes_HAN = create_graph("grafos/HAN.txt")
    grafo_NYT, new_nodes_NYT = create_graph("grafos/NYT.txt")
    grafo_PES, new_nodes_PES = create_graph("grafos/PES.txt")
    
    # Actualiza los grafos con las longituds entre nodos y los escribre en un archivo de texto
    grafo_FOS_actualizado = longitud_tuberias(grafo_FOS)
    add_file(grafo_FOS_actualizado, "resultado_longitud_FOS.txt")
    
    grafo_HAN_actualizado = longitud_tuberias(grafo_HAN)
    add_file(grafo_HAN_actualizado, "resultado_longitud_HAN.txt")
    
    grafo_NYT_actualizado = longitud_tuberias(grafo_NYT)
    add_file(grafo_NYT_actualizado, "resultado_longitud_NYT.txt")
    
    grafo_PES_actualizado = longitud_tuberias(grafo_PES)
    add_file(grafo_PES_actualizado, "resultado_longitud_PES.txt")