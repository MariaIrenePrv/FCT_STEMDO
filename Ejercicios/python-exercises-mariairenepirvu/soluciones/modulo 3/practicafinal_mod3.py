# ### Análisis de Texto

# Crear un programa en Python que solicite al usuario un texto y tres letras, y realice varios análisis sobre el texto ingresado. El programa mostrará los resultados de estos análisis de manera clara y organizada.

# #### Instrucciones:

# 1. **Solicita al usuario que ingrese un texto:**
#    Utiliza la función `input()` para capturar el texto.

# 2. **Solicita al usuario que ingrese tres letras:**
#    Utiliza la función `input()` nuevamente para capturar las tres letras a su elección.

# 3. **Realiza los siguientes análisis sobre el texto:**
#    - Contar cuántas veces aparece cada una de las letras ingresadas en el texto. Asegúrate de convertir tanto el texto como las letras a minúsculas para encontrar todas las apariciones.
#    - Contar la cantidad total de palabras en el texto. Utiliza el método `split()` para dividir el texto en palabras.
#    - Obtener la primera y última letra del texto.
#    - Invertir el orden de las palabras en el texto.
#    - Verificar si la palabra "Python" está presente en el texto.

# 4. **Muestra los resultados de los análisis** de manera clara y organizada.

# #### Recuerda:

# - Utiliza variables descriptivas para almacenar los resultados de cada análisis.
# - Emplea métodos de cadenas y listas para realizar los análisis de manera eficiente.
# - Maneja correctamente las mayúsculas y minúsculas para garantizar resultados precisos.

# Declaro la variable texto 
texto = input("Introduce un texto: ") 

# Declaro la variable letras 
letras = input("Introduce tres letras: ") 

# Declaramos la variable y pasamos a minusculas todo el texto.
minuscula = texto.lower()

# Declaramos las variables de las letras y las pasamos a minúsculas
letra1 = letras[0].lower()
letra2 = letras[1].lower()
letra3 = letras[2].lower()

# Sacamos por pantalla el número de veces que aparece cada letra
print(f"La letra {letra1} aparece {minuscula.count(letra1)} veces.")
print(f"La letra {letra2} aparece {minuscula.count(letra2)} veces.")
print(f"La letra {letra3} aparece {minuscula.count(letra3)} veces.")

# Divido el texto en palabras
palabras = texto.split(" ")
 
# Muestro el número total de palabras 
print(f"El número total de palabras en el texto es: {len(palabras)}")

# Declaro la variable primera 
primera = texto[0]

# Imprimo la primera letra en aparecer
print(f"La primera palabra del texto es: {primera}")

# Declaro la variable ultima 
ultima = texto[-1]

# Imprimo la última letra en aparecer
print(f"La última palabra del texto es: {ultima}")

# Invierto el orden de las palabras del texto. Utilizo la variable 'palabras' ya que esta contiene el texto separado por palabras.
invertido = " ".join(palabras[::-1])

# Imprimo el texto invertido
print(f"El texto invertido es: {invertido}")

# Verificación Python
verificacion = "Python" in texto
print(f"¿La palabra \"Python\" aparece en el texto? {verificacion}")