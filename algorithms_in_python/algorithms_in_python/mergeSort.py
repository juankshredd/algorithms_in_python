"""
El algoritmo Merge Sort es un algoritmo de ordenamiento basado en la técnica de "dividir y conquistar". 
Divide la lista no ordenada en n sublistas de tamaño 1, 
luego las combina en pares de sublistas ordenadas, 
repite el proceso hasta que hay una sola lista ordenada.

Explicación:

División: La función merge_sort divide la lista en dos mitades (left_half y right_half) de manera recursiva hasta que cada mitad tiene un solo elemento o está vacía.
Combinación: La función merge combina dos listas ordenadas (left y right) en una sola lista ordenada (result). 
Compara los elementos en las listas left y right y agrega el elemento más pequeño a result. 
Luego, avanza al siguiente elemento en la lista de la cual se tomó el elemento agregado. 
Este proceso se repite hasta que se han recorrido todas las listas.
Recursividad: Finalmente, las llamadas recursivas y las combinaciones continúan hasta que todas las sublistas estén ordenadas 
y se hayan combinado en una única lista ordenada, que es el resultado final.

El algoritmo Merge Sort tiene una complejidad de tiempo de  O(n log n)
lo que lo hace eficiente para ordenar grandes conjuntos de datos.

"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Llamadas recursivas para ordenar las dos mitades
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combina las dos listas ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    
    # Combina las dos listas ordenadas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Agrega los elementos restantes, si los hay
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Lista ordenada:")
print(sorted_arr)
