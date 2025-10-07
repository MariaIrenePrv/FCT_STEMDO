# ### Ejercicio: Manejo de Strings

# Manipular y modificar cadenas de texto en Python.

# #### Instrucciones:

# 1. Une la siguiente lista en un solo string, separando cada elemento con un espacio. Utiliza el método adecuado de listas o strings y muestra el resultado en pantalla en MAYÚSCULAS.

#    ```python
#    lista_palabras = ["Si", "la", "implementación", "es", "difícil", "de", "explicar,", "puede", "que", "sea", "una", "mala", "idea"]
#    ```

# 2. Reemplaza en el nuevo string los siguientes pares de palabras:

#    - `"difícil"` por `"fácil"`
#    - `"mala"` por `"buena"`

#    Luego, muestra en pantalla la frase con ambas palabras modificadas.

# Creamos la lista 
lista_palabras = ["Si", "la", "implementación", "es", "difícil", "de", "explicar,", "puede", "que", "sea", "una", "mala", "idea"]

# Introducimos la lista en una varibale y le añadimos .join y .upper para que se convierta en un solo string y se imprima en mayúsculas. 
resultado = ' ' .join(lista_palabras).upper()

# Imprimimos el resultado
print (resultado)

# Utilizamos . replace para modificar las palabras 
resultado2= resultado.replace( 'DIFÍCIL', 'FÁCIL').replace('MALA', 'BUENA')

# Imprimimos por pantalla los nuevos resultados
print (resultado2)