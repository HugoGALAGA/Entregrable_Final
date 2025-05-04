# (Asumir que las clases Node y BinarySearchTree están definidas arriba)

print("--- Ejemplo 1: Inserción Ordenada y Recorrido Inorden Especial (BST vs AB) ---")
bst1 = BinarySearchTree()

# 1. Insertar nodos para construir el árbol
print("Insertando valores en un BST: 50, 30, 70, 20, 40, 60, 80")
bst1.insert(50)
bst1.insert(30)
bst1.insert(70)
bst1.insert(20)
bst1.insert(40)
bst1.insert(60)
bst1.insert(80)
print("Árbol BST construido.")

# Estructura esperada (visualización mental o dibujo - siempre ordenada):
#         50
#        /  \
#      30    70
#     / \  / \
#   20  40 60  80

# 2. Realizar el recorrido en Orden (In-order)
print("\nRecorrido en Orden (In-order) del BST:")
print(bst1.inorder_traversal()) # Debería imprimir los elementos ordenados

# 3. Comparación con un Árbol Binario general (conceptual)
print("\n--- Comparación con un Árbol Binario General (No BST) ---")
print("En un Árbol Binario general (no BST), la inserción no sigue reglas de ordenamiento.")
print("Por ejemplo, se podría insertar nivel por nivel, o siempre a la izquierda vacía.")
print("Un AB general con los mismos datos (50, 30, 70, 20, 40, 60, 80) pero insertados así:")
print("Insertando: 50 (root), 30 (left of 50), 70 (right of 50), 20 (left of 30),")
print("40 (left of 70), 60 (right of 20), 80 (right of 40) - ¡una estructura totalmente diferente!")
print("\nUna posible estructura de AB general con los mismos datos:")
#         50
#        /  \
#      30    70
#     / \  / \
#   20  60 40  80 <-- El orden es arbitrario/depende de la regla de inserción
print("\nEl recorrido In-order de este AB general *no estaría ordenado*:")
# Conceptual: Recorrido In-order: Izquierda(20) -> Raíz(30) -> Derecha(60) -> Raíz(50) -> Izquierda(40) -> Raíz(70) -> Derecha(80)
# Resultado In-order AB general: [20, 30, 60, 50, 40, 70, 80] <-- ¡No ordenado!
print("[Demostración conceptual: Recorrido In-order de un AB general no BST con estos datos podría ser: 20, 30, 60, 50, 40, 70, 80]")
print("\nLa clave es que en el BST, la propiedad de ordenamiento en la inserción *garantiza* que el In-order sea ordenado.")
print("-" * 30)
