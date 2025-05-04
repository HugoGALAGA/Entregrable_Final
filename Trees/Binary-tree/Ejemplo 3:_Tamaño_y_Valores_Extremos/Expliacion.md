# Explicación del Ejemplo 3: Tamaño y Valores Extremos

Este ejemplo ilustra cómo obtener información agregada sobre un Árbol Binario de Búsqueda: cuántos elementos contiene y cuáles son los valores mínimo y máximo almacenados.

**Funcionalidades Demostradas:**

1.  **`insert` (Construcción):** Nuevamente, se insertan nodos para formar el BST, respetando la propiedad de ordenamiento. La diversidad de los valores insertados ayuda a crear un árbol con una estructura más variada.

2.  **`get_size` (Obtener tamaño):** El método `bst3.get_size()` calcula el número total de nodos en el árbol. La implementación recursiva `_get_size_recursive` muestra cómo se puede obtener esto: si un nodo es `None`, el tamaño es 0; de lo contrario, el tamaño es 1 (el nodo actual) más el tamaño de su subárbol izquierdo más el tamaño de su subárbol derecho. Este proceso visita efectivamente cada nodo una vez para contarlo. El ejemplo muestra el tamaño inicial y cómo cambia al insertar nuevos nodos.

3.  **`find_min` (Encontrar el valor mínimo):** En un BST, el valor más pequeño siempre se encuentra en el nodo más a la **izquierda** del árbol. Esto se debe a que los valores menores que un nodo siempre se colocan en su subárbol izquierdo. Para encontrar el mínimo, se comienza en la raíz y se sigue la rama izquierda hasta llegar a un nodo que no tenga un hijo izquierdo (`current_node.left` es `None`). El dato de ese nodo es el mínimo. El ejemplo demuestra cómo se encuentra el mínimo inicial y cómo se actualiza al insertar un valor aún menor.

4.  **`find_max` (Encontrar el valor máximo):** De manera análoga a `find_min`, el valor más grande en un BST siempre se encuentra en el nodo más a la **derecha** del árbol. Para encontrar el máximo, se comienza en la raíz y se sigue la rama derecha hasta llegar a un nodo que no tenga un hijo derecho (`current_node.right` es `None`). El dato de ese nodo es el máximo. El ejemplo demuestra cómo se encuentra el máximo inicial y cómo se actualiza al insertar un valor aún mayor.

**En Resumen:**

Este ejemplo destaca cómo la estructura ordenada de un BST permite encontrar eficientemente los valores extremos (`find_min`, `find_max`) simplemente recorriendo una rama del árbol (O(altura del árbol)), no necesitando visitar todos los nodos. También muestra una forma común (`get_size` recursivo) de obtener el número total de nodos, una operación que sí requiere visitar cada nodo.
