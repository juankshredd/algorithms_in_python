"""
algoritmo Quick Sort es un algoritmo de ordenamiento eficiente y ampliamente utilizado

En este algoritmo, un elemento de la lista se selecciona como el "pivote" 
y se divide la lista en dos sublistas: una con elementos menores que el pivote 
y otra con elementos mayores que el pivote. Luego, el algoritmo se aplica recursivamente a estas sublistas. 
Finalmente, se concatenan las sublistas ordenadas junto con el pivote para obtener la lista ordenada.

Quick Sort tiene un rendimiento promedio muy bueno y es adecuado para grandes conjuntos de datos

Explicación:

Pivote: Se elige un elemento de la lista como pivote. En el código, hemos tomado el primer elemento del array como pivote.
División: La lista se divide en dos sublistas: una que contiene elementos menores que el pivote y otra con elementos mayores que el pivote.
Recursión: Se aplica el mismo proceso de forma recursiva a las sublistas generadas. Cada sublista se convierte en una lista más pequeña hasta que tengan 0 o 1 elementos. 
Las sublistas de 0 o 1 elemento ya están ordenadas por definición.
Combinación: Finalmente, las sublistas ordenadas se combinan para formar la lista completamente ordenada.
Este proceso de dividir, ordenar y combinar se repite hasta que toda la lista esté ordenada. 
Quick Sort es un algoritmo de ordenamiento eficiente en la mayoría de los casos y tiene una complejidad promedio de O(n log n), 
aunque puede degradarse a O(n^2) en el peor de los casos si no se elige un buen pivote.






"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Elementos menores que el pivote
        less = [x for x in arr[1:] if x <= pivot]
        # Elementos mayores que el pivote
        greater = [x for x in arr[1:] if x > pivot]
        # Llamadas recursivas para ordenar las sublistas
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Lista ordenada:")
print(sorted_arr)
