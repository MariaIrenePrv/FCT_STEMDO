# ### Ejercicio: Crear y mostrar una matriz
 
# **Descripción:**
 
# Escribe un programa que genere una matriz de 3x3 con números aleatorios del 1 al 10 y luego imprima la matriz en un formato legible.


# Importamos la libreria randint
from random import randint

# Creamos la matriz
matriz = []

# Creamos un bucle for para completar la matriz 3x3 con números aleatorios.
for fila in range(3):
    # Lista vacía para cada fila de la matriz
    fila_matriz = []
    for columna in range(3):
        # Número aleatorio del 1 al 10
        aleatorio = randint(1,10)
        # Añadimos el número a la fila
        fila_matriz.append(aleatorio)
    # Añadimos la fila a la matriz
    matriz.append(fila_matriz)

# Imprimimos por pantalla la matriz 
for fila in matriz:
    print(fila)