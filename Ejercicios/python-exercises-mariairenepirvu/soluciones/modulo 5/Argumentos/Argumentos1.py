# ### Ejercicio: Cantidad indeterminada de argumentos
# Crea una función llamada `suma_cuadrados` que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.


# Por ejemplo, para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

# Creamos la funcion que toma argumentos
def suma_cuadrados(*numeros):
    return sum(n ** 2 for n in numeros)

# Ejemplos 
print(suma_cuadrados(1,2,3))
print(suma_cuadrados(2,2,2))
print(suma_cuadrados(5,5))
print(suma_cuadrados(7,8,9,10))