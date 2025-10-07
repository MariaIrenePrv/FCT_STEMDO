# ### Ejercicio: Verificación
# Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

# *Tierra mojada,*

# *mis recuerdos de viaje*

# *entre las lluvias*

# Declaro la variable haiku 
haiku= ( """Tierra mojada,

mis recuerdos de viaje

entre las lluvias""")

# Muestro por pantalla el valor de haiku
print(haiku)

# Verifico si la palabra "agua" no está en haiku
resultado = "agua" not in haiku

# Muestro por pantalla el resultado de la verificación 
print(resultado)