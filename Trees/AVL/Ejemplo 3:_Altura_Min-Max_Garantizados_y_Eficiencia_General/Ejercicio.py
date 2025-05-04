# (Asumir que las clases Node y AVLTree están definidas arriba)
# (Opcionalmente, tener la clase BinarySearchTree simple del ejemplo anterior para comparación)

print("\n--- Ejemplo 3: Altura, Min/Max Garantizados y Eficiencia General (AVL vs BST vs AB) ---")
avl_tree4 = AVLTree()
bst_tree4 = BinarySearchTree() # Usaremos un BST simple para la comparación de altura

# 1. Insertar nodos para construir un árbol
print("Insertando valores (mezclados para intentar mantener un BST no degenerado, pero no garantizado): 50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 75")
values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 75]
for val in values:
    avl_tree4.insert(val)
    bst_tree4.insert(val)

print("\nÁrbol AVL después de inserciones:")
avl_tree4.visualize()
print(f"Altura teórica logarítmica (log2 de {avl_tree4.get_size()} nodos): aprox {import math; math.log2(avl_tree4.get_size()):.2f}")

print("\nÁrbol BST simple después de las mismas inserciones:")
bst_tree4.visualize() # Mostrará una estructura diferente y posiblemente mayor altura

print("\n--- Altura Garantizada (AVL vs BST vs AB) ---")
print("Un BST simple puede tener altura O(n) en el peor caso (inserciones ordenadas).")
print("Un Árbol Binario general no tiene garantía de altura basada en el número de nodos.")
print("Un AVL **garantiza** que su altura máxima sea O(log n) (factor logarítmico del número de nodos).")
print(f"Altura del AVL ({avl_tree4.get_height(avl_tree4.root)}) vs Altura del BST simple ({bst_tree4.get_height(bst_tree4.root)}) después de estas inserciones.") # La diferencia puede ser menor con inserciones mixtas, pero con secuenciales es drástica.

# 2. Encontrar Min y Max (aprovechando la altura O(log n) garantizada)
print("\n--- Encontrar Mínimo y Máximo ---")
print(f"Valor mínimo en el AVL: {avl_tree4.find_min()}") # Debería ser 10
print(f"Valor máximo en el AVL: {avl_tree4.find_max()}") # Debería ser 80

print("\n--- Comparación de Min/Max Finding (AVL vs BST vs AB) ---")
print("En un BST, Min/Max se encuentran recorriendo la rama izquierda/derecha. Es O(altura).")
print("En un AB general, se necesita recorrer todo el árbol (O(n)) para encontrar Min/Max.")
print("En un AVL, como la altura es **garantizadamente** O(log n), encontrar Min/Max es **SIEMPRE** O(log n).")

# 3. Tamaño (similar en ambos, O(n) si se calcula recorriendo)
print("\n--- Tamaño (Get Size) ---")
print(f"Tamaño del AVL: {avl_tree4.get_size()}")
print(f"Tamaño del BST: {bst_tree4.get_size()}")

print("\n--- Comparación de Tamaño (AVL vs BST vs AB) ---")
print("Calcular el tamaño recorriendo todos los nodos es O(n) en AB, BST y AVL si no se mantiene un contador.")
print("Mantener un contador actualizado durante insert/delete permitiría O(1).")
print("Esta operación no es donde AVL muestra su principal ventaja, a menos que la implementación la haga O(1).")

print("-" * 30)
