# (Asumir que las clases Node y LinkedList están definidas arriba)

print("\n--- Ejemplo 2: Gestión de Historial Reciente ---")
history = LinkedList()

# 1. Agregar elementos al historial (prepend)
print("Visitando páginas/items (agregando al principio)...")
history.prepend("Item C") # Más reciente
history.prepend("Item B")
history.prepend("Item A") # Menos reciente (inicialmente)
print("Historial actual (más reciente al principio):")
history.display() # display

# 2. Agregar otro elemento al principio
print("\nVisitando 'Item D' (agregando al principio)...")
history.prepend("Item D")
print("Historial actualizado:")
history.display() # display

# 3. Verificar el tamaño del historial (get_size)
print(f"\nNúmero de elementos en el historial: {history.get_size()}") # get_size

# 4. Buscar un elemento específico en el historial (search)
print("\nBuscando 'Item B' en el historial...")
print(f"¿'Item B' está en el historial? {history.search('Item B')}") # search
print("Buscando 'Item E' en el historial...")
print(f"¿'Item E' está en el historial? {history.search('Item E')}") # search

# 5. Demostrar que si un elemento visitado ya existe, podría re-agregarse al principio
# (En una implementación real, primero se eliminaría el viejo, luego se agregaría el nuevo)
print("\nVisitando 'Item B' de nuevo (simple prepend para demostración)...")
history.prepend("Item B")
print("Historial actualizado:")
history.display() # display
print(f"Número de elementos después de re-visitar: {history.get_size()}") # get_size
