# ### Ejercicio: Conversiones

# 1. Crea una variable llamada `num1` y convierte su valor en un `int`. Imprime el tipo de dato que resulta.

# 2. Crea una variable llamada `num2` y convierte su valor en un `float`. Imprime el tipo de dato que resulta.

# 3. Suma los valores de `num1` y `num2`. **No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función `print()`.**

# Pide el valor de la variable num1
num1 = input ("Introduce un numero entero: ")
# Pide el valor de la variable num2
num2 = input ("Introduce un numero decimal: ")
# Convierte num1 en entero  
num1 = int(num1)
# Sacamos por pantalla el tipo
print(f"El número \"{num1}\" es de tipo {type(num1)}")
# Convierte num1 en decimal  
num2 = float(num2)
# Sacamos por pantalla el tipo
print(f"El número \"{num2}\" es de tipo {type(num2)}")
# Sacamos por pantalla la suma de ambos números 
print(f"La suma de {num1} + {num2} es: {num1 + num2}")  
