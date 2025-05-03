# Explicación del Ejemplo 3: Cola de Llamadas en un Call Center

Este ejemplo simula cómo un centro de llamadas gestiona las llamadas entrantes. Cuando todas las líneas de los agentes están ocupadas, las llamadas adicionales se colocan en una cola de espera y se atienden en el orden en que llegaron.

**Funcionalidades Demostradas:**

1.  **`enqueue` (Llamada entrante):** Implementado con `cola_llamadas.append()`. Cada vez que una nueva llamada entra y no hay un agente disponible inmediatamente, se añade al *final* de la cola de espera.

2.  **`dequeue` (Agente toma llamada/Eliminar):** Realizado con `cola_llamadas.popleft()`. Cuando un agente termina una llamada y está libre, toma la llamada que ha estado esperando más tiempo, la cual está en el *frente* de la cola. `popleft()` elimina esa llamada de la cola y la "pasa" al agente.

3.  **`size` (Cantidad de llamadas esperando):** Obtenido mediante `len(cola_llamadas)`. Permite saber cuántas llamadas hay en la cola en un momento dado, lo cual es una métrica importante para un call center (indica la carga de trabajo y el posible tiempo de espera).

4.  **`isEmpty` (Verificar si hay llamadas):** Representado por la condición `if cola_llamadas:` o `if not cola_llamadas:`. Antes de que un agente intente tomar una llamada, el sistema verifica si hay llamadas *pendientes* en la cola. Si la cola está vacía (`isEmpty` es `True`), el agente no tiene llamadas que atender de la cola de espera.

**En Resumen:**

Este ejemplo ilustra un uso muy práctico de una cola para gestionar el flujo de solicitudes (llamadas) que llegan a un recurso limitado (agentes). Demuestra cómo las operaciones `enqueue` y `dequeue` mantienen el orden de atención (FIFO), y cómo `size` e `isEmpty` son cruciales para monitorear y gestionar eficientemente la carga del sistema y la disponibilidad de recursos.
