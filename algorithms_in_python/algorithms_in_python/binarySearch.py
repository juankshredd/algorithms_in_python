"""
algoritmo de búsqueda binaria es un método eficiente para encontrar un elemento específico en una lista ordenada. 
Funciona dividiendo repetidamente a la mitad la porción de la lista que podría contener el elemento, y luego realizando la búsqueda en esa mitad.

Explicación:

Inicialización de variables: left y right representan los índices del primer y último elemento en la lista respectivamente.
Bucle While: Mientras left sea menor o igual a right, el algoritmo calcula el índice del elemento en el medio (mid) y compara el valor del elemento en el medio con el objetivo.
Comparación y ajuste de límites: Si el elemento en el medio es igual al objetivo, se ha encontrado el elemento y se devuelve su índice. 
Si el elemento en el medio es menor que el objetivo, el objetivo debe estar en la mitad derecha de la lista, por lo que se ajusta left para buscar en la mitad derecha. 
Si el elemento en el medio es mayor que el objetivo, el objetivo debe estar en la mitad izquierda, por lo que se ajusta right para buscar en la mitad izquierda.
Salida: Si el bucle termina y no se ha encontrado el elemento, la función devuelve -1 para indicar que el elemento no está en la lista.
Este algoritmo de búsqueda binaria es eficiente, ya que reduce a la mitad el espacio de búsqueda en cada iteración, 
lo que resulta en un tiempo de ejecución de logarítmico en función del tamaño de la lista.

"""
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Encuentra el índice del elemento en el medio
        
        # Comprueba si el elemento en el medio es igual al objetivo
        if arr[mid] == target:
            return mid  # Se encontró el elemento, devuelve su índice
        elif arr[mid] < target:
            left = mid + 1  # El objetivo está en la mitad derecha, ajusta los límites
        else:
            right = mid - 1  # El objetivo está en la mitad izquierda, ajusta los límites
    
    return -1  # El elemento no está en la lista

# Ejemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"El elemento {target} está en el índice {result}.")
else:
    print(f"El elemento {target} no está en la lista.")
