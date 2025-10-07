# ### Enunciado del Ejercicio: Inversor de Palabras

# Crea un programa en Python que permita al usuario invertir una palabra o frase y seguir interactuando con el programa hasta que decida salir.

# #### Requisitos:

# 1. El programa debe permitir al usuario introducir una palabra o una frase.
# 2. El programa invertirá el orden de los caracteres en la palabra o frase y mostrará el resultado.
# 3. El programa debe repetirse en un bucle `while` que seguirá ejecutándose hasta que el usuario escriba la palabra clave "salir".
# 4. Si el usuario escribe "salir", el programa terminará con un mensaje de despedida.

# #### Reglas adicionales:
# - El programa debe ignorar si el usuario escribe "salir" en mayúsculas o minúsculas (por ejemplo, "SALIR", "Salir", etc.).
# - El programa no debe invertir la palabra clave "salir" y debe terminar el bucle cuando se ingrese dicha palabra.


# Bucle que no para hasta que se escriba "salir"
while True:
    # Pide al usuario una palabra o frase
    texto = input("Introduce una palabra o frase (escribe 'salir' para terminar): ")

    # Si el usuario escribe "salir", en mayúsculas o minúsculas, se cierra el bucle
    if texto.lower() == "salir":
        print("Bye bye")
        break  # Termina el bucle

    # Invertir el texto introducido
    texto_invertido = texto[::-1]

    # Imprimimos el texto invertido
    print("Texto invertido:", texto_invertido)
