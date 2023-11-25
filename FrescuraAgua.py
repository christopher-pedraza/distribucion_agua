# 4.- Frescura del agua en función de la distancia del nodo a la fuente.
# Una métrica de la calidad del agua es el tiempo que tarda en llegar de la fuente a un nodo. Esto es proporcional a la distancia. Por cada sector, determina cuál seria el nodo que recibe el agua con mayor tardanza.
# Reporta su distancia a la fuente.

# Salidas: Por cada sector, su fuente, nodo mas lejano y la longitud de esa distancia.

# Librerías Necesarias
import heapq

 
 # Funcion para calcular la distancia de un nodo a todos los demas nodos 
def dijkstra(graph, start): 
    # Inicializar las distancias de todos los nodos a infinito
    distances = {node: float('inf') for node in graph}
    # Inicializar la distancia del nodo inicial a 0
    distances[start] = 0
    pq = [(0, start)]


    # Mientras la cola de prioridad no este vacia
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue
# Para cada vecino del nodo actual
        for neighbor in graph[current_node]['vecinos']:
            neighbor_id = neighbor['id']
            edge_weight = neighbor['longitud']
            distance = current_distance + edge_weight

            # Si la distancia es menor a la distancia actual
            if distance < distances[neighbor_id]:
                distances[neighbor_id] = distance
                heapq.heappush(pq, (distance, neighbor_id))

    return distances

def max_delay_per_sector(graph):
    #Funcion para calcular el nodo mas lejano de cada sector y su distancia a la fuente usando dijkstra
    sectors = {}
    for node_id, node_info in graph.items():
        if node_info['fuente']:  # Excluir nodos fuentes
            continue
        
        sector = node_info['sector']
        if sector not in sectors:
            # Inicializar el sector con un nodo cualquiera
            sectors[sector] = {'fuente': None, 'nodo_mas_lejano': None, 'distancia': float('-inf')}
        
        # Calcular las distancias de todos los nodos al nodo actual
        distances = dijkstra(graph, sector)  # Usar el número de sector como fuente

        max_distance = max([distances[node] for node, info in graph.items() if not info['fuente'] and info['sector'] == sector])

        # Si la distancia es mayor a la distancia actual
        if max_distance > sectors[sector]['distancia']:
            sectors[sector]['fuente'] = sector
            sectors[sector]['nodo_mas_lejano'] = max(distances, key=distances.get)
            sectors[sector]['distancia'] = max_distance


    return sectors



def guardar_resultados_en_archivo(nombre_archivo, resultados):
    # Funcion para guardar los resultados en un archivo de texto
    with open(nombre_archivo, 'w') as file:
        for sector, data in resultados.items():
            print(f"Para el sector {sector}:", file=file)
            print(f"Fuente: {data['fuente']}", file=file)
            print(f"Nodo más lejano: {data['nodo_mas_lejano']}", file=file)
            print(f"Distancia: {data['distancia']}\n", file=file)
