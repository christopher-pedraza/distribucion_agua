# Problema 2  Longitud de las tuberías.
# Utiliza las coordenadas x,y de cada nodo para determinar la longitud de la tubería que conecta dos nodos.
# Salidas: un listado de aristas, agregando la longitud a sus atributos preexistentes.


# Funcion para escribir el grafo a un archivo de texto
def add_file(grafo, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        # Escribe el numero de nodos y aristas
        for nodo, detalles in grafo.items():
            archivo.write(f"Nodo {nodo}:\n")
            archivo.write(f"  Coordenadas: ({detalles['x']}, {detalles['y']})\n")
            archivo.write("  Vecinos:\n")
            for vecino in detalles["vecinos"]:
                archivo.write(
                    f"    - Nodo: {vecino['id']}, Peso: {vecino['capacidad']}, longitud: {vecino['longitud']}\n"
                )
            archivo.write("\n")
