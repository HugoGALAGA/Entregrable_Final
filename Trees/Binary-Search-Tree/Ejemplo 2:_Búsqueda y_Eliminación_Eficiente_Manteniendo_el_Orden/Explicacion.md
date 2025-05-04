# Explicación del Ejemplo 2: Búsqueda y Eliminación Eficiente Manteniendo el Orden (BST vs AB)

Este ejemplo resalta la eficiencia de la búsqueda en un BST y la complejidad inherente de la eliminación, ya que ambas operaciones deben preservar la propiedad de ordenamiento que define al árbol.

**Funcionalidades Demostradas:**

1.  **`search` (Búsqueda Eficiente):** La operación `bst2.search()` busca un valor específico. Gracias a la propiedad del BST, en cada nodo, se compara el valor buscado con el valor del nodo actual: si es menor, la búsqueda se limita al subárbol izquierdo; si es mayor, al subárbol derecho. Esto permite descartar una gran parte del árbol en cada paso.
    *   **Diferencia con AB General:** En un Árbol Binario general, para saber si un elemento existe, no hay un patrón de ordenamiento que guíe la búsqueda. En el peor caso, se debería realizar un recorrido completo del árbol (como pre-orden, in-orden, o post-orden) y comparar el valor buscado con cada nodo visitado hasta encontrarlo o agotar el árbol. La complejidad de búsqueda en un BST bien formado es O(log n) en promedio, mientras que en un AB general es O(n) en el peor caso.

2.  **`delete` (Eliminación Manteniendo BST):** La operación `bst2.delete()` elimina un nodo con un valor dado. Esta es una operación más compleja que en un AB general si se quiere mantener la propiedad del BST. Se deben considerar tres casos para el nodo a eliminar:
    *   **0 hijos (hoja):** Simplemente se desvincula del padre.
    *   **1 hijo:** El padre del nodo a eliminar se conecta directamente con el único hijo de este.
    *   **2 hijos:** Este es el caso más complejo. Para mantener la propiedad BST, el nodo eliminado debe ser reemplazado por otro nodo de su subárbol que mantenga el orden. La práctica común es usar el **sucesor in-order** (el nodo con el valor más pequeño en el subárbol derecho) o el predecesor in-order. El sucesor se encuentra y se copia su valor al nodo que se desea eliminar, y luego se elimina recursivamente el sucesor de su posición original (que siempre será un nodo con 0 o 1 hijo, manejando los casos anteriores).
    *   **Diferencia con AB General:** La eliminación en un AB general no tiene la restricción de mantener la propiedad de ordenamiento por valor. Un nodo puede ser reemplazado de formas más simples (ej. por uno de sus hijos, o el último nodo en un recorrido) sin preocuparse por cómo esto afecta a la relación de orden entre nodos. La complejidad de la eliminación en un BST es O(log n) en promedio (incluyendo la búsqueda y la posible búsqueda del sucesor/predecesor), mientras que en un AB general, la eliminación puede ser más rápida si no se mantiene una estructura particular, pero no conservaría el ordenamiento de los valores.

**En Resumen:**

La búsqueda en un BST es significativamente más rápida que en un AB general debido a su estructura ordenada. La eliminación en un BST es más compleja que en un AB general porque debe realizarse de manera que la propiedad de ordenamiento se preserve, a menudo involucrando la reestructuración del árbol en la zona afectada.
