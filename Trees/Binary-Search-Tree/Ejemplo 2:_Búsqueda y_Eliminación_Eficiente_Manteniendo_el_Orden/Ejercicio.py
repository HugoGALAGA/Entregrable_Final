# (Asumir que las clases Node y BinarySearchTree están definidas arriba)

print("--- Ejemplo 2: Búsqueda y Eliminación Eficiente (BST vs AB) ---")
bst2 = BinarySearchTree()

# 1. Insertar nodos para construir el árbol
print("Insertando valores en un BST: 25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90")
values = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
for val in values:
    bst2.insert(val)
print("Árbol BST construido.")
print("In-order (ordenado):", bst2.inorder_traversal())

# 2. Búsqueda eficiente
print("\n--- Búsqueda (Search) ---")
print("Buscando 22:", bst2.search(22)) # True (presente)
print("Buscando 55:", bst2.search(55)) # False (ausente)
print("Buscando 4:", bst2.search(4))   # True (presente - hoja)
print("Buscando 25:", bst2.search(25)) # True (presente - raíz)

print("\n--- Comparación de Búsqueda (BST vs AB General) ---")
print("En un BST, la búsqueda compara el valor con el nodo actual y decide ir SOLO a la izquierda o SOLO a la derecha.")
print("Esto reduce el espacio de búsqueda a la mitad en cada paso (en promedio).")
print("Complejidad: O(log n) en promedio (árbol balanceado), O(n) en peor caso (árbol degenerado a lista).")
print("\nEn un Árbol Binario general, la búsqueda para saber si un elemento existe podría requerir visitar, en el peor caso, *todos* los nodos (O(n)) usando un recorrido como pre-orden, in-orden o post-orden si no se conoce la estructura específica.")


# 3. Eliminación manteniendo la propiedad BST
print("\n--- Eliminación (Delete) ---")
print("Estado inicial In-order:", bst2.inorder_traversal())

print("\nEliminando 22 (nodo con 1 hijo)...")
bst2.delete(22)
print("Estado después de eliminar 22 (In-order):", bst2.inorder_traversal()) # Debería estar ordenado y sin 22

print("\nEliminando 4 (nodo hoja)...")
bst2.delete(4)
print("Estado después de eliminar 4 (In-order):", bst2.inorder_traversal()) # Debería estar ordenado y sin 4

print("\nEliminando 50 (nodo con 2 hijos)...")
# 50 tiene 35 (left) y 70 (right). Sucesores in-order en subárbol derecho son 66, 70, 90. El mínimo es 66.
# 50 debería ser reemplazado por 66, y 66 (el original) eliminado de su posición.
bst2.delete(50)
print("Estado después de eliminar 50 (In-order):", bst2.inorder_traversal()) # Debería estar ordenado y sin 50

print("\nIntentando eliminar 99 (nodo inexistente)...")
bst2.delete(99)
print("Estado después de intentar eliminar 99 (In-order):", bst2.inorder_traversal()) # La lista no cambia

print("\n--- Comparación de Eliminación (BST vs AB General) ---")
print("En un BST, la eliminación es compleja porque debe mantener la propiedad de ordenamiento.")
print("Para nodos con 2 hijos, se debe encontrar el sucesor in-order (o predecesor), reemplazar el nodo a eliminar con él, y luego eliminar el sucesor de su posición original.")
print("Complejidad: O(log n) en promedio, O(n) en peor caso (debido a la búsqueda del sucesor/predecesor y la búsqueda del nodo a eliminar).")
print("\nEn un Árbol Binario general, la eliminación de un nodo *cualquiera* sin preocuparse por el ordenamiento puede ser más simple (por ejemplo, reemplazarlo por un hijo o el nodo más a la derecha en su subárbol), pero *no mantendría ninguna propiedad de ordenamiento* ni garantizaría que los recorridos específicos (como el in-order) tengan un significado particular.")

print("-" * 30)
