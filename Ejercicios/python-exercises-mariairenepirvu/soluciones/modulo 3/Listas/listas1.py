# ### Ejercicio: Gestión de listas
# #### Crea una lista con 5 elementos, dentro de la variable `mi_lista`.

# *Puedes incluir strings, booleanos, números, etc.*

# Agrega el elemento "motocicleta"

# Quitar el tercer elemento de la lista y almacénalo en una variable llamada "eliminado"

# Creo una lista con 5 elementos
mi_lista = ['Motocicleta', '800', 'True', '5.6', ['rojo', 'negro', 'azul'] ]
# Imprimo el tipo 
print(type(mi_lista))
# Imprimo el valor de 'mi_lista'
print(mi_lista)

# Almaceno el tercer elemento en una variable y lo elimino con .pop
eliminado = mi_lista.pop(2)

# Imprimo el valor de 'mi_lista'
print(mi_lista)

# Imprimo el valor de 'eliminado'
print(f"El elemento eliminado es: {eliminado}")
