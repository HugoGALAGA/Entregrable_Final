# (Asumir que las clases Node y AVLTree están definidas arriba)
# (Opcionalmente, tener la clase BinarySearchTree simple del ejemplo anterior para comparación)

print("\n--- Ejemplo 2: Búsqueda y Eliminación Eficiente y con Altura Garantizada (AVL vs BST vs AB) ---")
avl_tree3 = AVLTree()
# bst_tree3 = BinarySearchTree() # Uncomment for comparison

# 1. Insertar nodos para construir un árbol AVL razonable
print("Insertando valores: 40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75")
values = [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]
for val in values:
    avl_tree3.insert(val)
    # bst_tree3.insert(val) # Uncomment for comparison

print("\nÁrbol AVL inicial:")
avl_tree3.visualize()
# if 'bst_tree3' in locals():
#    print("\nÁrbol BST simple inicial (estructura puede ser diferente, altura potencialmente mayor):")
#    bst_tree3.visualize() # Note: need visualize method in BST class for this

# 2. Búsqueda
print("\n--- Búsqueda (Search) ---")
print("Buscando 25:", avl_tree3.search(25)) # True
print("Buscando 99:", avl_tree3.search(99)) # False
print(f"La búsqueda de 25 en este AVL (altura {avl_tree3.get_height(avl_tree3.root)}) toma log_2({avl_tree3.get_size()}) pasos en el peor caso.")

print("\n--- Comparación de Búsqueda (AVL vs BST vs AB) ---")
print("En un BST, la búsqueda es O(log n) en promedio, pero O(n) en el peor caso si el árbol está degenerado.")
print("En un AVL, la búsqueda es **SIEMPRE** O(log n) porque el árbol *garantiza* una altura logarítmica.")
print("En un Árbol Binario general, la búsqueda es O(n) en el peor caso (recorrer todo el árbol) ya que no hay ordenamiento.")

# 3. Eliminación y Rebalanceo
print("\n--- Eliminación (Delete) ---")
print("In-order antes de eliminar:", avl_tree3.inorder_traversal())

print("\nEliminando 10 (nodo con 1 hijo, causa desbalance en 20?)...")
avl_tree3.delete(10)
print("Árbol AVL después de eliminar 10:")
avl_tree3.visualize() # La altura podría no cambiar, pero la estructura sí para mantener el balance

print("\nEliminando 60 (nodo con 2 hijos)...")
# 60 tiene 50 (left) y 70 (right). Sucesores in-order en subárbol derecho son 65, 70, 75. El mínimo es 65.
# 60 será reemplazado por 65, y 65 (original) eliminado de su posición. Puede causar desbalance.
avl_tree3.delete(60)
print("Árbol AVL después de eliminar 60:")
avl_tree3.visualize() # Muestra el nuevo In-order y cómo la altura se mantiene baja

print("\nIntentando eliminar 99 (inexistente)...")
avl_tree3.delete(99)
print("Árbol AVL después de intentar eliminar 99:")
avl_tree3.visualize() # Sin cambios

print("\n--- Comparación de Eliminación (AVL vs BST vs AB) ---")
print("La eliminación en un BST es O(log n) en promedio, O(n) en peor caso (búsqueda del nodo + sucesor/predecesor). No garantiza balance.")
print("La eliminación en un AVL es **SIEMPRE** O(log n). La complejidad adicional de buscar el sucesor/predecesor y rebalancear (rotaciones) sigue siendo logarítmica.")
print("En un Árbol Binario general, la eliminación es O(n) en peor caso (búsqueda del nodo), y no se preocupa por el orden o el balance.")

print("-" * 30)
