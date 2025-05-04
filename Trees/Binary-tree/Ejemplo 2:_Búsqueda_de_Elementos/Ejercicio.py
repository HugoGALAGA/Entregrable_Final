# (Asumir que las clases Node y BinaryTree están definidas arriba)

print("--- Ejemplo 2: Búsqueda de Elementos ---")
bst2 = BinaryTree()

# 1. Insertar algunos nodos
print("Insertando valores: 15, 10, 20, 8, 12, 17, 25")
bst2.insert(15)
bst2.insert(10)
bst2.insert(20)
bst2.insert(8)
bst2.insert(12)
bst2.insert(17)
bst2.insert(25)
print("Árbol construido.")

# Estructura esperada:
#          15
#         /  \
#       10    20
#      / \   / \
#     8  12 17  25

# 2. Buscar diferentes valores
print("\nBuscando valores...")
value1 = 20
print(f"¿El valor {value1} existe en el árbol? {bst2.search(value1)}") # Debería ser True

value2 = 10
print(f"¿El valor {value2} existe en el árbol? {bst2.search(value2)}") # Debería ser True

value3 = 99
print(f"¿El valor {value3} existe en el árbol? {bst2.search(value3)}") # Debería ser False

value4 = 1
print(f"¿El valor {value4} existe en el árbol? {bst2.search(value4)}") # Debería ser False

value5 = 15
print(f"¿El valor {value5} existe en el árbol? {bst2.search(value5)}") # Debería ser True (la raíz)

print("-" * 30)
