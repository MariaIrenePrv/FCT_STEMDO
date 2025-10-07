# ### Ejercicio: Obtener ubicación de palabra
# Encuentra y muestra en pantalla el índice de la *primera* aparición de la palabra *"práctica"* en la siguiente frase:

# *"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."*

# Ahora muestra en pantalla el índice de la *última* aparición de la palabra *"práctica"*

# Declaro la variable frase 
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

# Declaro la variable primera y encontramos la primera palabra con el método .find
primera = frase.find("práctica")

# Imprimo la primera aparición de 'práctica'
print(f"La primera aparición de la palabra práctica es: {primera}")

# Declaro la variable ultima y encontramos la última palabra con el método .rfind
ultima = frase.rfind("práctica")

# Imprimo la última aparición de 'práctica'
print(f"La última aparición de la palabra práctica es: {ultima}")
