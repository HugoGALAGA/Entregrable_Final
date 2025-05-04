# Explicación del Ejemplo 1: Inserción Secuencial y Rebalanceo Automático (AVL vs BST vs AB)

Este ejemplo demuestra la característica definitoria de un Árbol AVL: su capacidad para **auto-balancearse** durante la inserción, a diferencia de un BST simple o un Árbol Binario general. Se ilustra insertando datos en un orden que causaría un desbalance severo en un BST simple.

**Funcionalidades Demostradas:**

1.  **`insert` (con Rebalanceo Interno):** La operación `avl_tree.insert()` no solo coloca el nuevo nodo en la posición correcta según las reglas del BST (menor a la izquierda, mayor a la derecha), sino que, después de la inserción, recorre la ruta de regreso hacia la raíz. En cada nodo visitado, recalcula su altura y su factor de balance (`get_balance_factor`). Si el factor de balance excede el rango válido (-1, 0, 1), el algoritmo de inserción realiza **rotaciones** (`_rotate_left`, `_rotate_right` o combinaciones) para reestructurar el subárbol desbalanceado y restaurar la propiedad AVL. El ejemplo inserta números en orden ascendente, lo que forzaría múltiples rotaciones para evitar que el árbol se convierta en una lista enlazada (como sucedería en un BST simple).

2.  **`get_height` (Altura Mantenida):** Aunque no se llama explícitamente en el bucle de inserción, el método `get_height` (y `_update_height` internamente) es fundamental para el AVL. Cada nodo almacena su altura, y esta se actualiza después de cada inserción y después de cada rotación. El ejemplo muestra la altura final del AVL después de las inserciones secuenciales, demostrando que es significativamente menor (logarítmica) que la altura lineal que tendría un BST simple con los mismos datos insertados en el mismo orden.

3.  **`inorder_traversal` (Verificar Orden):** Este recorrido se utiliza para mostrar los elementos del árbol. En un AVL (como en un BST), el recorrido in-order siempre produce los elementos en orden ascendente. Esto verifica que, a pesar de las reestructuraciones por balanceo, la propiedad fundamental de Árbol Binario de Búsqueda se mantiene. La estructura física del árbol (vista con pre-order o una visualización completa) será muy diferente a la de un BST simple con la misma secuencia de inserciones, pero el orden lógico (in-order) es el mismo.

**Comparación (AVL vs BST vs AB):**

*   **vs AB General:** Un Árbol Binario general no tiene reglas de ordenamiento por valor ni mecanismos de balanceo. Insertar datos en orden ascendente simplemente los pondría en la siguiente posición disponible según su regla de construcción (ej. llenando por niveles), y el árbol podría tener una altura arbitraria y desbalanceada. Su recorrido in-order no estaría ordenado.
*   **vs BST Simple:** Un BST simple mantiene la propiedad de ordenamiento, pero *no* se auto-balancea. Insertar datos en orden ascendente (o descendente, o una V) crea un árbol degenerado (similar a una lista enlazada), donde la altura es O(n). Esto degrada el rendimiento de operaciones como búsqueda o eliminación a O(n) en el peor caso. El AVL supera esto añadiendo la lógica de balanceo.

**En Resumen:**

La clave de este ejemplo es la `insert` en un AVL. No es solo añadir un nodo; es añadirlo, verificar si se rompe la regla de balanceo en la ruta hacia la raíz, y si es así, realizar las rotaciones necesarias para restaurar el balance. Este proceso garantiza que la altura del árbol permanezca O(log n), incluso con secuencias de inserción adversas que colapsarían un BST simple. Esto es la principal diferencia y ventaja del AVL sobre un BST no balanceado.
