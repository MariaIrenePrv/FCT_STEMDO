# ### Enunciado del Ejercicio: Comparadores y Operadores Lógicos

# Crea un programa en Python que pida al usuario ingresar tres números y determine si:

# 1. Los tres números son iguales.
# 2. Los tres números son diferentes.
# 3. Al menos dos números son iguales.
# 4. Al menos uno de los números es mayor que 100.
# 5. Los tres números están en un rango entre 0 y 50 (inclusive).

# #### Requisitos:

# 1. El programa debe pedir al usuario ingresar tres números enteros.
# 2. Utiliza comparadores (`==`, `!=`, `>`, `<`, `>=`, `<=`) y operadores lógicos (`and`, `or`, `not`) para evaluar las condiciones anteriores.
# 3. Imprime un mensaje que indique cuál de las condiciones se cumple (pueden cumplirse varias al mismo tiempo).

# Pedimos al usuario 3 números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Comprobación 3 números iguales
if num1 == num2 == num3:
    print("Los tres números son iguales.")

# Comprobación 3 números diferentes 
if num1 != num2 and num1 != num3 and num2 != num3:
    print("Los tres números son diferentes.")

# Comprobación 2 iguales 
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Al menos dos números son iguales.")

# Comprobación 1 mayor que 100
if num1 > 100 or num2 > 100 or num3 > 100:
    print("Al menos uno de los números es mayor que 100.")

# Comprobación números entre 0 y 50 
if 0 <= num1 <= 50 and 0 <= num2 <= 50 and 0 <= num3 <= 50:
    print("Los tres números están en el rango entre 0 y 50.")
