# Explicación del Ejemplo 2: Búsqueda de Elementos

Este ejemplo se enfoca en una de las operaciones más comunes y eficientes de un Árbol Binario de Búsqueda: la **búsqueda de un elemento**. Aprovecha la estructura ordenada del BST para encontrar un valor o determinar si no está presente.

**Funcionalidades Demostradas:**

1.  **`insert` (Construcción):** Aunque el enfoque principal es la búsqueda, primero necesitamos construir el árbol insertando algunos datos. La inserción sigue las reglas del BST (menor va a la izquierda, mayor va a la derecha), lo cual es fundamental para que la búsqueda sea eficiente.

2.  **`search` (Buscar):** La operación `bst2.search()` toma un valor y busca si existe un nodo con ese dato en el árbol. En un BST, esta búsqueda comienza en la raíz. Si el valor buscado es igual al dato del nodo actual, se encuentra. Si es menor, la búsqueda continúa *solo* en el subárbol izquierdo. Si es mayor, la búsqueda continúa *solo* en el subárbol derecho. Este proceso descarta aproximadamente la mitad de los nodos restantes en cada paso (en un árbol balanceado), haciendo la búsqueda muy rápida (complejidad promedio O(log n)). El ejemplo muestra cómo se obtienen resultados `True` para valores presentes y `False` para valores ausentes, siguiendo esta lógica de comparación.

**En Resumen:**

Este ejemplo subraya la eficiencia de la operación de búsqueda en un BST. Gracias a la propiedad de ordenamiento mantenida durante la inserción, buscar un elemento no requiere visitar todos los nodos (como sería necesario en una lista enlazada o un árbol binario general no ordenado), sino que se puede dirigir la búsqueda hacia el subárbol relevante, reduciendo significativamente el tiempo de búsqueda, especialmente en árboles grandes.
