# Explicación del Ejemplo 1: Cola de Procesamiento de Tareas

Este ejemplo simula un sistema simple donde las tareas que llegan deben ser procesadas en el estricto orden de llegada. Esto es un caso de uso clásico para una **cola (Queue)** debido a su naturaleza **FIFO (First-In, First-Out)**.

**Funcionalidades Demostradas:**

1.  **`enqueue` (Agregar):** Representado por la operación `cola_tareas.append()`. Cada vez que una nueva tarea ("Tarea A", "Tarea B", "Tarea C") se agrega, se añade al *final* (la "parte trasera" o `right` en `deque`) de la cola. Esto simula que nuevas tareas llegan al sistema y se ponen en espera.

2.  **`dequeue` (Procesar/Eliminar):** Representado por la operación `cola_tareas.popleft()`. Cuando el sistema está listo para procesar una tarea, toma el elemento del *frente* (la "cabeza" o `left` en `deque`) de la cola. `popleft()` no solo devuelve el elemento, sino que también lo *elimina* de la cola. Esto asegura que la tarea que lleva más tiempo esperando es la siguiente en ser procesada.

3.  **`isEmpty` (Verificar si está vacía):** Representado por la condición del bucle `while cola_tareas:` o por `len(cola_tareas) == 0`. Antes de intentar procesar una tarea, es importante verificar si la cola realmente contiene elementos. El bucle `while cola_tareas:` aprovecha que `deque` (y la mayoría de las colecciones en Python) se evalúan como `False` cuando están vacías y `True` cuando no lo están. Al final, `len(cola_tareas) == 0` confirma explícitamente si la cola ha quedado vacía después de procesar todas las tareas.

**En Resumen:**

El ejemplo muestra cómo una cola mantiene el orden de llegada (`append` al final, `popleft` desde el frente) y cómo se puede iterar sobre ella procesando elementos uno por uno hasta que no queden más (`while cola_tareas:`). Es una demostración fundamental del principio FIFO de las colas.
