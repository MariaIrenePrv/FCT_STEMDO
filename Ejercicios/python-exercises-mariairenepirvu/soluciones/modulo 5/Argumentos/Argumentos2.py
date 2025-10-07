# ### Ejercicio: Suma absoluta
# Crea una función llamada `suma_absolutos`, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*numeros):
     return sum(abs(n) for n in numeros)


 # Ejemplos (mismos números que en suma_cuadrados)
print(suma_absolutos(1, -2, 3))  
print(suma_absolutos(2, -2, 2)) 
print(suma_absolutos(-5, -5,))  
print(suma_absolutos(7, -8, 9, -10))
