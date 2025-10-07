# ### Ejercicio: Agrupación y Manipulación de Sets

# 1. **Une los siguientes sets** en uno solo llamado `mi_set_3`:

#    ```python
#    set1 = {1, 2, "tres", "cuatro"}
#    set2 = {"tres", 4, 5}
#    ```

# 2. **Agrega** el nombre "`Damián`" al set `mi_set_3` utilizando métodos de sets.

# 3. Elimina un elemento al **azar** del set `mi_set_3`.

# Declaro los sets 1 y 2.
set1 = {1, 2, "tres", "cuatro"}
set2 = {"tres", 4, 5}

# Uno los dos sets en uno solo
mi_set_3= set1.union(set2)

# Imprimo el valor de 'mi_set_3' 
print(mi_set_3)

# Añado el nombre 'Damián' al set
mi_set_3.add("Damián")

# Imprimo el cambio por pantalla
print(mi_set_3)

# Elimino un elemento al azar del set 'mi_set_3'
mi_set_3.pop()

# Imprimo por pantalla el cambio
print(mi_set_3)