# Explicación del Ejemplo 1: Construcción y Recorridos Básicos

Este ejemplo se centra en la creación de un **Árbol Binario de Búsqueda (BST)** mediante la inserción de nodos y en demostrar las diferentes formas estándar de recorrer el árbol para acceder a los datos que contiene.

**Funcionalidades Demostradas:**

1.  **`insert` (Construcción):** La operación `bst1.insert()` construye el árbol. En un BST, cada nuevo dato se compara con el nodo actual: si es menor, se mueve al subárbol izquierdo; si es mayor, al subárbol derecho. Este proceso recursivo o iterativo continúa hasta encontrar una posición vacía (un `None`) donde se inserta el nuevo nodo. Esto asegura que el árbol mantenga la propiedad de BST (valor del nodo izquierdo < valor del nodo actual < valor del nodo derecho).

2.  **`inorder_traversal` (Recorrido en Orden):** Este recorrido sigue el patrón **Izquierda -> Raíz -> Derecha**. Visita primero todo el subárbol izquierdo, luego el nodo actual, y finalmente todo el subárbol derecho. La propiedad clave de un BST es que un recorrido en orden siempre produce los elementos del árbol en **orden ascendente y ordenado**. El ejemplo muestra cómo los números insertados se listan de menor a mayor.

3.  **`preorder_traversal` (Recorrido Pre-orden):** Este recorrido sigue el patrón **Raíz -> Izquierda -> Derecha**. Visita primero el nodo actual, luego todo el subárbol izquierdo, y finalmente todo el subárbol derecho. Este orden es útil, por ejemplo, para crear una copia exacta del árbol o para serializar la estructura del árbol.

4.  **`postorder_traversal` (Recorrido Post-orden):** Este recorrido sigue el patrón **Izquierda -> Derecha -> Raíz**. Visita primero todo el subárbol izquierdo, luego todo el subárbol derecho, y finalmente el nodo actual. Este orden es útil, por ejemplo, para liberar la memoria de un árbol (borrando primero los nodos hijos antes que el padre) o en la evaluación de expresiones.

**En Resumen:**

Este ejemplo fundamental ilustra cómo se construye un BST (`insert`) basándose en la comparación de valores y, crucialmente, cómo los diferentes tipos de recorridos (`inorder`, `preorder`, `postorder`) visitan los nodos en secuencias distintas, cada una con aplicaciones específicas. El recorrido en orden es particularmente significativo para los BSTs debido a que revela los datos ordenados.
