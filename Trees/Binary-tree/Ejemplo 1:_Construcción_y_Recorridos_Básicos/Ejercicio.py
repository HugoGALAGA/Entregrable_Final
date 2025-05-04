# (Asumir que las clases Node y BinaryTree están definidas arriba)

print("--- Ejemplo 1: Construcción y Recorridos Básicos ---")
bst1 = BinaryTree()

# 1. Insertar nodos para construir el árbol
print("Insertando valores: 50, 30, 70, 20, 40, 60, 80")
bst1.insert(50)
bst1.insert(30)
bst1.insert(70)
bst1.insert(20)
bst1.insert(40)
bst1.insert(60)
bst1.insert(80)
print("Árbol construido.")

# Estructura esperada (visualización mental o dibujo):
#         50
#        /  \
#      30    70
#     / \  / \
#   20  40 60  80

# 2. Realizar diferentes recorridos
print("\nRecorrido en Orden (In-order):")
print(bst1.inorder_traversal()) # Debería imprimir los elementos ordenados

print("\nRecorrido Pre-orden (Pre-order):")
print(bst1.preorder_traversal()) # Útil para copiar el árbol

print("\nRecorrido Post-orden (Post-order):")
print(bst1.postorder_traversal()) # Útil para borrar el árbol

print("-" * 30)
