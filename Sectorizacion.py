# Problema 3
# Aqui dependiendo de los nodos y sus vecinos son las tuberias que se van a cerrar
# Salida: Lista de tuberias cerradas junto con los nodos del grafo actualizado con su respectiva sección
# Complejidad O(Vertices +  Aristas)

def sectores_cerrados(grafo, nombre_archivo):
    # Conjunto para almacenar las tuberías cerradas
    lst_cerrada = set()

    # Iterar sobre cada nodo en el grafo
    for nodo, detalles in grafo.items():
        # Obtener los vecinos del nodo actual
        vecinos = detalles["vecinos"]
        
        # Iterar sobre los vecinos
        for vecino in vecinos:
            vecino_nodo = vecino["id"]
            
            # Verificar si los nodos pertenecen a diferentes sectores
            if grafo[nodo]["sector"] != grafo[vecino_nodo]["sector"]:
                # Añadir pares ordenados para evitar duplicados
                par_ordenado = tuple(sorted((nodo, vecino_nodo)))
                lst_cerrada.add(par_ordenado)

    # Escribir información de sectorización y tuberías cerradas en un archivo
    with open(nombre_archivo, "w") as archivo:
        archivo.write("---------------------------------- Sectorizacion -----------------------------------------------\n")
        for nodo, detalles in grafo.items():
            archivo.write(f"Nodo: {nodo} sector al que pertenece: {detalles['sector']}\n")
        
        archivo.write("---------------------------------- Tuberias Cerradas -----------------------------------------------\n")
        archivo.write(f"{lst_cerrada}")

    # Devolver el conjunto de tuberías cerradas
    return lst_cerrada

