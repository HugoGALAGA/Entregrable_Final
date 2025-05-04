# (Asumir que las clases Node y BinaryTree están definidas arriba)

print("--- Ejemplo 3: Tamaño y Valores Extremos ---")
bst3 = BinaryTree()

# 1. Insertar algunos nodos
print("Insertando valores: 45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40, 50, 60, 70, 80")
values = [45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40, 50, 60, 70, 80]
for val in values:
    bst3.insert(val)
print("Árbol construido.")

# 2. Obtener el tamaño del árbol
print(f"\nTamaño del árbol (número de nodos): {bst3.get_size()}") # get_size

# 3. Encontrar los valores mínimo y máximo (BST propiedad)
print(f"Valor mínimo en el árbol: {bst3.find_min()}") # find_min
print(f"Valor máximo en el árbol: {bst3.find_max()}") # find_max

# 4. Insertar un nuevo mínimo y verificar
print("\nInsertando un nuevo valor mínimo: 5")
bst3.insert(5)
print(f"Nuevo tamaño del árbol: {bst3.get_size()}") # get_size
print(f"Nuevo valor mínimo en el árbol: {bst3.find_min()}") # find_min

# 5. Insertar un nuevo máximo y verificar
print("\nInsertando un nuevo valor máximo: 100")
bst3.insert(100)
print(f"Nuevo tamaño del árbol: {bst3.get_size()}") # get_size
print(f"Nuevo valor máximo en el árbol: {bst3.find_max()}") # find_max

print("-" * 30)
