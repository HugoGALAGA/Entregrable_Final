# (Asumir que las clases Node y AVLTree están definidas arriba)
# (Opcionalmente, tener la clase BinarySearchTree simple del ejemplo anterior para comparación)

print("--- Ejemplo 1: Inserción Secuencial y Rebalanceo Automático (AVL vs BST vs AB) ---")
avl_tree = AVLTree()
# bst_tree = BinarySearchTree() # Uncomment to compare with a standard BST

# 1. Insertar valores secuenciales (peor caso para BST simple)
print("Insertando valores en un AVL: 10, 20, 30, 40, 50, 60") # Inserción ascendente
values = [10, 20, 30, 40, 50, 60]
for val in values:
    print(f"Insertando {val}...")
    avl_tree.insert(val)
    # bst_tree.insert(val) # Uncomment to insert into BST too
    # print(f"  Estado In-order AVL: {avl_tree.inorder_traversal()}") # Muestra el proceso si se desea

print("\nÁrbol AVL construido después de inserciones ascendentes:")
avl_tree.visualize() # Muestra In-order, Pre-order, Raíz, Altura, Balance Raíz

# Estructura del AVL esperada (ej. 40 como raíz, 20 en izq, 50 en der, etc.)
#      40
#     /  \
#    20   50
#   / \    \
#  10 30   60
# Altura = 3

print("\n--- Comparación con BST y AB General ---")
print("En un BST simple, insertar 10, 20, 30, 40, 50, 60 secuencialmente crearía un árbol degenerado (una lista enlazada hacia la derecha):")
# Estructura de BST simple degenerado:
# 10 -> 20 -> 30 -> 40 -> 50 -> 60
print("   10")
print("     \\")
print("      20")
print("        \\")
print("         30")
print("           \\")
print("            40")
print("              \\")
print("               50")
print("                 \\")
print("                  60")
print(f"Altura de este BST simple sería {len(values)} ({len(values)}) - O(n).")
# if 'bst_tree' in locals():
#    print(f"  Altura real del BST simple: {bst_tree.get_height(bst_tree.root)}")

print("\nUn Árbol Binario general (no BST) insertaría los nodos según su propia regla (ej. por niveles), sin importar el valor, y no se balancearía.")
print("No tendría la propiedad de que el In-order sea ordenado, ni garantizaría una altura baja.")
print("Su altura dependería enteramente del orden de inserción y la regla de construcción.")

print("\nEl AVL, sin embargo, detectó el desbalance durante la inserción y realizó rotaciones (automáticamente).")
print("Esto reestructuró el árbol para mantener la propiedad AVL (factor de balance -1, 0, o 1 en cada nodo).")
print(f"El resultado es un árbol con altura {avl_tree.get_height(avl_tree.root)}, que es O(log n) para {avl_tree.get_size()} nodos.")
print("Esta baja altura GARANTIZA un rendimiento logarítmico para las operaciones futuras.")

print("-" * 30)

# Insertar otra secuencia para mostrar rebalanceo diferente (ej. V invertida)
print("\n--- Demostración de Rebalanceo LR/RL (Inserción V invertida) ---")
avl_tree2 = AVLTree()
print("Insertando valores en un AVL: 30, 10, 20") # Causa un desbalance LR en la raíz después de insertar 20
print("Insertando 30...")
avl_tree2.insert(30)
print("Insertando 10...")
avl_tree2.insert(10)
print("Insertando 20...")
avl_tree2.insert(20)

print("\nÁrbol AVL construido después de 30, 10, 20:")
avl_tree2.visualize()
# Estructura esperada después de rebalanceo LR:
#    20
#   /  \
#  10   30
# Altura = 2, Balance = 0
print("Se realizó una rotación doble (Left-Right) para balancear el árbol. La raíz ahora es 20.")
print("-" * 30)
