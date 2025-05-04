# Explicación del Ejemplo 1: Inserción Ordenada y Recorrido Inorden Especial (BST vs AB)

Este ejemplo se centra en cómo la **propiedad de ordenamiento** de un **Árbol Binario de Búsqueda (BST)** influye fundamentalmente en su construcción (`insert`) y en el resultado de uno de sus recorridos (`inorder_traversal`), diferenciándolo de un Árbol Binario (AB) general.

**Funcionalidades Demostradas:**

1.  **`insert` (Construcción con Orden):** La operación `bst1.insert()` añade nuevos valores de forma que se mantiene la regla del BST: para cualquier nodo, los valores en su subárbol izquierdo son menores que su propio valor, y los valores en su subárbol derecho son mayores. Esto no ocurre en un Árbol Binario general, donde un nuevo nodo simplemente se añade en la siguiente posición disponible según alguna regla (por ejemplo, de arriba abajo, de izquierda a derecha para mantener la forma de un árbol completo), sin importar su valor en relación con otros nodos.

2.  **`inorder_traversal` (Recorrido que muestra el Orden):** Este recorrido visita los nodos en el orden **Izquierda -> Raíz -> Derecha**. En un BST, debido a la propiedad de ordenamiento, este recorrido siempre produce una secuencia de los datos almacenados en el árbol en **orden ascendente y ordenado**. El ejemplo demuestra esto imprimiendo los números insertados de menor a mayor.
    *   **Diferencia con AB General:** En un Árbol Binario general (no BST), el recorrido in-order *también* visita los nodos en el orden Izquierda -> Raíz -> Derecha. Sin embargo, como la posición de los nodos en un AB general no está ligada a su valor, el resultado del recorrido in-order *no estará ordenado*. El ejemplo conceptual ilustra cómo un AB general con los mismos datos podría tener una estructura diferente y su recorrido in-order no sería secuencial.

**En Resumen:**

La inserción en un BST es más "inteligente" que en un AB general, ya que coloca los nodos basándose en su valor para mantener una estructura ordenada. Esta propiedad de ordenamiento es la que confiere al recorrido in-order de un BST su característica especial de producir una lista ordenada de elementos, algo que no sucede en un AB general.
