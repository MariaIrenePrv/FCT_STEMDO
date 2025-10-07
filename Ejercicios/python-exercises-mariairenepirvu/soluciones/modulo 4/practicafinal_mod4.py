# ### Juego Interactivo de Adivinanza de Números en Python

# Escribe un programa en Python que implemente un juego interactivo de adivinanza de números siguiendo las reglas detalladas a continuación:

# 1. **Inicio del Juego:**
#    - Solicita al usuario que ingrese su nombre.

# 2. **Generación del Número Secreto:**
#    - El programa generará aleatoriamente un número secreto entre 1 y 100.

# 3. **Reglas del Juego:**
#    - Informa al usuario que el programa ha pensado en un número y que tiene ocho intentos para adivinarlo.

# 4. **Proceso de Adivinanza:**
#    - En cada intento, solicita al usuario que ingrese un número.
#    - Valida el número ingresado y proporciona una respuesta según el caso:
#      - Si el número está fuera del rango de 1 a 100, informa al usuario que ha elegido un número no permitido.
#      - Si el número ingresado es menor que el número secreto, indica que el número elegido es menor al número secreto.
#      - Si el número ingresado es mayor que el número secreto, indica que el número elegido es mayor al número secreto.
#      - Si el usuario adivina correctamente el número secreto, felicita al usuario y muestra cuántos intentos le tomó adivinarlo.

# 5. **Terminación del Juego:**
#    - Continúa solicitando números hasta que el usuario adivine el número secreto o se agoten los ocho intentos.
#    - Una vez finalizados los intentos o al adivinar correctamente, muestra el número secreto si el usuario no lo adivinó.

# **Recuerda:**
# - Maneja correctamente los intentos y las respuestas del usuario para que el juego sea interactivo y amigable.


# Importamos la librería random
import random

# Pedimos el nombre del jugador
nombre = input("Introduce tu nombre para empezar a jugar: ")
print("Bienvenido jugador")

# Número secreto
numero_secreto = random.randint(1, 100)

# Reglas
print("He pensado en un número entre 1 y 100")
print("Tienes 8 intentos")

# Adivinanza. Bucle while con las condiciones
intentos = 0
max_intentos = 8

while intentos < max_intentos:
    entrada = input(f"Intento {intentos + 1}: Ingresa tu número: ")

    # Validar si lo ingresado es un número entero positivo
    if not entrada.isdigit():
        print("Introduce un número entero válido.")
        continue

    intento = int(entrada)

    if intento < 1 or intento > 100:
        print("El número debe estar comprendido entre 1 y 100.")
        continue

    intentos += 1

    if intento < numero_secreto:
        print("Tu número es menor, sigue intentándolo.")
    elif intento > numero_secreto:
        print("Tu número es mayor, sigue intentándolo.")
    else:
        print(f"¡Enhorabuena {nombre}! Adivinaste el número en {intentos} intentos.")
        break

# Mensaje de finalización si no lo adivina
if intento != numero_secreto:
    print(f"Lo siento, {nombre}. Te quedaste sin intentos.")
    print(f"El número secreto era: {numero_secreto}")
