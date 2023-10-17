"""
La búsqueda en profundidad (Depth-First Search o DFS en inglés) 
es un algoritmo para recorrer o buscar estructuras de datos como árboles y grafos. 
DFS comienza desde el nodo inicial (o nodo raíz en un árbol) y explora lo más profundo posible 
a lo largo de cada rama antes de retroceder.

Explicación:

Parámetros de la función dfs: La función dfs toma tres parámetros: 
el grafo representado como un diccionario (graph), el nodo actual (node), y un conjunto visited para realizar un seguimiento de los nodos visitados.
Condición base: Si el nodo actual no está en el conjunto visited, se imprime el nodo y se añade al conjunto visited.
Recursión: Luego, la función se llama recursivamente para cada nodo vecino del nodo actual. 
Esto asegura que el algoritmo se adentre profundamente en el grafo antes de retroceder y explorar otras ramas.
Ejemplo de uso: En el ejemplo proporcionado, se representa un grafo como un diccionario en Python. 
El nodo inicial es 'A' y el algoritmo DFS imprime los nodos del grafo en el orden en que son visitados.
DFS es útil para encontrar caminos en un grafo, verificar la conectividad del grafo y 
para muchas otras aplicaciones en ciencias de la computación y problemas del mundo real que involucran estructuras de datos tipo árbol o grafo.


"""
def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

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

visited = set()  # Conjunto para realizar un seguimiento de nodos visitados
print("Recorrido DFS del grafo:")
dfs(graph, 'A', visited)
