"""
algoritmo de ordenamiento de burbuja (Bubble Sort) es un algoritmo simple pero ineficiente para ordenar una lista de elementos

En este algoritmo, se compara cada elemento con el siguiente en la lista 
y se intercambian si están en el orden incorrecto. 
Este proceso se repite para cada elemento de la lista hasta que toda la lista esté ordenada. 
Ten en cuenta que el algoritmo de burbuja no es eficiente para grandes conjuntos de datos debido 
a su complejidad de tiempo cuadrática.

Explicación del código:

n = len(lista): Esto obtiene la longitud de la lista que se va a ordenar.
El primer bucle for itera sobre la lista desde el primer elemento hasta el último.
El segundo bucle for compara los elementos adyacentes y los intercambia si están en el orden incorrecto. 
Después de la primera iteración, el elemento más grande estará en la última posición.
El proceso se repite para los elementos restantes (desde el primer elemento hasta el penúltimo en la segunda iteración, 
y así sucesivamente), asegurando que los elementos más grandes se coloquen en su posición correcta.
Finalmente, después de completar todas las iteraciones, la lista estará ordenada de menor a mayor.
"""

def bubble_sort(lista):
    n = len(lista)
    
    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente elemento, los intercambiamos
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ejemplo de lista desordenada
lista = [64, 34, 25, 12, 22, 11, 90]

# Llamamos a la función bubble_sort para ordenar la lista
bubble_sort(lista)

# Imprimimos la lista ordenada
print("Lista ordenada:", lista)
