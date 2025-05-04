# Explicación del Ejemplo 3: Altura, Min/Max Garantizados y Eficiencia General (AVL vs BST vs AB)

Este ejemplo consolida la comprensión del beneficio del balanceo AVL mostrando cómo la altura logarítmica garantizada impacta la eficiencia de operaciones como encontrar los valores mínimo y máximo, y reafirmando la diferencia de altura con un BST simple.

**Funcionalidades Demostradas:**

1.  **`get_height` (Altura Logarítmica Garantizada):** Se insertan varios nodos en el AVL. A pesar de que el orden de inserción puede hacer que la estructura sea diferente de un BST simple con los mismos datos, el AVL realiza rebalanceos internos para asegurar que la altura total del árbol permanezca baja, con un límite superior de O(log n). Se compara explícitamente la altura del AVL con la de un BST simple construido con los mismos datos, mostrando que el AVL tiende a ser más bajo (o significativamente más bajo en casos de inserciones adversas).

2.  **`find_min` y `find_max` (O(log n) Garantizado):** En un AVL (que es un BST), el valor mínimo se encuentra recorriendo la rama izquierda y el máximo recorriendo la rama derecha. La diferencia clave con un BST simple es que, como el AVL *garantiza* una altura O(log n), la longitud de estas ramas (y por lo tanto el número de nodos visitados) es también O(log n) en el peor caso. Encontrar el mínimo o el máximo es, por lo tanto, una operación **siempre** eficiente (O(log n)) en un AVL.
    *   **Comparación:** En un BST simple, aunque la lógica de `find_min`/`find_max` también es seguir una rama, la longitud de esa rama podría ser O(n) en un árbol degenerado (peor caso), haciendo que la operación sea O(n). En un AB general, encontrar el mínimo o el máximo requiere visitar *todos* los nodos (O(n)) porque no hay una propiedad de ordenamiento que concentre los valores extremos en ubicaciones predecibles.

3.  **`get_size` (O(n) en esta implementación):** Se incluye para mostrar el número total de nodos. Notablemente, esta operación (si se implementa recorriendo el árbol) tiene una complejidad de O(n) tanto en AB, BST y AVL. No es una operación que se beneficie intrínsecamente del balanceo o del ordenamiento (a menos que se mantenga un contador externo).

**Comparación (AVL vs BST vs AB):**

*   **vs AB General:** AVL es un BST auto-balanceado. ABs generales no tienen ordenamiento ni balanceo. Operaciones como buscar Min/Max son O(n) en AB, O(log n) garantizado en AVL.
*   **vs BST Simple:** La principal diferencia radica en la **garantía** de rendimiento. BSTs simples tienen O(log n) *en promedio* para muchas operaciones (búsqueda, inserción, eliminación, min/max) pero O(n) *en el peor caso* debido a la posible degeneración. AVL, al mantener activamente el balance, elimina el peor caso O(n) para estas operaciones, haciéndolas **siempre** O(log n). Esto tiene un costo en complejidad de implementación (para las rotaciones) y un ligero overhead en las operaciones de inserción/eliminación (para verificar y rebalancear), pero la ganancia en rendimiento garantizado es significativa para grandes conjuntos de datos y cargas de trabajo dinámicas.

**En Resumen:**

El AVL se destaca porque, aunque comparte la lógica de búsqueda de un BST (gracias a ser un BST), su mecanismo de auto-balanceo (`insert`, `delete`) garantiza que la altura del árbol se mantenga siempre en O(log n). Esto se traduce en una **garantía de rendimiento** O(log n) para operaciones críticas como `search`, `insert`, `delete`, `find_min`, y `find_max`, sin importar el orden de inserción o eliminación. Un BST simple ofrece solo un rendimiento promedio O(log n) con un peor caso de O(n), y un AB general no ofrece ninguna garantía basada en el número de nodos. El AVL es la elección cuando se necesita un rendimiento logarítmico consistente y garantizado.
