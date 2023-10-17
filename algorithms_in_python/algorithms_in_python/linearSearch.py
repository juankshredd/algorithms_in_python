"""
El algoritmo de búsqueda lineal es un método simple y directo para encontrar un elemento específico en una lista. 
Funciona revisando cada elemento de la lista hasta encontrar el elemento buscado, 
o hasta determinar que el elemento no está presente en la lista.

Explicación:

Bucle For: La función linear_search recorre cada elemento de la lista utilizando un bucle for.
Comparación: Compara cada elemento de la lista con el objetivo (target).
Encuentra el elemento: Si encuentra un elemento que coincide con el objetivo, devuelve el índice de ese elemento en la lista.
Elemento no encontrado: Si el bucle termina y no se ha encontrado el elemento, la función devuelve -1 para indicar que el elemento no está en la lista.
El algoritmo de búsqueda lineal es fácil de entender y utilizar, pero puede volverse ineficiente para listas muy grandes, ya que tiene una complejidad de tiempo lineal,
es decir, su tiempo de ejecución crece linealmente con el tamaño de la lista. 
Si la lista es larga, otros algoritmos de búsqueda como la búsqueda binaria pueden ser mucho más eficientes.
"""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Se encontró el elemento, devuelve su índice
    return -1  # El elemento no está en la lista

# Ejemplo de uso
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 9
result = linear_search(arr, target)

if result != -1:
    print(f"El elemento {target} está en el índice {result}.")
else:
    print(f"El elemento {target} no está en la lista.")
