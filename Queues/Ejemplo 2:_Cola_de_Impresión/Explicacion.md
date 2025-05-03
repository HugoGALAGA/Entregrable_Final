# Explicación del Ejemplo 2: Cola de Impresión

Este ejemplo modela la cola de documentos que se envían a una impresora. La impresora procesa los trabajos en el orden en que fueron enviados, lo cual es otro escenario perfecto para una estructura de datos de tipo **cola (Queue)**.

**Funcionalidades Demostradas:**

1.  **`enqueue` (Agregar):** Realizado con `cola_impresion.append()`. Cada documento enviado (`"Reporte.docx"`, `"Imagen.png"`, etc.) se añade al *final* de la cola de impresión. Esto representa los trabajos que se ponen en espera para ser impresos.

2.  **`dequeue` (Imprimir/Eliminar):** Implementado con `cola_impresion.popleft()`. Cuando la impresora está libre, toma el documento que ha estado esperando más tiempo (el del *frente* de la cola), lo "imprime" (simulado por el `print()`) y lo elimina de la cola. Esto garantiza que los documentos se imprimen en el orden correcto (FIFO).

3.  **`peek` (Ver el primero sin remover):** Mostrado por `cola_impresion[0]`. Antes de imprimir, a menudo es útil ver cuál es el próximo elemento en la cola sin sacarlo. Acceder al índice `[0]` en `deque` permite hacer esto: obtener una referencia al elemento en el frente *sin eliminarlo* de la cola.

4.  **`size` (Cantidad de elementos):** Obtenido usando `len(cola_impresion)`. Esta funcionalidad permite saber cuántos documentos hay actualmente en la cola esperando a ser impresos. Es útil para monitorear la carga de trabajo o el tiempo de espera estimado.

**En Resumen:**

Este ejemplo utiliza la cola para gestionar el orden de los trabajos de impresión, demostrando no solo las operaciones básicas de agregar y eliminar (manteniendo el orden FIFO), sino también cómo inspeccionar el próximo elemento (`peek`) y verificar cuántos elementos hay esperando (`size`), que son operaciones comunes en sistemas de gestión de recursos.
