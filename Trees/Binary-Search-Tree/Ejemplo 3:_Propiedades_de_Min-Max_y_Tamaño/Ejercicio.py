# (Asumir que las clases Node y BinarySearchTree están definidas arriba)

print("--- Ejemplo 3: Propiedades de Min/Max y Tamaño (BST vs AB) ---")
bst3 = BinarySearchTree()

# 1. Insertar nodos
print("Insertando valores en un BST: 40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75")
values = [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]
for val in values:
    bst3.insert(val)
print("Árbol BST construido.")
print("In-order:", bst3.inorder_traversal())

# 2. Obtener tamaño
print(f"\nTamaño del árbol (número de nodos): {bst3.get_size()}") # get_size

# 3. Encontrar Min y Max (aprovechando la propiedad BST)
print("\n--- Encontrar Mínimo y Máximo ---")
print(f"Valor mínimo en el árbol: {bst3.find_min()}") # find_min (debe ser 5)
print(f"Valor máximo en el árbol: {bst3.find_max()}") # find_max (debe ser 75)

# 4. Insertar un nuevo mínimo y un nuevo máximo
print("\nInsertando nuevo mínimo (1) y nuevo máximo (100)...")
bst3.insert(1)
bst3.insert(100)
print("Árbol actualizado. In-order:", bst3.inorder_traversal())
print(f"Nuevo tamaño del árbol: {bst3.get_size()}")
print(f"Nuevo valor mínimo en el árbol: {bst3.find_min()}")   # find_min (debe ser 1)
print(f"Nuevo valor máximo en el árbol: {bst3.find_max()}")   # find_max (debe ser 100)

print("\n--- Comparación de Min/Max Finding (BST vs AB General) ---")
print("En un BST, el mínimo siempre está en el nodo más a la izquierda y el máximo en el más a la derecha.")
print("Encontrarlos solo requiere seguir una única rama del árbol (ir siempre a la izquierda para min, siempre a la derecha para max).")
print("Complejidad: O(altura del árbol), que es O(log n) en promedio para un BST balanceado, O(n) en peor caso.")
print("\nEn un Árbol Binario general, no existe esta propiedad de ordenamiento por rama.")
print("Para encontrar el mínimo o máximo valor, se debería recorrer *todo* el árbol (usando pre-orden, in-orden, post-orden o por niveles) y comparar cada valor encontrado para llevar un registro del mínimo y máximo global.")
print("Complejidad: O(n) en todos los casos, ya que se deben visitar todos los nodos.")
print("\nLa funcionalidad get_size (contar nodos) es similar en ambos tipos de árboles (requiere visitar todos los nodos, O(n) en implementaciones básicas recursivas o iterativas).")

print("-" * 30)
