----

## 🌲 Binary Trees (Árboles Binarios)

Un tipo específico de estructura de datos de Árbol donde cada nodo tiene como máximo dos hijos. Son fundamentales en Ciencias de la Computación.

---

### 🤔 ¿Qué son?

Un Árbol Binario es una estructura de datos compuesta por **nodos**, donde cada nodo tiene un valor (dato) y **como máximo dos nodos hijos**, referenciados comúnmente como el **hijo izquierdo** y el **hijo derecho**.

Al igual que un árbol general, tiene una **raíz** (el nodo superior sin padre) y aristas que conectan padres con hijos. La característica binaria es la restricción en el número de hijos por nodo.

Piensa en ello como un **organigrama simplificado** donde cada persona (nodo) en el organigrama puede tener como máximo dos subordinados directos (hijos izquierdo y derecho).

### ⚙️ ¿Cómo Funcionan Internamente?

Un Árbol Binario se implementa generalmente utilizando **nodos** que contienen:

1.  El **dato** o valor del nodo.
2.  Un **puntero** (o referencia) al **hijo izquierdo**.
3.  Un **puntero** (o referencia) al **hijo derecho**.

Si un nodo no tiene hijo izquierdo o derecho, el puntero correspondiente es `null` (o equivalente). El árbol en sí se maneja a través de un puntero a su **raíz**.

**Terminología Relevante (Revisión para Binarios):**

La terminología de árboles generales aplica a los árboles binarios:

*   **Raíz (Root):** El nodo superior.
*   **Nodo Padre (Parent Node):** Un nodo que tiene uno o dos hijos.
*   **Nodos Hijos (Child Nodes):** Nodos directamente conectados debajo de un padre (específicamente, **hijo izquierdo** y **hijo derecho**).
*   **Hoja (Leaf Node):** Un nodo sin hijos.
*   **Subárbol Izquierdo (Left Subtree):** El subárbol cuya raíz es el hijo izquierdo de un nodo.
*   **Subárbol Derecho (Right Subtree):** El subárbol cuya raíz es el hijo derecho de un nodo.
*   **Profundidad (Depth):** Distancia desde la raíz.
*   **Altura (Height):** Distancia desde un nodo hasta la hoja más lejana en sus descendientes.

### 🌳 Tipos Específicos de Árboles Binarios

La estructura de un árbol binario puede variar, dando lugar a diferentes tipos con propiedades útiles:

*   **Árbol Binario Completo (Complete Binary Tree):** Un árbol binario en el que todos los niveles, **excepto quizás el último**, están completamente llenos, y todos los nodos en el último nivel están tan a la **izquierda como sea posible**.
*   **Árbol Binario Lleno (Full Binary Tree):** Un árbol binario en el que **cada nodo tiene 0 o 2 hijos**. No hay nodos con un solo hijo.
*   **Árbol Binario Perfecto (Perfect Binary Tree):** Un árbol binario que es **tanto lleno como completo**. Todos los nodos internos tienen dos hijos, y todas las hojas están en el mismo nivel. La altura `h` está directamente relacionada con el número de nodos `n` por la fórmula `n = 2^(h+1) - 1`.
*   **Árbol Degenerado o Puntiagudo (Degenerate or Skewed Tree):** Un árbol binario en el que cada nodo padre tiene **un solo hijo**. Se comporta esencialmente como una Lista Enlazada. Pueden ser completamente inclinados a la izquierda o a la derecha.

### ⏰ Operaciones Comunes y su Complejidad

Las operaciones básicas en un Árbol Binario (que *no* es necesariamente un Árbol Binario de Búsqueda) suelen implicar recorrer el árbol. La complejidad de búsqueda, inserción o eliminación *sin una propiedad de orden* es generalmente lineal.

*   **Recorrido (Traversal):** Visitar cada nodo. Los tres recorridos principales (definidos en la explicación de árboles generales) son fundamentales para Árboles Binarios debido a sus dos hijos:
    *   **In-order (Inorden):** Recorrer el subárbol izquierdo, visitar el nodo actual, recorrer el subárbol derecho.
    *   **Pre-order (Preorden):** Visitar el nodo actual, recorrer el subárbol izquierdo, recorrer el subárbol derecho.
    *   **Post-order (Postorden):** Recorrer el subárbol izquierdo, recorrer el subárbol derecho, visitar el nodo actual.
    *   **Level-order (Por Niveles):** Visitar nodos nivel por nivel. Se usa una **Queue** para implementarlo de forma eficiente.
    *   **Complejidad de Tiempo para todos los recorridos:** `O(n)` para visitar cada uno de los `n` nodos.
    *   **Complejidad de Espacio para recorridos recursivos (In/Pre/Post):** `O(h)` en el peor caso (altura del árbol, debido a la pila de llamadas). Puede ser `O(n)` en un árbol degenerado.
    *   **Complejidad de Espacio para recorrido Level-order:** `O(ancho máximo)` del árbol, que en el peor caso (árbol completo) es `O(n/2)`, es decir, `O(n)`, debido al espacio de la Queue.

*   **Búsqueda (Search):**
    *   **¿Cómo?** Para encontrar un valor específico en un **Árbol Binario general (no ordenado)**, debes realizar un recorrido (ej: Pre-order o Level-order) y comparar el valor buscado con el dato de cada nodo hasta encontrarlo o haber visitado todos los nodos.
    *   **Complejidad de Tiempo:** `O(n)` en el peor caso (el elemento no está o es el último visitado).
    *   **Explicación:** Debes visitar hasta `n` nodos. (¡Contraste esto con la búsqueda en un BST que es O(h)!)

*   **Inserción (Insertion):**
    *   **¿Cómo?** La forma de insertar un nuevo nodo en un **Árbol Binario general** depende de las reglas específicas o el propósito del árbol. A menudo, se busca la primera posición "disponible" para mantener una estructura completa (similar a cómo se llena un heap en un array) o se inserta basándose en alguna otra lógica, no en el valor del nodo.
    *   **Complejidad de Tiempo:** `O(n)` en el peor caso para encontrar el lugar de inserción si no hay una regla estructurada clara (requiere un recorrido o búsqueda de la posición). `O(1)` para realizar el enlace una vez encontrado el lugar. En algunos casos, si se sigue una estrategia específica (como llenar por niveles), encontrar la posición puede ser O(log n) o O(h).
    *   **Explicación:** Sin una propiedad de orden, encontrar dónde poner el nuevo nodo para mantener alguna estructura o simplemente añadirlo en un lugar específico suele requerir recorrer el árbol.

*   **Eliminación (Deletion):**
    *   **¿Cómo?** Eliminar un nodo en un **Árbol Binario general** también depende de las reglas. Una vez encontrado el nodo a eliminar (`O(n)` búsqueda), la forma de reestructurar el árbol para llenar el hueco puede variar. Una estrategia común es reemplazar el nodo eliminado con el último nodo en un recorrido (ej: Level-order) y luego eliminar ese último nodo de su posición original.
    *   **Complejidad de Tiempo:** `O(n)` en el peor caso (búsqueda + reestructuración).
    *   **Explicación:** Similar a la inserción, la falta de una regla de orden hace que encontrar y reestructurar sea una operación potencialmente lineal.

### ✅ Ventajas de los Árboles Binarios

*   **Representación de Relaciones Jerárquicas Específicas:** Útil cuando las relaciones padre-hijo se limitan a un máximo de dos.
*   **Base para Estructuras Eficientes:** Son el fundamento conceptual y estructural para los Árboles Binarios de Búsqueda (BSTs) y los Heaps, que sí ofrecen eficiencias logarítmicas para ciertas operaciones.
*   **Natural para Problemas Binarios:** Adecuado para representar estructuras de decisión binarias, expresiones matemáticas (donde cada operador binario tiene dos operandos), etc.
*   **Los recorridos son bien definidos:** Los algoritmos de recorrido (In-order, Pre-order, Post-order, Level-order) son estándar y muy útiles para procesar todos los nodos.

### ❌ Desventajas de los Árboles Binarios

*   **Búsqueda, Inserción y Eliminación Lenta (sin Orden):** A menos que se aplique una propiedad de orden (como en un BST), estas operaciones son `O(n)`, requiriendo un recorrido completo en el peor caso.
*   **Más Complejos que las Estructuras Lineales:** Implican manejo de múltiples punteros por nodo.
*   **Consumo de Memoria por Punteros:** Cada nodo requiere memoria para sus dos punteros hijos (incluso si son `null`).

### 💡 Utilidad y Casos de Uso Comunes

Los Árboles Binarios (en su forma general o tipos específicos) se utilizan en:

*   **Árboles de Expresión (Expression Trees):** Para representar expresiones matemáticas o lógicas. Los nodos hoja son operandos, y los nodos internos son operadores.
*   **Árboles de Decisión (Decision Trees):** En aprendizaje automático y teoría de decisiones, representan una secuencia de decisiones binarias y sus posibles resultados.
*   **Compiladores:** Los Árboles de Sintaxis Abstracta (ASTs) a menudo tienen una estructura binaria para representar operaciones y estructuras de control.
*   **Como Base para Implementar Otras Estructuras:** Son el esqueleto sobre el que se construyen BSTs, Árboles AVL, Árboles Rojo-Negro y Heaps.
*   **Algoritmos de Compresión:** Árboles de Huffman para compresión de datos.

### ⏱️ Complejidad Resumida (Árbol Binario General)

| Operación              | Complejidad de Tiempo (Peor) | Complejidad de Espacio (Peor) | Notas                                    |
| :--------------------- | :--------------------------- | :---------------------------- | :--------------------------------------- |
| **Recorrido (Cualquiera)**| `O(n)`                       | `O(h)` (recursivo), `O(n)` (por niveles) | Se visitan todos los `n` nodos. Altura `h`.|
| **Búsqueda por Valor** | `O(n)`                       | `O(h)` (recursivo para el recorrido) | Requiere escanear, en el peor caso.      |
| **Inserción**          | `O(n)`                       | `O(h)` (si se busca pos recursivamente) | Depende de la regla de inserción.       |
| **Eliminación**        | `O(n)`                       | `O(h)`                        | Depende de la regla de eliminación.      |
| **Encontrar Raíz**     | `O(1)`                       | `O(1)`                        | Asumiendo que se mantiene un puntero a la raíz. |

*(Nota: Las complejidades de Inserción/Eliminación/Búsqueda son `O(n)` en un árbol binario general porque no hay una propiedad de orden que te permita descartar partes del árbol. Debes buscar el nodo o la posición, lo que requiere un recorrido o una búsqueda que, en el peor caso, visita la mayoría de los nodos).*

### 🧩 Relación con Otras Estructuras

*   **vs. Árbol General:** Un Árbol Binario es un caso especial de Árbol General donde el número de hijos está limitado a dos.
*   **vs. BST (Árbol Binario de Búsqueda):** Un BST es un **tipo** de Árbol Binario que añade una propiedad de orden a la colocación de los nodos (menores a la izquierda, mayores a la derecha). Esta propiedad de orden es lo que transforma la Búsqueda, Inserción y Eliminación de `O(n)` a `O(h)` (potencialmente `O(log n)` si está balanceado).
*   **vs. Arrays/Listas Enlazadas:** Son no lineales y no soportan acceso O(1) por índice como los arrays. Su flexibilidad de tamaño es similar a las listas enlazadas, pero su estructura jerárquica es fundamentalmente diferente.

---

**Conclusión:**

Los Árboles Binarios son estructuras jerárquicas clave, definidas por la restricción de tener como máximo dos hijos por nodo. Son el **esqueleto** sobre el que se construyen estructuras más especializadas y eficientes como los Árboles Binarios de Búsqueda (BSTs) y los Heaps. Mientras que las operaciones de búsqueda, inserción y eliminación en un árbol binario *general* son típicamente `O(n)`, la estructura binaria es ideal para ciertos tipos de problemas (como expresiones o decisiones) y, lo más importante, sirve como base fundamental para comprender estructuras arbóreas más avanzadas que sí logran un rendimiento logarítmico al añadir propiedades de orden o balanceo. Los recorridos (`In-order`, `Pre-order`, `Post-order`, `Level-order`) son operaciones estándar y eficientes (`O(n)`) para procesar todos sus nodos.
