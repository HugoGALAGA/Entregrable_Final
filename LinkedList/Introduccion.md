---

## 🔗 Linked Lists (Listas Enlazadas)

Una estructura de datos lineal donde los elementos no están almacenados en posiciones de memoria contiguas, sino que cada elemento apunta al siguiente.

---

### 🤔 ¿Qué son?

Una Lista Enlazada es una colección de elementos llamados **nodos**, donde cada nodo contiene:

1.  El **dato** del elemento.
2.  Un **puntero** (o referencia) al **siguiente nodo** en la secuencia.

A diferencia de los Arrays, los elementos de una Lista Enlazada **no necesitan estar almacenados juntos** en la memoria. La conexión entre los nodos se establece a través de los punteros. La lista en sí misma solo necesita mantener una referencia al **primer nodo**, generalmente llamado **cabeza (`head`)**. El último nodo apunta a `null` (o un valor similar) para indicar el final de la lista.

Piensa en ello como una **cadena**: cada eslabón (nodo) contiene algo (dato) y está conectado al siguiente eslabón (puntero), pero los eslabones individuales podrían estar dispersos en el espacio si no fuera por la cadena que los une. Para ir de un eslabón a otro, sigues la conexión.

### ⚙️ ¿Cómo Funcionan Internamente?

La operación clave en una lista enlazada es **seguir los punteros**. Para acceder a un elemento, debes comenzar desde la `head` y seguir el puntero `next` de nodo en nodo hasta llegar al deseado.

**Tipos Comunes de Listas Enlazadas:**

*   **Lista Simplemente Enlazada (Singly Linked List):** Cada nodo tiene un puntero solo al *siguiente* nodo. La lista tiene un puntero `head`. A veces, se mantiene también un puntero `tail` al último nodo para hacer la inserción al final eficiente.
*   **Lista Doblemente Enlazada (Doubly Linked List):** Cada nodo tiene un puntero al *siguiente* nodo y otro puntero al *nodo anterior* (`prev`). La lista tiene punteros `head` y `tail`. Esto permite recorrer la lista en ambas direcciones.
*   **Lista Enlazada Circular (Circular Linked List):** La lista puede ser simple o doblemente enlazada, pero el último nodo apunta al primer nodo (`head`) en lugar de a `null`.

### ⏰ Operaciones Comunes y su Complejidad

La no contigüidad de la memoria cambia drásticamente la eficiencia de algunas operaciones en comparación con los Arrays.

*   **Acceso a un Elemento por Índice (`list[i]`):**
    *   **¿Cómo?** Debes empezar desde la `head` y **recorrer** la lista (`seguir los punteros next`) hasta alcanzar la posición `i`.
    *   **Complejidad de Tiempo:** `O(n)` (Lineal).
    *   **Explicación:** Para encontrar el elemento en la posición `i`, debes visitar los `i` nodos anteriores. En el peor caso (último elemento), debes recorrer toda la lista (`n` nodos). A diferencia de los arrays, no hay forma de calcular la dirección directamente.

*   **Búsqueda de un Elemento por Valor:**
    *   **¿Cómo?** Debes empezar desde la `head` y **recorrer** la lista (`seguir los punteros next`) nodo por nodo, comparando el dato de cada nodo con el valor buscado.
    *   **Complejidad de Tiempo:** `O(n)` (Lineal) en el peor caso (elemento no encontrado o al final).
    *   **Explicación:** En el peor escenario, debes examinar cada uno de los `n` elementos de la lista.

*   **Inserción de un Elemento:**
    *   **¿Cómo?** Se crea un nuevo nodo. Para insertarlo, solo necesitas modificar los punteros del nodo *anterior* y del *nuevo* nodo para "enlazarlo" en la posición correcta.
    *   **a) Al Principio (Head):**
        *   **¿Cómo?** El nuevo nodo apunta al `head` actual, y el `head` se actualiza al nuevo nodo.
        *   **Complejidad de Tiempo:** `O(1)` (Constante). ¡Muy eficiente!
    *   **b) Al Final (Tail):**
        *   **¿Cómo?**
            *   *Lista Simplemente Enlazada (sin `tail`):* Debes recorrer toda la lista para encontrar el último nodo, luego enlazar el nuevo nodo a él. `O(n)`.
            *   *Lista Simplemente Enlazada (con `tail`):* El `tail` actual apunta al nuevo nodo, y el `tail` se actualiza al nuevo nodo. `O(1)`.
            *   *Lista Doblemente Enlazada (con `tail`):* Similar, O(1).
        *   **Complejidad de Tiempo (con `tail`):** `O(1)` (Constante).
    *   **c) En Medio:**
        *   **¿Cómo?** Si ya tienes una referencia al nodo *anterior* al punto de inserción: el nuevo nodo apunta al nodo que seguía al anterior, y el nodo anterior apunta al nuevo nodo. Si es una doblemente enlazada, actualizas los punteros `prev` también.
        *   **Complejidad de Tiempo (si tienes la referencia del nodo anterior):** `O(1)` (Constante). ¡Muy eficiente!
        *   **Complejidad de Tiempo (si debes encontrar la posición por índice o valor):** `O(n)` debido a que encontrar la posición requiere recorrer la lista.
    *   **Resumen de Inserción:** La inserción es `O(1)` *si tienes la referencia* al nodo anterior (o es el inicio/fin con `tail`). Encontrar el lugar puede ser `O(n)`.

*   **Eliminación de un Elemento:**
    *   **¿Cómo?** Para eliminar un nodo, modificas el puntero `next` del nodo *anterior* para que apunte al nodo *siguiente* del nodo a eliminar. El nodo a eliminar deja de estar enlazado y puede ser recogido por el recolector de basura.
    *   **a) Al Principio (Head):**
        *   **¿Cómo?** El `head` se actualiza al siguiente nodo.
        *   **Complejidad de Tiempo:** `O(1)` (Constante). ¡Muy eficiente!
    *   **b) Al Final (Tail):**
        *   **¿Cómo?**
            *   *Lista Simplemente Enlazada:* Debes recorrer la lista para encontrar el nodo *anterior* al `tail` actual (O(n)).
            *   *Lista Doblemente Enlazada (con `tail`):* Puedes usar el puntero `prev` del `tail` para encontrar el anterior en O(1), actualizar `tail` y el puntero `next` del nuevo `tail`. `O(1)`.
        *   **Complejidad de Tiempo (Simplemente Enlazada):** `O(n)`.
        *   **Complejidad de Tiempo (Doblemente Enlazada con `tail`):** `O(1)` (Constante).
    *   **c) En Medio:**
        *   **¿Cómo?** Si tienes una referencia al nodo *anterior* al nodo a eliminar: actualizas el puntero `next` del nodo anterior para "saltarse" el nodo a eliminar. En doblemente enlazadas, también actualizas el puntero `prev` del nodo *siguiente* al eliminado.
        *   **Complejidad de Tiempo (si tienes la referencia del nodo anterior):** `O(1)` (Constante). ¡Muy eficiente!
        *   **Complejidad de Tiempo (si debes encontrar la posición por índice o valor):** `O(n)` debido a que encontrar la posición requiere recorrer la lista.
    *   **Resumen de Eliminación:** La eliminación es `O(1)` *si tienes la referencia* al nodo a eliminar (en doblemente enlazadas) o al nodo anterior (en simplemente enlazadas). Encontrar el lugar puede ser `O(n)`.

*   **Recorrido (Traversal):**
    *   **¿Cómo?** Empezar en `head` y seguir los punteros `next` hasta llegar a `null`.
    *   **Complejidad de Tiempo:** `O(n)` (Lineal).
    *   **Explicación:** Debes visitar cada uno de los `n` nodos.

### ✅ Ventajas de las Linked Lists

*   **Tamaño Dinámico:** Pueden crecer o encogerse fácilmente en tiempo de ejecución, sin necesidad de pre-asignar un tamaño fijo o realizar redimensionamientos costosos.
*   **Inserciones y Eliminaciones Eficientes:** Las operaciones de inserción y eliminación son `O(1)` *si se tiene una referencia al nodo* en el que se va a operar (o el anterior/siguiente), o si se realizan al principio/final (con `tail` en algunos casos). Esto es mucho mejor que el `O(n)` de los Arrays para operaciones en medio.
*   **No Desperdician Memoria (Potencialmente):** Solo asignan memoria para los nodos que realmente contienen datos. No hay bloques de memoria vacíos pre-asignados esperando ser llenados.
*   **Implementación de Otras Estructuras:** Son ideales para construir Stacks (usando la cabeza como cima) y Queues (usando cabeza como frente y cola como final).

### ❌ Desventajas de las Linked Lists

*   **Acceso Lento (No Aleatorio):** La mayor desventaja es el acceso `O(n)` por índice o la búsqueda `O(n)` por valor. No puedes saltar directamente a un elemento; debes recorrer la lista desde el principio.
*   **Mayor Consumo de Memoria por Elemento:** Cada nodo requiere memoria adicional para almacenar los punteros (`next` y opcionalmente `prev`), además del dato en sí. Para datos muy pequeños, la sobrecarga del puntero puede ser significativa.
*   **No Aprovechan la Caché (Pobre Localidad Espacial):** Como los nodos están dispersos en la memoria, los procesadores no pueden leer bloques contiguos eficientemente en la caché como lo harían con los Arrays. Esto puede hacer que los recorridos sean más lentos en la práctica que los recorridos de arrays, a pesar de que ambos sean `O(n)` en complejidad teórica de tiempo.
*   **Más Complejas de Implementar:** Manejar punteros requiere más cuidado y es propenso a errores (como fugas de memoria, punteros nulos, etc.) en lenguajes sin recolección de basura automática o si no se manejan bien los casos límite (lista vacía, un solo nodo).

### 💡 Utilidad y Casos de Uso Comunes

Las listas enlazadas son útiles en escenarios donde la flexibilidad de tamaño y las inserciones/eliminaciones eficientes son más importantes que el acceso rápido por índice:

*   **Implementación de Stacks y Queues:** Las implementaciones más limpias y eficientes de estas estructuras a menudo usan Linked Lists.
*   **Sistemas de Archivos:** Algunas estructuras internas pueden usar listas enlazadas para rastrear bloques de datos dispersos.
*   **Gestión de Memoria Dinámica:** Los asignadores de memoria pueden usar listas enlazadas para mantener un registro de bloques de memoria libres y asignados.
*   **Implementación de Listas Dinámicas:** En lenguajes donde los arrays son de tamaño fijo, una lista enlazada o una estructura basada en ella (como `std::list` en C++ o la base de `list` en Python, que usa bloques con punteros) proporciona la funcionalidad de tamaño variable.
*   **Listas de Historiales o Recientes:** Donde se añaden elementos al final o al principio y se accede/elimina el más antiguo o el más reciente.
*   **Implementación de otras estructuras complejas:** Utilizadas como base para estructuras como grafos o árboles de búsqueda.

### ⏱️ Complejidad Resumida (Peor Caso)

| Operación                       | Lista Simplemente Enlazada (sin `tail`) | Lista Simplemente Enlazada (con `tail`) | Lista Doblemente Enlazada (con `head`/`tail`) | Arrays (para comparación) |
| :------------------------------ | :-------------------------------------- | :-------------------------------------- | :-------------------------------------------- | :------------------------ |
| **Acceso por Índice**           | `O(n)`                                  | `O(n)`                                  | `O(n)`                                        | `O(1)`                    |
| **Búsqueda por Valor**          | `O(n)`                                  | `O(n)`                                  | `O(n)`                                        | `O(n)` (desordenado), `O(log n)` (ordenado)|
| **Inserción (Inicio)**          | `O(1)`                                  | `O(1)`                                  | `O(1)`                                        | `O(n)`                    |
| **Inserción (Fin)**             | `O(n)`                                  | `O(1)`                                  | `O(1)`                                        | `O(1)` (con espacio), `O(n)` (redimensionar)|
| **Inserción (Medio - si tienes nodo anterior)** | `O(1)`                                  | `O(1)`                                  | `O(1)`                                        | `O(n)`                    |
| **Eliminación (Inicio)**        | `O(1)`                                  | `O(1)`                                  | `O(1)`                                        | `O(n)`                    |
| **Eliminación (Fin)**           | `O(n)`                                  | `O(n)` (aún necesitas anterior)         | `O(1)`                                        | `O(1)`                    |
| **Eliminación (Medio - si tienes nodo anterior)** | `O(1)`                                  | `O(1)`                                  | `O(1)`                                        | `O(n)`                    |
| **Recorrido**                   | `O(n)`                                  | `O(n)`                                  | `O(n)`                                        | `O(n)`                    |

---

**Conclusión:**

Las Linked Lists son una alternativa flexible a los Arrays cuando las inserciones y eliminaciones frecuentes, especialmente al principio o en medio (si tienes una referencia), son operaciones críticas. Sacrifican la velocidad de acceso aleatorio (`O(n)` vs `O(1)` de los arrays) y pueden usar más memoria total (debido a los punteros), pero ofrecen una gran eficiencia para modificar la estructura sin costosos movimientos de datos como los arrays. La elección entre una Lista Enlazada y un Array depende completamente de qué operaciones serán más comunes y críticas para el problema que intentas resolver.
