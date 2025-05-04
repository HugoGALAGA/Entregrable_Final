---

## 🌳 Trees (Árboles)

Una estructura de datos **no lineal** que representa relaciones jerárquicas entre elementos.

---

### 🤔 ¿Qué son?

Un Árbol es una colección de elementos llamados **nodos**, conectados por **aristas** (o enlaces). Se caracterizan por tener una estructura **jerárquica**:

*   Hay un nodo especial llamado **raíz (`root`)** en la parte superior.
*   Cada nodo (excepto la raíz) tiene exactamente un nodo **padre**.
*   Cada nodo puede tener cero o más nodos **hijos**.
*   No hay **ciclos**; es decir, no puedes seguir las aristas y volver al mismo nodo.

Piensa en un Árbol como la **estructura de carpetas en tu computadora** o un **árbol genealógico**: hay una carpeta principal (raíz), dentro hay subcarpetas (hijos), y cada subcarpeta está contenida en solo una carpeta padre. Los archivos dentro de la carpeta más interna serían las hojas.

### ⚙️ ¿Cómo Funcionan Internamente?

Los árboles generalmente se implementan utilizando **punteros** o referencias entre nodos. Cada nodo típicamente almacena su dato y punteros a sus hijos.

**Terminología Clave:**

*   **Raíz (Root):** El nodo superior del árbol. No tiene padre.
*   **Nodo (Node):** Un elemento individual en el árbol que contiene un dato y enlaces a otros nodos.
*   **Padre (Parent):** Un nodo que tiene uno o más hijos.
*   **Hijo (Child):** Un nodo conectado directamente debajo de otro nodo (su padre).
*   **Hermanos (Siblings):** Nodos que comparten el mismo padre.
*   **Hoja (Leaf):** Un nodo que no tiene hijos.
*   **Arista (Edge):** El enlace o conexión entre un padre y un hijo.
*   **Ruta (Path):** Una secuencia de nodos conectados por aristas desde un nodo a otro.
*   **Profundidad (Depth):** La longitud de la ruta desde la raíz hasta un nodo específico. La raíz tiene profundidad 0.
*   **Altura (Height):** La longitud de la ruta más larga desde un nodo específico hasta una hoja descendiente. La altura de un árbol es la altura de su raíz.
*   **Subárbol (Subtree):** Un nodo y todos sus descendientes.

A diferencia de las listas enlazadas lineales (que tienen un solo puntero `next`), los nodos en un árbol pueden tener múltiples punteros a hijos (dependiendo del tipo de árbol).

### 🌲 Tipos Comunes de Árboles

Existen muchos tipos especializados de árboles, optimizados para diferentes propósitos:

*   **Árbol General (General Tree):** Cada nodo puede tener cualquier número de hijos.
*   **Árbol Binario (Binary Tree):** Cada nodo tiene como máximo **dos** hijos (generalmente llamados hijo izquierdo y hijo derecho). Es un tipo muy común y la base de muchos otros árboles.
*   **Árbol Binario de Búsqueda (Binary Search Tree - BST):** Un Árbol Binario con una propiedad de orden:
    *   Todos los nodos en el **subárbol izquierdo** de un nodo `N` tienen valores **menores** que el valor de `N`.
    *   Todos los nodos en el **subárbol derecho** de un nodo `N` tienen valores **mayores** que el valor de `N`.
    *   Esta propiedad es recursiva para todos los nodos. Es crucial para la búsqueda eficiente.
*   **Árboles Balanceados:** Tipos de BSTs que implementan reglas adicionales para mantener la altura del árbol lo más pequeña posible (cercana a `log n`), evitando que se degeneren en estructuras parecidas a listas enlazadas. Ejemplos: **Árboles AVL**, Árboles Rojo-Negro (Red-Black Trees). Esto garantiza que las operaciones como búsqueda, inserción y eliminación mantengan su eficiencia logarítmica incluso en el peor caso.
*   **Heaps (Montículos):** A menudo representados como árboles binarios (aunque se suelen implementar en arrays por eficiencia de espacio), pero con una propiedad de orden diferente (propiedad del montículo): el valor de cada nodo padre es mayor o igual (Heap Máximo) o menor o igual (Heap Mínimo) que los valores de sus hijos. Se usan para implementar Colas de Prioridad.
*   **B-Trees:** Árboles de múltiples vías (cada nodo puede tener más de dos hijos, en un rango definido). Diseñados para sistemas de almacenamiento secundario (discos duros), optimizando el acceso a datos en bloques. Utilizados comúnmente en índices de bases de datos y sistemas de archivos.

### ⏰ Operaciones Comunes y su Complejidad

Las operaciones sobre árboles a menudo implican recorrer o buscar caminos. La complejidad depende críticamente de la **altura (h)** del árbol, que a su vez depende de si el árbol está balanceado.

*   **Recorrido (Traversal):**
    *   **¿Cómo?** Visitar cada nodo en el árbol exactamente una vez. Existen diferentes órdenes:
        *   **In-order (Inorden):** Visita el subárbol izquierdo, luego el nodo actual, luego el subárbol derecho. En un **BST**, esto visita los nodos en orden **ascendente** de valor. (Izquierda -> Nodo -> Derecha)
        *   **Pre-order (Preorden):** Visita el nodo actual, luego el subárbol izquierdo, luego el subárbol derecho. Útil para copiar árboles o representar la estructura. (Nodo -> Izquierda -> Derecha)
        *   **Post-order (Postorden):** Visita el subárbol izquierdo, luego el subárbol derecho, luego el nodo actual. Útil para eliminar árboles o evaluar expresiones. (Izquierda -> Derecha -> Nodo)
        *   **Level-order (Por Niveles):** Visita los nodos nivel por nivel, de izquierda a derecha. Requiere usar una **Queue**.
    *   **Complejidad de Tiempo:** `O(n)` para visitar cada uno de los `n` nodos.
    *   **Complejidad de Espacio:** `O(h)` para recorridos recursivos (debido a la pila de llamadas). `O(ancho máximo)` del árbol, que en el peor caso es `O(n)`, para el recorrido por niveles (debido al espacio necesario para la Queue).

*   **Búsqueda (Search / Lookup):**
    *   **¿Cómo?** Para un **BST**, comienzas en la raíz. Si el valor buscado es igual al nodo actual, lo encontraste. Si es menor, vas al hijo izquierdo. Si es mayor, vas al hijo derecho. Repites hasta encontrarlo o llegar a una hoja nula. Para un árbol general (no BST), la búsqueda es típicamente un recorrido (ej: Pre-order o Level-order) hasta encontrar el nodo.
    *   **Complejidad de Tiempo:** `O(h)`, donde `h` es la altura del árbol.
    *   **Explicación:** En un **BST balanceado**, `h` es `O(log n)`. En un **BST degenerado** (parece una lista enlazada, altura `n`), `h` es `O(n)`, degradándose a búsqueda lineal.

*   **Inserción (Insertion):**
    *   **¿Cómo?** Para un **BST**, buscas la posición correcta para el nuevo nodo (similar a la búsqueda) y lo añades como una nueva hoja.
    *   **Complejidad de Tiempo:** `O(h)`, donde `h` es la altura del árbol.
    *   **Explicación:** Similar a la búsqueda, la complejidad depende del balanceo del árbol. `O(log n)` en balanceados, `O(n)` en degenerados. *Nota:* En árboles balanceados (AVL, Rojo-Negro), la inserción también incluye el costo adicional de re-balancear, pero la operación total se mantiene en `O(log n)`.

*   **Eliminación (Deletion):**
    *   **¿Cómo?** Para un **BST**, es la operación más compleja. Involucra encontrar el nodo a eliminar y manejar varios casos: eliminar una hoja, eliminar un nodo con un hijo, eliminar un nodo con dos hijos (este último requiere encontrar su sucesor o predecesor in-order para reemplazarlo y luego eliminar el sucesor/predecesor).
    *   **Complejidad de Tiempo:** `O(h)`, donde `h` es la altura del árbol.
    *   **Explicación:** Similar a la búsqueda e inserción, depende del balanceo. `O(log n)` en balanceados (incluyendo re-balanceo), `O(n)` en degenerados.

*   **Encontrar Mínimo/Máximo:**
    *   **¿Cómo?** En un **BST**, el mínimo está siempre en el nodo más a la izquierda desde la raíz. El máximo está en el nodo más a la derecha. Simplemente sigues los punteros izquierdo (para mínimo) o derecho (para máximo) hasta llegar a un nodo sin hijo en esa dirección.
    *   **Complejidad de Tiempo:** `O(h)`, donde `h` es la altura del árbol.
    *   **Explicación:** En un BST balanceado, es `O(log n)`. En un BST degenerado, es `O(n)`.

### ✅ Ventajas de los Árboles

*   **Representación Jerárquica:** Ideal para modelar datos con relaciones padre-hijo.
*   **Búsqueda, Inserción y Eliminación Eficientes (en BSTs Balanceados):** Las operaciones clave son `O(log n)`, lo cual es mucho más rápido que `O(n)` para grandes conjuntos de datos, superando a arrays (para inserción/eliminación en medio y búsqueda en desordenados) y listas enlazadas (para búsqueda y acceso).
*   **Flexibilidad Dinámica:** Al igual que las listas enlazadas, pueden crecer o encogerse según sea necesario, sin los problemas de redimensionamiento de los arrays.
*   **Base para Estructuras Más Avanzadas:** Son el fundamento de BSTs, Heaps, B-Trees, etc.

### ❌ Desventajas de los Árboles

*   **Acceso por Índice Lento:** No puedes acceder directamente al k-ésimo elemento sin recorrer parte del árbol (`O(n)` en el peor caso para un BST).
*   **Complejidad de Implementación:** Más complejos de implementar que estructuras lineales como arrays o listas enlazadas. Manejar punteros, casos de eliminación y el balanceo requiere cuidado.
*   **Pueden Degenerar (BSTs no balanceados):** Si los datos se insertan en un orden particular (ej: ya ordenados), un BST puede convertirse en una estructura similar a una lista enlazada, perdiendo su eficiencia logarítmica y degradando las operaciones a `O(n)`. Los árboles balanceados resuelven esto a costa de mayor complejidad de implementación.
*   **Mayor Consumo de Memoria por Nodo:** Cada nodo necesita espacio para sus punteros a hijos (uno o dos, o más), además del dato.

### 💡 Utilidad y Casos de Uso Comunes

Los árboles se utilizan en una amplia gama de aplicaciones:

*   **Sistemas de Archivos:** La estructura de directorios es un árbol general.
*   **Bases de Datos:** Se utilizan para índices (B-Trees, B+ Trees) para acelerar la búsqueda de registros.
*   **Compiladores:** Generan Árboles de Sintaxis Abstracta (ASTs) para representar la estructura del código fuente.
*   **Inteligencia Artificial / Algoritmos:** Árboles de decisión, árboles de juego (para estrategias en juegos como ajedrez).
*   **Routing en Redes:** Algunos algoritmos usan estructuras de árbol.
*   **Algoritmos de Búsqueda y Ordenamiento:** BSTs para búsqueda eficiente; Heap Sort usa un Heap.
*   **Representación de Jerarquías:** Organigramas, estructuras XML/JSON (a menudo se parsean a árboles internos).

### ⏱️ Complejidad Resumida (Depende del Tipo y Balanceo)

| Operación         | Árbol General (Recorrido) | BST (Promedio / Balanceado) | BST (Peor Caso / Degenerado) |
| :---------------- | :------------------------ | :-------------------------- | :--------------------------- |
| **Acceso por Índice**| `O(n)` (implícito, por recorrido) | `O(n)` (por recorrido)      | `O(n)`                       |
| **Búsqueda**      | `O(n)`                    | `O(log n)`                  | `O(n)`                       |
| **Inserción**     | `O(h)` (depende cómo encuentras lugar) | `O(log n)`                  | `O(n)`                       |
| **Eliminación**   | `O(h)` (depende cómo encuentras lugar) | `O(log n)`                  | `O(n)`                       |
| **Recorrido (cualquiera)** | `O(n)`                    | `O(n)`                      | `O(n)`                       |
| **Encontrar Mín/Máx**| `O(n)`                    | `O(log n)`                  | `O(n)`                       |

*(Nota: Las complejidades para BSTs balanceados incluyen el costo del re-balanceo, que mantiene la altura logarítmica).*

### 🧩 Relación con Otras Estructuras

*   **vs. Arrays / Listas Enlazadas:** Los árboles ofrecen un rendimiento intermedio para búsqueda/inserción/eliminación (`O(log n)` en BSTs balanceados) comparado con `O(1)` (acceso array/list head) vs `O(n)` (array/list search/middle ops). Son más flexibles en tamaño que los arrays y más rápidos que listas enlazadas para búsqueda general.
*   **vs. Grafos:** Un árbol es un tipo especial de grafo: un grafo conexo, acíclico y dirigido donde cada nodo tiene un único padre (excepto la raíz). Los grafos son más generales y permiten ciclos y múltiples padres.
*   **vs. Tablas Hash:** Las Tablas Hash ofrecen búsqueda/inserción/eliminación `O(1)` en promedio, lo cual es mejor que `O(log n)`. Sin embargo, las Tablas Hash no mantienen los datos ordenados y no son eficientes para encontrar el mínimo/máximo o rangos de valores, tareas en las que los BSTs destacan.

---

**Conclusión:**

Los Árboles son estructuras de datos jerárquicas fundamentales. Su principal fortaleza reside en los **Árboles Binarios de Búsqueda (BSTs)**, especialmente cuando están **balanceados** (como AVL o Rojo-Negro), que permiten operaciones de búsqueda, inserción y eliminación con una eficiencia `O(log n)` mucho mayor que las estructuras lineales para grandes volúmenes de datos. Aunque son más complejos de implementar y manejar (especialmente el balanceo y la eliminación) y no permiten acceso `O(1)` por índice, su capacidad para representar relaciones jerárquicas y su rendimiento logarítmico en BSTs balanceados los hacen indispensables en áreas como bases de datos, sistemas de archivos y algoritmia eficiente.
