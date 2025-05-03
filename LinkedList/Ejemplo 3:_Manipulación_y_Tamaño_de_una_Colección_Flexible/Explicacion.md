# Explicación del Ejemplo 3: Manipulación y Tamaño de una Colección Flexible

Este ejemplo combina varias operaciones para demostrar la naturaleza dinámica de una lista enlazada como una colección donde los elementos pueden ser añadidos y eliminados flexiblemente, y donde se puede consultar su tamaño.

**Funcionalidades Demostradas:**

1.  **`append` (Agregar al final):** Utilizado con `my_collection.append()`. Añade elementos al final de la lista. Como se explicó antes, implica recorrer hasta el último nodo y enlazar el nuevo.

2.  **`prepend` (Agregar al principio):** Utilizado con `my_collection.prepend()`. Añade elementos al principio de la lista, lo cual es una operación rápida (O(1)).

3.  **`delete_node` (Eliminar por valor):** Utilizado con `my_collection.delete_node()`. Muestra cómo eliminar nodos tanto del principio (como "Item 0") como del medio (como "Item 2"). También demuestra qué sucede cuando se intenta eliminar un elemento que no está presente en la lista.

4.  **`get_size` (Obtener tamaño):** Llamado con `my_collection.get_size()` en varios puntos. Muestra cómo el tamaño de la lista cambia dinámicamente a medida que se añaden y eliminan elementos. `get_size` recorre la lista para contar los nodos.

5.  **`display` (Mostrar):** Usado después de cada operación de modificación o en puntos clave para mostrar el estado actual de la lista y verificar que las operaciones se realizaron correctamente y que el orden se mantiene como se espera.

**En Resumen:**

Este ejemplo proporciona una visión más completa de la manipulación de una lista enlazada al combinar inserciones al principio y al final con eliminaciones en diferentes posiciones lógicas (principio, medio). Destaca cómo la estructura de la lista enlazada permite modificarla eficientemente (especialmente en los extremos, O(1), o al eliminar un nodo conocido si tienes la referencia al anterior, O(1), aunque nuestra `delete_node` es O(n) porque busca primero) y cómo se puede consultar su tamaño (`get_size`, O(n) en esta implementación simple).
