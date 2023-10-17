"""
La búsqueda en amplitud (Breadth-First Search o BFS en inglés) 
es un algoritmo para recorrer o buscar estructuras de datos como árboles y grafos. 
A diferencia de la búsqueda en profundidad, BFS explora todos los nodos vecinos del 
nodo actual antes de moverse a los nodos vecinos de estos nodos.

Explicación:

Inicialización: 
Se crea un conjunto visited para realizar un seguimiento de los nodos que ya han sido visitados 
y una cola queue para almacenar los nodos que están pendientes de explorar. 
Comenzamos con el nodo de inicio (start) y lo añadimos a la cola.
Exploración del grafo: 
Mientras hay nodos en la cola, el algoritmo saca un nodo de la cola, lo visita, marca como visitado 
y añade sus nodos vecinos no visitados a la cola. Esto asegura que el algoritmo explore todos los nodos
 en el mismo nivel antes de moverse al siguiente nivel.
Ejemplo de uso: 
En el ejemplo proporcionado, se representa un grafo como un diccionario en Python. 
El nodo inicial es 'A' y el algoritmo BFS imprime los nodos del grafo en el orden en que son visitados.
BFS es útil para encontrar el camino más corto en un grafo no ponderado y para verificar la conectividad del grafo. 
También se utiliza en problemas de búsqueda de rutas, como encontrar el camino más corto en un mapa, 
donde cada intersección es un nodo y las calles son aristas.

"""

from collections import deque

def bfs(graph, start):
    visited = set()  # Conjunto para realizar un seguimiento de nodos visitados
    queue = deque([start])  # Cola para almacenar nodos pendientes de explorar
    
    while queue:
        node = queue.popleft()  # Obtiene el primer nodo de la cola
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Ejemplo de uso
# Representación de un grafo como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Recorrido BFS del grafo:")
bfs(graph, 'A')
