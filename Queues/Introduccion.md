---

## 🚶‍♀️ Queues (Colas)

Una estructura de datos lineal que sigue el principio **FIFO** (First-In, First-Out - Primero en Entrar, Primero en Salir).

---

### 🤔 ¿Qué son?

Una Cola es una colección de elementos diseñada para que el primer elemento que se añade sea también el primero en ser eliminado. Tiene dos extremos principales de operación:

*   Se agregan elementos por el **final** (o "parte trasera"). La operación se llama comúnmente `enqueue()`.
*   Se eliminan elementos por el **frente** (o "parte delantera"). La operación se llama comúnmente `dequeue()`.

Piensa en una cola como la **fila en un supermercado**: la primera persona que llega a la fila es la primera persona que pasa por la caja. Las nuevas personas se unen al final de la fila.

### ⚙️ ¿Cómo Funcionan Internamente?

Al igual que las pilas, las colas se implementan utilizando otras estructuras de datos subyacentes. Las dos implementaciones más comunes son con Arrays o Listas Enlazadas.

*   **Usando Arrays (Arreglos):**
    *   Se usa un array para almacenar los elementos. Se necesitan **dos punteros o índices**: uno para el **frente** (`front`) y otro para el **final** (`rear`).
    *   `enqueue`: Se añade el elemento en la posición del `rear` y se incrementa el `rear`.
    *   `dequeue`: Se elimina el elemento en la posición del `front` y se incrementa el `front`.
    *   **Problema con Arrays Lineales:** Si simplemente incrementas `front` y `rear`, eventualmente el array se "llenará" aunque haya espacio libre al principio. Para hacer espacio al principio, tendrías que mover todos los elementos hacia adelante después de cada `dequeue`, lo cual es `O(n)` y muy ineficiente.
    *   **Solución: Arrays Circulares:** Una implementación más eficiente usa un array circular (o "buffer anular"). Los índices `front` y `rear` avanzan y "envuelven" (usan el operador módulo `%`) al final del array, reutilizando el espacio liberado al principio.
    *   *Consideraciones:* Implementar colas eficientes con arrays requiere manejar el "envolvimiento" de índices y distinguir entre una cola llena y una cola vacía usando los mismos índices (a menudo requiere un contador de tamaño o dejar un espacio vacío).

*   **Usando Listas Enlazadas:**
    *   Esta es generalmente la implementación **más sencilla y común** para colas eficientes. Se usa una lista enlazada simple con punteros al **primer nodo** (`head`, que representa el `front`) y al **último nodo** (`tail`, que representa el `rear`).
    *   `enqueue`: Se crea un nuevo nodo, se enlaza *después* del nodo `tail` actual, y luego el puntero `tail` se actualiza al nuevo nodo. Si la cola estaba vacía, el `head` también apunta al nuevo nodo. Esta operación es `O(1)`.
    *   `dequeue`: Se devuelve el valor del nodo `head` actual, y luego el puntero `head` se actualiza al siguiente nodo. Si la cola se vacía, `tail` también debe ser nulo. Esta operación es `O(1)`.
    *   *Consideraciones:* No hay problema de tamaño fijo ni de manejo complejo de índices como en arrays lineales/circulares. Cada nodo tiene el overhead de un puntero.

Independientemente de la implementación (circular array o linked list), las operaciones clave `enqueue` y `dequeue` se diseñan para ser `O(1)`.

### ⏰ Operaciones Comunes y su Complejidad

Las operaciones de una Cola se centran en los extremos (`front` y `rear`).

*   **`enqueue(elemento)`:**
    *   **¿Cómo?** Agrega un `elemento` al **final** (`rear`) de la cola.
    *   **Complejidad de Tiempo:** `O(1)` (Constante) con implementaciones eficientes (array circular o lista enlazada).
    *   **Explicación:** La operación solo implica añadir un elemento en una posición conocida (el final), sin importar cuántos elementos ya haya en la cola.

*   **`dequeue()`:**
    *   **¿Cómo?** Elimina y devuelve el elemento del **frente** (`front`) de la cola.
    *   **Complejidad de Tiempo:** `O(1)` (Constante) con implementaciones eficientes.
    *   **Explicación:** La operación solo implica remover un elemento de una posición conocida (el frente). Se debe verificar si la cola está vacía antes de intentar `dequeue`.

*   **`peek()` / `front()`:**
    *   **¿Cómo?** Devuelve el elemento del **frente** (`front`) de la cola *sin eliminarlo*.
    *   **Complejidad de Tiempo:** `O(1)` (Constante).
    *   **Explicación:** Solo requiere acceder al elemento referenciado por el puntero/índice del `front`. Se debe manejar el caso de cola vacía.

*   **`isEmpty()`:**
    *   **¿Cómo?** Verifica si la cola no contiene elementos.
    *   **Complejidad de Tiempo:** `O(1)` (Constante).
    *   **Explicación:** Generalmente se basa en verificar si el puntero `front` o `head` es nulo, o si un contador de tamaño es cero.

*   **`size()`:**
    *   **¿Cómo?** Devuelve el número de elementos en la cola.
    *   **Complejidad de Tiempo:** `O(1)` (Constante) si se mantiene un contador de elementos que se actualiza en `enqueue` y `dequeue`. `O(n)` si requiere recorrer todos los elementos (implementación ineficiente, no estándar para ADT Queue).
    *   **Explicación:** Es común que las implementaciones de cola eficientes mantengan un contador para que esta operación sea también `O(1)`.

### ✅ Ventajas de las Colas

*   **Simplicidad Conceptual:** Reflejan procesos del mundo real (filas, espera).
*   **Eficiencia Extrema para Operaciones Principales:** `enqueue`, `dequeue`, `peek`, `isEmpty` son todas `O(1)` con implementaciones adecuadas.
*   **Imponen Orden FIFO:** Ideal para problemas donde el orden de procesamiento es "primero en llegar, primero en ser atendido".
*   **Desacoplamiento:** Permiten separar la parte del sistema que produce tareas de la parte que las consume (buffers, sistemas de mensajes).

### ❌ Desventajas de las Colas

*   **Acceso Limitado:** Solo puedes acceder al elemento del frente. Acceder a elementos en medio o al final es difícil o imposible sin modificar la cola (`dequeue`ando elementos).
*   **Búsqueda Ineficiente:** Encontrar un elemento específico (que no sea el del `front`) es `O(n)` en el peor caso, ya que requeriría `dequeue`ar elementos hasta encontrarlo o vaciar la cola.

### 💡 Utilidad y Casos de Uso Comunes

Las colas son esenciales en muchos sistemas informáticos para gestionar tareas o datos en un orden específico:

*   **Sistemas Operativos:**
    *   **Planificación de Procesos (CPU Scheduling):** Procesos esperando para usar la CPU.
    *   **Colas de Impresión:** Documentos esperando para ser impresos.
    *   **Gestión de I/O (Entrada/Salida):** Solicitudes pendientes a discos, redes, etc.
*   **Redes:**
    *   **Buffers de Paquetes:** Paquetes de datos esperando para ser procesados o transmitidos.
    *   **Colas de Mensajes:** Usadas en arquitecturas distribuidas para comunicación asíncrona.
*   **Algoritmos:**
    *   **Búsqueda en Amplitud (Breadth-First Search - BFS):** En grafos y árboles, se usa una cola para explorar nodos nivel por nivel.
*   **Simulaciones:** Modelar sistemas donde entidades esperan en línea (clientes en una tienda, autos en una cola).
*   **Manejo de Eventos:** Eventos en un sistema esperando ser procesados en el orden en que ocurrieron.

### ⏱️ Complejidad Resumida (Peor Caso con Implementación Eficiente)

| Operación           | Complejidad de Tiempo |
| :------------------ | :-------------------- |
| **`enqueue(elemento)`**| `O(1)`                |
| **`dequeue()`**     | `O(1)`                |
| **`peek()` / `front()`**| `O(1)`                |
| **`isEmpty()`**     | `O(1)`                |
| **`size()`**        | `O(1)` (si se usa contador) |
| **Búsqueda por Valor**| `O(n)`                |
| **Acceso por Índice**| No es una operación estándar |

---

En conclusión, las Queues son estructuras de datos optimizadas para el orden FIFO. Su principal fortaleza reside en la eficiencia `O(1)` de sus operaciones de adición (`enqueue`) y eliminación (`dequeue`) en los extremos definidos. Son la herramienta perfecta cuando la secuencia de procesamiento de elementos es crucial y sigue un modelo de "primero en llegar, primero en ser servido".
