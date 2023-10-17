"""
El algoritmo de Dijkstra es un algoritmo para encontrar el camino más corto desde un nodo de inicio dado a todos los demás nodos 
en un grafo ponderado y dirigido (donde cada arista tiene un peso numérico asociado). 
Es un algoritmo de búsqueda en grafos que encuentra el camino más corto desde un nodo fuente 
a todos los demás nodos en un grafo con pesos no negativos

Explicación:

Inicialización: 
distances es un diccionario que mantiene un seguimiento de la distancia más corta conocida 
desde el nodo de inicio hasta cada nodo en el grafo. 
Se inicializa con infinito para todos los nodos excepto el nodo de inicio, 
que se inicializa con 0. priority_queue es una cola de prioridad (implementada como una lista en este caso) 
que se utiliza para seleccionar el próximo nodo a explorar.
Exploración del grafo: 
Mientras haya nodos en la cola de prioridad, el algoritmo selecciona el nodo con la distancia más corta conocida, 
y luego actualiza las distancias a sus nodos vecinos si se encuentra un camino más corto. 
Esto se repite hasta que se hayan explorado todos los nodos alcanzables desde el nodo de inicio.
Resultado: Después de que el algoritmo ha terminado, 
el diccionario distances contiene las distancias más cortas desde el nodo de inicio hasta todos los demás nodos en el grafo.
El algoritmo de Dijkstra es eficiente para grafos pequeños o medianos y funciona bien para grafos con pesos no negativos. 
Sin embargo, no maneja correctamente los grafos con aristas negativas y puede volverse ineficiente en grafos muy grandes.

"""
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si hemos encontrado un camino más corto hacia el nodo actual, actualizamos la distancia
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Si encontramos un camino más corto hacia el vecino, actualizamos la distancia
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Distancias más cortas desde el nodo", start_node, "a los demás nodos:")
print(shortest_distances)

