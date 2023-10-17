"""
La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos anteriores. 
La secuencia comienza con 0 y 1, y los números siguientes en la secuencia son la suma de los dos números anteriores. 
La secuencia de Fibonacci se ve así: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, y así sucesivamente.

El algoritmo de la secuencia de Fibonacci se puede implementar de varias maneras. 
Una de las formas más comunes es mediante recursión. 
Aquí tienes una implementación sencilla del algoritmo de Fibonacci en Python usando recursión

Explicación:

Caso base: Si n es 0, el resultado es 0. Si n es 1, el resultado es 1. Estos son los casos base de la recursión.

Caso recursivo: Para cualquier otro valor de n, la función fibonacci(n) es la suma de los dos números anteriores en la secuencia de Fibonacci, 
es decir, fibonacci(n-1) y fibonacci(n-2). 
Esta llamada recursiva se hace hasta que se alcanzan los casos base.
Aunque esta implementación es simple, tiene un problema de eficiencia. 
Calcula muchos números de Fibonacci múltiples veces, lo que lleva a un tiempo de ejecución exponencial, 
lo cual es ineficiente para valores grandes de n. Para mejorar la eficiencia, 
se pueden utilizar técnicas como la memorización (también conocida como memoización) o la iteración.

"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
n = 10  # Encuentra el décimo número en la secuencia de Fibonacci
result = fibonacci(n)
print(f"El {n}-ésimo número en la secuencia de Fibonacci es: {result}")
