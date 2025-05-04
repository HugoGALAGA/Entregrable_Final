# Explicación del Ejemplo 2: Búsqueda y Eliminación Eficiente y con Altura Garantizada (AVL vs BST vs AB)

Este ejemplo se enfoca en cómo la propiedad de altura O(log n) garantizada por el balanceo AVL impacta directamente en la eficiencia de las operaciones de búsqueda y eliminación.

**Funcionalidades Demostradas:**

1.  **`search` (Eficiencia O(log n) Garantizada):** La operación `avl_tree3.search()` busca un valor siguiendo la misma lógica de un BST: ir a la izquierda si el valor es menor, a la derecha si es mayor. La diferencia crucial es que, dado que el AVL *garantiza* que la altura del árbol es siempre O(log n), la búsqueda de cualquier elemento nunca requerirá visitar más de O(log n) nodos en el peor caso.
    *   **Comparación:** En un BST simple, la búsqueda es O(log n) *en promedio* (si el árbol está relativamente balanceado), pero puede degradarse a O(n) en el peor caso (árbol degenerado). En un AB general, la búsqueda para encontrar un elemento arbitrario es típicamente O(n) en el peor caso, ya que no hay una estructura ordenada que permita reducir el espacio de búsqueda rápidamente.

2.  **`delete` (con Rebalanceo Interno):** La operación `avl_tree3.delete()` elimina un nodo. Similar a la inserción, después de realizar la eliminación lógica (manejando los casos de 0, 1 o 2 hijos como en un BST), el algoritmo verifica la altura y el factor de balance en cada nodo en la ruta de regreso a la raíz. Si se detecta un desbalance, se realizan las rotaciones necesarias para restaurar la propiedad AVL. El ejemplo muestra la eliminación de diferentes tipos de nodos (con 1 hijo, con 2 hijos) y cómo el árbol se reestructura para mantener su balance y, por lo tanto, su altura baja.

3.  **`get_height` (Altura Garantizada):** Se utiliza después de las eliminaciones para confirmar que la altura del árbol sigue siendo logarítmica en relación con el número actual de nodos. Esto valida que el proceso de rebalanceo tras la eliminación es efectivo.

**Comparación (AVL vs BST vs AB):**

*   **vs AB General:** La búsqueda y eliminación en un AB general son O(n) en el peor caso, ya que no hay ordenamiento ni garantía de altura baja.
*   **vs BST Simple:** La búsqueda y eliminación en un BST simple son O(log n) *en promedio*, pero O(n) *en el peor caso* si el árbol está desbalanceado. La lógica de eliminación es similar (especialmente para nodos con 2 hijos, usando el sucesor/predecesor), pero el BST simple *no* realiza rebalanceo después, por lo que puede quedar desbalanceado. El AVL añade la complejidad del rebalanceo (rotaciones) para garantizar el rendimiento O(log n) incluso en el peor caso.

**En Resumen:**

El valor principal de un AVL sobre un BST simple se ve claramente en la garantía de rendimiento de sus operaciones principales. La búsqueda y la eliminación en un AVL son **siempre** O(log n) porque el árbol *mantiene activamente* una altura logarítmica mediante rebalanceos (`insert` y `delete`). Un BST simple no ofrece esta garantía, ya que su altura puede ser O(n) en el peor caso, degradando el rendimiento de sus operaciones.
