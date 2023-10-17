"""

El problema de la mochila (Knapsack problem en inglés) 
es un problema clásico de optimización combinatoria. 
Dada una lista de objetos, cada uno con un peso y un valor, y una mochila con una capacidad máxima de peso, 
el objetivo es determinar la combinación de objetos a incluir en la mochila de manera que se maximice el valor total, 
sin exceder la capacidad de peso de la mochila.

Explicación:

Creación de la tabla dp: Se crea una tabla dp de tamaño (n + 1) x (capacity + 1), 
donde n es el número de objetos en la lista.
dp[i][w] representará el valor máximo que se puede obtener considerando los primeros i objetos y una capacidad máxima de w en la mochila.
Relleno de la tabla dp: Se utiliza un bucle doble para llenar la tabla dp. 
Para cada objeto i, se consideran dos opciones: incluirlo en la mochila o excluirlo. 
Si el peso del objeto actual (weights[i - 1]) es menor o igual a la capacidad actual (w), 
se compara el valor de incluir el objeto actual (values[i - 1]) con el valor sin incluirlo (dp[i - 1][w - weights[i - 1]]). Se toma el valor máximo de estas dos opciones.
Resultado final: El valor máximo que se puede obtener estará almacenado en dp[n][capacity], donde n es el número total de objetos y capacity es la capacidad máxima de la mochila.
Este algoritmo resuelve el problema de la mochila utilizando programación dinámica y tiene una complejidad de tiempo de 
O(n * capacity)
donde n es el número de objetos y capacity es la capacidad máxima de la mochila.

"""
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla dp usando programación dinámica
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Ejemplo de uso
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value = knapsack(weights, values, capacity)
print("El valor máximo que se puede obtener es:", max_value)
