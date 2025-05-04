---

## 🌳 Binary Search Trees (Árboles Binarios de Búsqueda - BST)

Un tipo especial de Árbol Binario que mantiene una propiedad de orden específica para permitir la búsqueda, inserción y eliminación eficientes.

---

### 🤔 ¿Qué son?

Un Árbol Binario de Búsqueda (BST) es un **Árbol Binario** donde los nodos se organizan siguiendo una regla de **ordenamiento**:

*   Para **cualquier nodo `N`** en el árbol:
    *   Todos los valores en el **subárbol izquierdo** de `N` son **menores** que el valor de `N`.
    *   Todos los valores en el **subárbol derecho** de `N` son **mayores** que el valor de `N`.
*   Esta propiedad se aplica de forma **recursiva** a todos los subárboles.

Piensa en un BST como una forma dinámica de **organizar números o palabras** (u otros datos comparables) para poder encontrarlos rápidamente. En lugar de una simple estructura jerárquica, aquí la posición de cada elemento está dictada por su valor en relación con su padre.

### ⚙️ ¿Cómo Funcionan Internamente?

Un BST se construye a partir de **nodos**, similar a un árbol binario general. Cada nodo contiene:

1.  El **dato** o valor del nodo.
2.  Un puntero al **hijo izquierdo**.
3.  Un puntero al **hijo derecho**.

La clave de su funcionamiento es la **propiedad de orden**: al insertar, buscar o eliminar un valor, siempre sabes si debes ir hacia la izquierda (si el valor es menor que el nodo actual) o hacia la derecha (si es mayor). Nunca necesitas explorar ambos subárboles, lo que reduce drásticamente el espacio de búsqueda. El árbol se referencia por su **raíz**.

### ⚖️ Propiedades Clave y Balance

La eficiencia de un BST depende fundamentalmente de su **altura (h)**.

*   En un BST **perfectamente balanceado**, la altura es `O(log n)`, donde `n` es el número de nodos. La búsqueda y otras operaciones se completan muy rápidamente (logarítmicamente).
*   Sin embargo, si los nodos se insertan en un orden particular (ej: ya ordenados), el BST puede degenerar en una estructura parecida a una **Lista Enlazada** (un árbol degenerado o puntiagudo). En este caso, la altura es `O(n)`, y la eficiencia de las operaciones se degrada a `O(n)`.

**Tipos de BSTs (por Balance):**

*   **BST No Balanceado:** Un BST básico sin mecanismos para mantener la altura mínima. Su rendimiento puede variar drásticamente entre `O(log n)` (mejor/promedio caso con inserciones aleatorias) y `O(n)` (peor caso con inserciones ordenadas).
*   **BST Auto-Balanceado:** Tipos avanzados de BSTs que realizan rotaciones u otras operaciones internas automáticamente durante la inserción o eliminación para garantizar que la altura se mantenga `O(log n)`, incluso en el peor caso. Ejemplos importantes incluyen **Árboles AVL** y **Árboles Rojo-Negro (Red-Black Trees)**. Estos garantizan un rendimiento logarítmico constante, a cambio de una implementación más compleja.

### ⏰ Operaciones Comunes y su Complejidad

Las operaciones en un BST aprovechan la propiedad de orden. La complejidad está ligada a la altura (`h`).

*   **Búsqueda (Search):**
    *   **¿Cómo?** Comienza en la raíz. Compara el valor buscado con el nodo actual: si es igual, encontrado; si es menor, ve al subárbol izquierdo; si es mayor, ve al subárbol derecho. Repite hasta encontrar el valor o llegar a un puntero `null`.
    *   **Complejidad de Tiempo:** `O(h)`.
    *   **Explicación:** En un **BST balanceado**, `h = O(log n)`, por lo que la búsqueda es `O(log n)`. En un **BST degenerado**, `h = O(n)`, y la búsqueda es `O(n)`. Esta es la **principal fortaleza** de los BSTs balanceados.

*   **Inserción (Insertion):**
    *   **¿Cómo?** Busca la posición correcta para el nuevo valor (como en la búsqueda). Una vez que llegas a un puntero `null` donde debería estar el valor (según la propiedad de orden), creas un nuevo nodo y lo enlazas allí.
    *   **Complejidad de Tiempo:** `O(h)`.
    *   **Explicación:** Similar a la búsqueda. `O(log n)` en balanceados (incluyendo el costo de re-balanceo para mantener la propiedad `O(log n)`), `O(n)` en degenerados.

*   **Eliminación (Deletion):**
    *   **¿Cómo?** Es la operación más compleja. Primero, buscas el nodo a eliminar (`O(h)`). Una vez encontrado, hay tres casos:
        1.  **Nodo Hoja:** Simplemente elimínalo.
        2.  **Nodo con un Hijo:** Reemplázalo por su único hijo.
        3.  **Nodo con Dos Hijos:** Encuentra su **sucesor in-order** (el nodo más pequeño en su subárbol derecho, que está en el camino más a la izquierda desde el hijo derecho). Copia el valor del sucesor al nodo que quieres eliminar, y luego elimina recursivamente el sucesor (el sucesor siempre tendrá 0 o 1 hijo, simplificando su eliminación).
    *   **Complejidad de Tiempo:** `O(h)`.
    *   **Explicación:** La búsqueda del nodo y el sucesor (en el peor caso) recorren una rama hasta una hoja. `O(log n)` en balanceados (incluyendo re-balanceo), `O(n)` en degenerados.

*   **Encontrar Mínimo/Máximo:**
    *   **¿Cómo?** El valor mínimo está siempre en el nodo más a la izquierda desde la raíz (siguiendo solo los punteros izquierdos). El valor máximo está en el nodo más a la derecha (siguiendo solo los punteros derechos).
    *   **Complejidad de Tiempo:** `O(h)`.
    *   **Explicación:** Recorres una rama hasta una hoja. `O(log n)` en balanceados, `O(n)` en degenerados.

*   **Recorrido In-order (Inorden):**
    *   **¿Cómo?** Recorrer subárbol izquierdo -> visitar nodo actual -> recorrer subárbol derecho.
    *   **Resultado:** ¡Produce una lista de los nodos en **orden ascendente**!
    *   **Complejidad de Tiempo:** `O(n)`.
    *   **Complejidad de Espacio:** `O(h)` (recursivo) o `O(n)` (iterativo con pila/level-order).

### ✅ Ventajas de los BSTs

*   **Búsqueda, Inserción y Eliminación Eficientes (Promedio/Balanceado):** El principal beneficio es el rendimiento `O(log n)` para estas operaciones clave, que es mucho mejor que `O(n)` para estructuras lineales grandes y mejor que `O(n)` para la búsqueda en arrays desordenados.
*   **Mantiene los Datos Ordenados:** A diferencia de las Tablas Hash, el recorrido in-order produce los elementos en orden clasificado, lo cual es muy útil.
*   **Flexible en Tamaño:** Como estructura basada en punteros, puede crecer y encogerse dinámicamente.
*   **Encontrar Mínimo/Máximo y Rangos:** Eficiente para encontrar los valores extremos o todos los valores dentro de un rango específico (`O(log n + k)`, donde `k` es el número de elementos en el rango, en balanceados).

### ❌ Desventajas de los BSTs

*   **Rendimiento Degenerado (sin Balanceo):** Si el árbol no está balanceado, el peor caso para búsqueda, inserción y eliminación es `O(n)`, perdiendo toda su ventaja sobre las estructuras lineales.
*   **Complejidad de Implementación (Especialmente Eliminación y Balanceo):** La eliminación es más complicada que en otras estructuras, y la implementación de BSTs auto-balanceados es significativamente más compleja.
*   **Consumo de Memoria por Punteros:** Cada nodo requiere memoria para dos punteros.
*   **Acceso Lento por Índice:** No es eficiente para acceder al k-ésimo elemento (`O(n)` en el peor caso).

### 💡 Utilidad y Casos de Uso Comunes

Los BSTs, particularmente sus variantes auto-balanceadas, son muy utilizadas:

*   **Implementación de Conjuntos (`Set`) y Mapas/Diccionarios (`Map`/`Dictionary`):** Donde necesitas almacenar pares clave-valor o colecciones de elementos únicos que puedan ser eficientemente buscados, insertados, eliminados *y* recuperados en orden ordenado (a diferencia de Tablas Hash).
*   **Bases de Datos:** Aunque las bases de datos suelen usar B-Trees (optimizados para disco), los BSTs (o sus conceptos) son fundamentales para entender cómo funcionan los índices que aceleran las consultas.
*   **Algoritmos de Búsqueda y Clasificación:** Son la base de la búsqueda logarítmica en colecciones dinámicas y pueden usarse para ordenar datos (In-order traversal).
*   **Sistemas que Requieren Datos Ordenados Dinámicos:** Donde los datos cambian frecuentemente y necesitas consultarlos o iterarlos en orden.

### ⏱️ Complejidad Resumida

| Operación         | BST (Promedio / Balanceado) | BST (Peor Caso / Degenerado) | Notas                                 |
| :---------------- | :-------------------------- | :--------------------------- | :------------------------------------ |
| **Búsqueda**      | `O(log n)`                  | `O(n)`                       | Depende de la altura `h`.             |
| **Inserción**     | `O(log n)`                  | `O(n)`                       | Depende de la altura `h`.             |
| **Eliminación**   | `O(log n)`                  | `O(n)`                       | Depende de la altura `h`.             |
| **Encontrar Mín/Máx**| `O(log n)`                  | `O(n)`                       | Depende de la altura `h`.             |
| **Recorrido (cualquiera)** | `O(n)`                      | `O(n)`                       | Se visitan todos los `n` nodos.       |
| **Recorrido In-order**| `O(n)`                      | `O(n)`                       | Visita nodos en orden ascendente.     |
| **Acceso por Índice**| `O(n)`                      | `O(n)`                       | Requiere recorrido.                   |

*(Nota: En BSTs auto-balanceados, las complejidades `O(log n)` se garantizan incluso en el peor caso de inserción/eliminación).*

### 🧩 Relación con Otras Estructuras

*   **vs. Binary Trees:** Un BST es un Árbol Binario *con una propiedad de orden*. Esta propiedad es la que habilita la búsqueda eficiente.
*   **vs. Arrays:** Los Arrays tienen `O(1)` acceso por índice y `O(log n)` búsqueda si están ordenados, pero `O(n)` para inserciones/eliminaciones en medio. Los BSTs balanceados ofrecen `O(log n)` para búsqueda, inserción y eliminación, lo que los hace mejores que los arrays para colecciones dinámicas con muchas modificaciones.
*   **vs. Linked Lists:** Las Listas Enlazadas tienen `O(1)` inserción/eliminación (si tienes la referencia) pero `O(n)` búsqueda y acceso. Los BSTs balanceados son mucho mejores para la búsqueda (`O(log n)` vs `O(n)`).
*   **vs. Hash Tables:** Las Tablas Hash ofrecen `O(1)` promedio para búsqueda, inserción y eliminación (más rápido que `O(log n)`). Sin embargo, no mantienen los datos ordenados y no son eficientes para encontrar mínimos/máximos o rangos. Los BSTs (balanceados) son la mejor opción cuando necesitas tanto operaciones rápidas *como* la capacidad de procesar los datos en orden ordenado o encontrar rangos/extremos eficientemente.

---

**Conclusión:**

Los Árboles Binarios de Búsqueda (BSTs) son una extensión crucial de los Árboles Binarios que, al imponer una propiedad de orden, logran un rendimiento de búsqueda, inserción y eliminación mucho más eficiente (`O(log n)` en el promedio y, crucialmente, en el peor caso para variantes auto-balanceadas) en comparación con estructuras lineales. Son la elección ideal cuando necesitas una estructura de datos dinámica que permita encontrar, añadir y eliminar elementos rápidamente, *y* donde la capacidad de iterar sobre los elementos en orden clasificado o encontrar rangos es importante. Sin embargo, es vital utilizar BSTs auto-balanceados en la práctica para evitar la degradación del rendimiento a `O(n)` en el peor caso.
