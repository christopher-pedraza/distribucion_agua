# Problema 3
# Utiliza el dijsktra del problema 2 para saber cuales son las distancias hacia las funtes, las fuentes tienen como sector su propio nodo y luego de eso vamos comparando
# con cada nodo el que esta más cerca y dependiendo de eso lo ponemos en ese sector, y al final miramos los vecinos de cada nodo y los que no esten en el mismo sector se 
# eliminan
# Salida: Lista de tuberias cerradas junto con los nodos del grafo actualizado con su respectiva sección

def sectores_cerrados(grafo, nombre_archivo):    
    lst_cerrada = set()
    for nodo, detalles in grafo.items():
        vecinos = detalles['vecinos']
        for vecino in vecinos:
            vecino_nodo = vecino['id']
            if grafo[nodo]['sector'] != grafo[vecino_nodo]['sector']:
                # Añadir pares ordenados para evitar duplicados
                par_ordenado = tuple(sorted((nodo, vecino_nodo)))
                lst_cerrada.add(par_ordenado)
    with open(nombre_archivo, "w") as archivo:
        archivo.write("---------------------------------- Sectorizacion -----------------------------------------------\n")
        for nodo, detalles in grafo.items():
            archivo.write(f"Nodo: {nodo} sector al que pertenece: {detalles['sector']}\n")
        archivo.write("---------------------------------- Tuberias Cerradas -----------------------------------------------\n")
        archivo.write(f"{lst_cerrada}")
            



