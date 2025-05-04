# Explicación del Ejemplo 3: Propiedades de Min/Max y Tamaño (BST vs AB)

Este ejemplo ilustra cómo la estructura específica de un BST permite encontrar los valores mínimo y máximo de manera muy eficiente, a diferencia de un Árbol Binario general, mientras que el cálculo del tamaño es similar.

**Funcionalidades Demostradas:**

1.  **`find_min` (Encontrar Mínimo):** En un BST, el valor más pequeño siempre se encuentra en el nodo más a la **izquierda**. Esto es una consecuencia directa de la propiedad de ordenamiento: todos los valores menores que un nodo están en su subárbol izquierdo. Para encontrar el mínimo, simplemente se sigue la rama izquierda desde la raíz hasta llegar a un nodo que no tiene hijo izquierdo. El dato de ese nodo es el mínimo.
    *   **Diferencia con AB General:** En un Árbol Binario general, el nodo con el valor mínimo podría estar en *cualquier* parte del árbol. No hay una dirección específica (siempre izquierda o siempre derecha) que te lleve al mínimo. Para encontrarlo, se necesitaría visitar cada nodo del árbol (usando un recorrido completo) y mantener un seguimiento del valor mínimo encontrado hasta el momento. La complejidad de `find_min` en un BST balanceado es O(log n) (siguiendo una rama), mientras que en un AB general es O(n) (visitando todos los nodos).

2.  **`find_max` (Encontrar Máximo):** De manera análoga a `find_min`, en un BST, el valor más grande siempre se encuentra en el nodo más a la **derecha**. Para encontrar el máximo, se sigue la rama derecha desde la raíz hasta llegar a un nodo que no tiene hijo derecho. El dato de ese nodo es el máximo.
    *   **Diferencia con AB General:** Similar al caso del mínimo, en un AB general, el nodo con el valor máximo puede estar en cualquier lugar. Encontrarlo requiere visitar todos los nodos (O(n)), a diferencia de la búsqueda O(log n) en un BST balanceado.

3.  **`get_size` (Obtener Tamaño):** Esta funcionalidad cuenta el número total de nodos en el árbol. La implementación común (recursiva o iterativa) implica visitar cada nodo del árbol una vez para contarlo.
    *   **Diferencia con AB General:** La forma de calcular el tamaño es fundamentalmente la misma tanto para un BST como para un Árbol Binario general. En ambos casos, se necesita visitar todos los nodos para obtener un conteo preciso, lo que resulta en una complejidad de O(n). Si el tamaño se mantiene como un contador que se actualiza en cada inserción o eliminación, esta operación podría ser O(1), pero la forma de calcularlo recorriendo el árbol es idéntica conceptualmente.

**En Resumen:**

Encontrar los valores extremos (mínimo y máximo) es una operación particularmente eficiente en un BST (O(log n) en promedio) debido a su estructura ordenada, que permite dirigirse directamente a la rama relevante. En un Árbol Binario general, esta operación requiere visitar todos los nodos (O(n)). El cálculo del tamaño, sin embargo, tiene una complejidad similar en ambos tipos de árboles (O(n) si se recorre).
