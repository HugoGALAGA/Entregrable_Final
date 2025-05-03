# (Asumir que las clases Node y LinkedList están definidas arriba)

print("\n--- Ejemplo 3: Manipulación y Tamaño de Colección Flexible ---")
my_collection = LinkedList()

# 1. Agregar elementos de diferentes maneras
print("Construyendo la colección...")
my_collection.append("Item 1") # Add to end
my_collection.append("Item 2") # Add to end
my_collection.prepend("Item 0") # Add to beginning
my_collection.append("Item 3") # Add to end
print("Colección actual:")
my_collection.display() # display

# 2. Verificar el tamaño actual (get_size)
print(f"Tamaño actual de la colección: {my_collection.get_size()}") # get_size

# 3. Eliminar elementos por valor (delete_node)
print("\nEliminando 'Item 2'...")
success = my_collection.delete_node("Item 2") # delete_node
if success: print("Eliminado con éxito.")
else: print("No se encontró para eliminar.")
print("Colección después de eliminar 'Item 2':")
my_collection.display() # display
print(f"Tamaño después de eliminar: {my_collection.get_size()}") # get_size

print("\nEliminando 'Item 0' (era el primero)...")
success = my_collection.delete_node("Item 0") # delete_node
if success: print("Eliminado con éxito.")
else: print("No se encontró para eliminar.")
print("Colección después de eliminar 'Item 0':")
my_collection.display() # display
print(f"Tamaño después de eliminar: {my_collection.get_size()}") # get_size

print("\nIntentando eliminar un elemento que ya no está ('Item 2')...")
success = my_collection.delete_node("Item 2") # delete_node
if success: print("Eliminado con éxito.")
else: print("No se encontró para eliminar.")
print("Colección después de intentar eliminar 'Item 2':")
my_collection.display() # display
print(f"Tamaño después de intentar eliminar: {my_collection.get_size()}") # get_size

# 4. Agregar más elementos
print("\nAgregando 'Item 4' al final...")
my_collection.append("Item 4") # append
print("Colección actualizada:")
my_collection.display() # display
print(f"Tamaño final: {my_collection.get_size()}") # get_size
