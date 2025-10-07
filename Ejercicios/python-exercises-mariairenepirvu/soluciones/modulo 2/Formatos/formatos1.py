# ### Ejercicio: Imprimir una Expresión en Pantalla
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# > Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# La cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.


# Solicita la cantidad de puntos anteriores y nuevos. Además convertimos a numero entero
puntos_anteriores = int(input("¿Cuántos puntos tienes?: "))  
puntos_nuevos = int(input("¿Cuántos puntos ganaste?: "))  

# Calcula los puntos totales
puntos_totales = puntos_anteriores + puntos_nuevos


print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos.")
