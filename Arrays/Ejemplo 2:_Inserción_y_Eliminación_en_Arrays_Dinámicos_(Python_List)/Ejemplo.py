# Ejemplo 2: Inserción y Eliminación en Arrays Dinámicos (Python List)

print("\n--- Ejemplo 2: Inserción y Eliminación ---")

array_dinamico = [10, 20, 30, 40, 50]
print(f"Array inicial: {array_dinamico}")
print(f"Tamaño inicial: {len(array_dinamico)}")

# 1. Inserción al final (append)
# Añadir un elemento al final es generalmente muy eficiente.
# En Python lists (arrays dinámicos), el 'append' es O(1) en tiempo promedio.
# Ocasionalmente, si el array necesita redimensionarse para hacer espacio, puede ser O(n),
# pero esto se amortiza a lo largo de muchas inserciones.
print(f"\n--- Inserción ---")
array_dinamico.append(60)
print(f"Después de append(60): {array_dinamico}") # Salida: [10, 20, 30, 40, 50, 60]
array_dinamico.append(70)
print(f"Después de append(70): {array_dinamico}") # Salida: [10, 20, 30, 40, 50, 60, 70]
print(f"Tamaño después de appends: {len(array_dinamico)}") # Salida: 7

# 2. Inserción en una posición específica (insert)
# Insertar en el inicio o en el medio del array es menos eficiente.
# Todos los elementos *después* del punto de inserción deben ser desplazados para hacer espacio.
# Esto tiene una complejidad de tiempo O(n), donde n es el número de elementos a desplazar.
array_dinamico.insert(0, 5) # Insertar 5 al principio (índice 0)
print(f"Después de insert(0, 5): {array_dinamico}") # Salida: [5, 10, 20, 30, 40, 50, 60, 70]

array_dinamico.insert(3, 28) # Insertar 28 en el índice 3
print(f"Después de insert(3, 28): {array_dinamico}") # Salida: [5, 10, 20, 28, 30, 40, 50, 60, 70]
print(f"Tamaño después de inserts: {len(array_dinamico)}") # Salida: 9


# 3. Eliminación del último elemento (pop sin argumento)
# Eliminar el último elemento es eficiente.
# Es una operación O(1).
print(f"\n--- Eliminación ---")
elemento_removido_final = array_dinamico.pop()
print(f"Elemento removido del final (pop()): {elemento_removido_final}") # Salida: 70
print(f"Después de pop(): {array_dinamico}") # Salida: [5, 10, 20, 28, 30, 40, 50, 60]
print(f"Tamaño después de pop(): {len(array_dinamico)}") # Salida: 8

# 4. Eliminación por índice (pop con argumento)
# Eliminar un elemento por su índice (especialmente al principio o en el medio) es menos eficiente.
# Todos los elementos *después* del elemento eliminado deben ser desplazados para llenar el hueco.
# Esto tiene una complejidad de tiempo O(n).
elemento_removido_inicio = array_dinamico.pop(0) # Eliminar el primer elemento (índice 0)
print(f"Elemento removido del inicio (pop(0)): {elemento_removido_inicio}") # Salida: 5
print(f"Después de pop(0): {array_dinamico}") # Salida: [10, 20, 28, 30, 40, 50, 60]

elemento_removido_medio = array_dinamico.pop(2) # Eliminar el elemento en el índice 2 (el 28)
print(f"Elemento removido del medio (pop(2)): {elemento_removido_medio}") # Salida: 28
print(f"Después de pop(2): {array_dinamico}") # Salida: [10, 20, 30, 40, 50, 60]
print(f"Tamaño después de pops: {len(array_dinamico)}") # Salida: 6

# 5. Eliminación por valor (remove)
# Eliminar la primera ocurrencia de un valor específico.
# Implica primero buscar el valor (O(n) en el peor caso) y luego eliminarlo,
# lo que requiere desplazar los elementos restantes (O(n)).
# La complejidad total es O(n).
try:
    array_dinamico.remove(40) # Eliminar la primera ocurrencia de 40
    print(f"Después de remove(40): {array_dinamico}") # Salida: [10, 20, 30, 50, 60]
    print(f"Tamaño después de remove: {len(array_dinamico)}") # Salida: 5
except ValueError as e:
    print(f"Error al intentar remove(40): {e}") # Ocurre si 40 no está en la lista

try:
     array_dinamico.remove(99) # Intentar eliminar un valor que no existe
except ValueError as e:
    print(f"Error al intentar remove(99) (valor no encontrado): {e}")

# 6. Limpiar el array
array_dinamico.clear()
print(f"\nDespués de clear(): {array_dinamico}") # Salida: []
print(f"Tamaño después de clear(): {len(array_dinamico)}") # Salida: 0


print("\n--- Fin Ejemplo 2 ---")
