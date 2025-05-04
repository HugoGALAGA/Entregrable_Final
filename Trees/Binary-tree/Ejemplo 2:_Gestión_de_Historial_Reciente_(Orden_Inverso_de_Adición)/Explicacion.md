# Explicación del Ejemplo 2: Gestión de Historial Reciente

Este ejemplo modela un historial de elementos vistos (como páginas web, productos, etc.) donde el elemento que se acaba de ver es siempre el más relevante y, por lo tanto, se coloca al principio del historial. Esto aprovecha la eficiencia de la operación de agregar al principio en una lista enlazada.

**Funcionalidades Demostradas:**

1.  **`prepend` (Agregar al principio):** La operación `history.prepend()` añade un nuevo nodo (el elemento visitado más recientemente) al *inicio* de la lista. Esto es muy eficiente en una lista enlazada simple porque solo requiere cambiar la referencia de la `head` y hacer que el nuevo nodo apunte a la antigua cabeza. No se necesita recorrer toda la lista.

2.  **`display` (Mostrar):** Similar al ejemplo anterior, `history.display()` recorre la lista desde la `head` para mostrar los elementos en orden. Dado que `prepend` añade al principio, el `display` mostrará los elementos en orden cronológico *inverso* de adición (el más reciente primero).

3.  **`search` (Buscar):** La función `history.search()` recorre la lista desde la `head` hasta encontrar un nodo cuyo dato coincida con la `key` buscada. Devuelve `True` si lo encuentra y `False` si llega al final de la lista sin encontrarlo. Esto demuestra cómo buscar un elemento específico dentro de la estructura enlazada.

4.  **`get_size` (Obtener tamaño):** El método `history.get_size()` recorre la lista nodo por nodo, contando cuántos nodos hay. Devuelve el contador al final. Esto permite saber cuántos elementos hay actualmente en la lista. A diferencia de las listas basadas en arrays, obtener el tamaño de una lista enlazada a menudo requiere recorrerla a menos que se mantenga un contador separado.

**En Resumen:**

Este ejemplo resalta la ventaja de la lista enlazada para inserciones al principio (`prepend`), una operación que es muy eficiente (O(1)). También muestra cómo buscar elementos (`search`) y obtener el tamaño actual (`get_size`) de la colección, que en una lista enlazada simple implica recorridos secuenciales.
