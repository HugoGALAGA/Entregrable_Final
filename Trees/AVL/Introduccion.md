---

## 🌲 AVL Trees (Árboles AVL)

Un tipo de Árbol Binario de Búsqueda (BST) que es **auto-balanceado**, garantizando así un rendimiento logarítmico (`O(log n)`) para las operaciones clave incluso en el peor caso.

---

### 🤔 ¿Qué son?

Un Árbol AVL es un **Árbol Binario de Búsqueda (BST)** que se adhiere a una propiedad adicional estricta para mantener su altura lo más pequeña posible: la propiedad de **balance AVL**.

*   **Propiedad de Balance AVL:** Para **cualquier nodo** en el árbol, la **diferencia entre la altura de su subárbol izquierdo y la altura de su subárbol derecho** (conocida como el **Factor de Balance**) debe ser **-1, 0, o 1**.

Si en algún momento una operación (inserción o eliminación) causa que el Factor de Balance de algún nodo se vuelva `-2` o `+2`, el árbol realiza automáticamente una o varias **rotaciones** para restaurar la propiedad de balance en ese nodo y sus descendientes, manteniendo el árbol "equilibrado".

Piensa en un Árbol AVL como un **BST muy ordenado y meticuloso** que, cada vez que añades o quitas algo, se "reorganiza" ligeramente de forma automática para asegurarse de que nunca se vuelva demasiado alto en un lado, garantizando que siempre puedas encontrar cualquier cosa rápidamente.

### ⚙️ ¿Cómo Funcionan Internamente?

Un Árbol AVL está compuesto por **nodos** que, además del **dato**, punteros a **hijo izquierdo** y **hijo derecho**, almacenan información sobre su altura o su factor de balance.

*   **Información de Balance:** Cada nodo típicamente guarda la altura de su propio subárbol, o directamente su factor de balance (`altura(izq) - altura(der)`). Esta información permite verificar rápidamente la propiedad de balance en cualquier nodo afectado por una operación.
*   **Rotaciones:** Si una operación rompe la propiedad de balance AVL en un nodo (Factor de Balance es -2 o +2), se realizan rotaciones. Las rotaciones son operaciones locales que **reestructuran una pequeña parte del árbol** (3 nodos involucrados) cambiando los punteros padre-hijo para reducir la altura, **mientras se mantiene la propiedad de BST**. Hay cuatro tipos básicos de rotaciones:
    *   **Rotación Simple a la Izquierda (Left Rotation):** Cuando un nodo está desbalanceado porque su subárbol *derecho* es demasiado alto, y el desbalance está del lado *derecho* del subárbol derecho.
    *   **Rotación Simple a la Derecha (Right Rotation):** Cuando un nodo está desbalanceado porque su subárbol *izquierdo* es demasiado alto, y el desbalance está del lado *izquierdo* del subárbol izquierdo.
    *   **Rotación Doble Izquierda-Derecha (Left-Right Rotation):** Cuando un nodo está desbalanceado porque su subárbol *izquierdo* es demasiado alto, pero el desbalance está del lado *derecho* del subárbol izquierdo. Se realiza una rotación simple a la izquierda en el hijo izquierdo, seguida de una rotación simple a la derecha en el nodo original.
    *   **Rotación Doble Derecha-Izquierda (Right-Left Rotation):** Cuando un nodo está desbalanceado porque su subárbol *derecho* es demasiado alto, pero el desbalance está del lado *izquierdo* del subárbol derecho. Se realiza una rotación simple a la derecha en el hijo derecho, seguida de una rotación simple a la izquierda en el nodo original.

Después de una inserción o eliminación, el algoritmo AVL remonta el camino desde el nodo afectado hasta la raíz, verificando y corrigiendo el balance en cada nodo si es necesario mediante rotaciones. Esto asegura que la propiedad de balance AVL se mantenga en todo momento.

### ⏰ Operaciones Comunes y su Complejidad

La propiedad de balance AVL **garantiza** que la altura `h` del árbol sea siempre `O(log n)`. Por lo tanto, cualquier operación cuya complejidad dependa de la altura será `O(log n)` incluso en el peor caso.

*   **Búsqueda (Search):**
    *   **¿Cómo?** Igual que en un BST estándar: compara el valor, ve a la izquierda si es menor, a la derecha si es mayor.
    *   **Complejidad de Tiempo:** `O(h)`. Como `h = O(log n)`, es **`O(log n)`** (Peor, Promedio y Mejor caso).
    *   **Explicación:** La búsqueda se realiza bajando por el árbol, y la altura está garantizada para ser logarítmica.

*   **Inserción (Insertion):**
    *   **¿Cómo?** Primero, inserta el nuevo nodo como en un BST estándar (`O(h)`). Luego, **re-balancea** el árbol: sube por el camino desde el nuevo nodo hasta la raíz, actualizando alturas y aplicando **rotaciones** si se rompe la propiedad de balance AVL.
    *   **Complejidad de Tiempo:** `O(h)` para la inserción inicial + `O(h)` para el recorrido hacia arriba y chequeo de balance + `O(1)` a `O(log n)` (limitado por `h`) para las rotaciones. Total: **`O(h)`**. Como `h = O(log n)`, es **`O(log n)`** (Peor, Promedio y Mejor caso).
    *   **Explicación:** La inserción inicial es rápida. El costo adicional de mantener el balance (verificación y rotaciones) no excede la altura logarítmica del árbol.

*   **Eliminación (Deletion):**
    *   **¿Cómo?** Es la operación más compleja. Primero, busca el nodo a eliminar (`O(h)`) y elimínalo como en un BST estándar. Luego, **re-balancea** el árbol: sube por el camino desde el nodo afectado (o el sucesor si eliminaste un nodo con dos hijos) hasta la raíz, actualizando alturas y aplicando **rotaciones** si se rompe la propiedad de balance AVL.
    *   **Complejidad de Tiempo:** `O(h)` para la búsqueda y eliminación inicial + `O(h)` para el re-balanceo. Total: **`O(h)`**. Como `h = O(log n)`, es **`O(log n)`** (Peor, Promedio y Mejor caso).
    *   **Explicación:** Similar a la inserción, el costo de mantener el balance después de la eliminación es logarítmico.

*   **Encontrar Mínimo/Máximo:**
    *   **¿Cómo?** Igual que en un BST estándar: sigue los punteros izquierdos para el mínimo, derechos para el máximo.
    *   **Complejidad de Tiempo:** `O(h)`. Como `h = O(log n)`, es **`O(log n)`** (Peor, Promedio y Mejor caso).

*   **Recorrido In-order:**
    *   **¿Cómo?** Recorrer subárbol izquierdo -> visitar nodo actual -> recorrer subárbol derecho.
    *   **Resultado:** Produce una lista de los nodos en orden ascendente.
    *   **Complejidad de Tiempo:** `O(n)`.
    *   **Complejidad de Espacio:** `O(h)` (recursivo) o `O(n)` (iterativo con pila/level-order). La altura `h` es O(log n), por lo que el espacio de pila recursiva es `O(log n)`.

### ✅ Ventajas de los Árboles AVL

*   **Rendimiento Garantizado O(log n):** La principal ventaja. Búsqueda, inserción y eliminación tienen un rendimiento logarítmico **en el peor caso**, a diferencia de los BSTs no balanceados que pueden degradarse a O(n). Esto los hace ideales para aplicaciones donde el rendimiento predecible es crítico.
*   **Búsquedas Ligeramente Más Rápidas:** Tienden a estar más estrictamente balanceados que otros árboles auto-balanceados (como los Rojo-Negro), lo que puede resultar en búsquedas marginalmente más rápidas en promedio.
*   **Mantiene los Datos Ordenados:** El recorrido in-order es `O(n)` y produce los elementos ordenados.

### ❌ Desventajas de los Árboles AVL

*   **Mayor Complejidad de Implementación:** Son significativamente más difíciles de implementar que los BSTs no balanceados debido a la necesidad de rastrear alturas/factores de balance y codificar la lógica de rotación para cuatro casos.
*   **Costos de Actualización Más Altos:** Las operaciones de inserción y eliminación (`O(log n)`) pueden ser ligeramente más lentas en la práctica que en otros árboles auto-balanceados (como los Rojo-Negro) o incluso en el caso promedio de un BST no balanceado, debido a la sobrecarga de verificar y corregir el balance (rotaciones). Requieren más rotaciones en promedio por actualización que los Rojo-Negro.
*   **Memoria Adicional por Nodo:** Cada nodo necesita almacenar su altura o factor de balance.

### 💡 Utilidad y Casos de Uso Comunes

Los Árboles AVL son una excelente opción cuando:

*   Las operaciones de **búsqueda son mucho más frecuentes** que las de inserción y eliminación. Su balance estricto optimiza las búsquedas.
*   Se necesita un **rendimiento garantizado en el peor caso** (`O(log n)`) para las operaciones clave (búsqueda, inserción, eliminación).
*   Se necesita una estructura de datos dinámica que mantenga los elementos ordenados y permita iterar sobre ellos eficientemente.
*   Ejemplos: Bases de datos (aunque B-Trees son más comunes para índices de disco), sistemas de archivos indexados, aplicaciones donde la latencia de búsqueda debe ser lo más baja y predecible posible.

### ⏱️ Complejidad Resumida

| Operación         | AVL Tree            | BST (Promedio)      | BST (Peor Caso)   | Red-Black Tree      |
| :---------------- | :------------------ | :------------------ | :---------------- | :------------------ |
| **Búsqueda**      | `O(log n)`          | `O(log n)`          | `O(n)`            | `O(log n)`          |
| **Inserción**     | `O(log n)`          | `O(log n)`          | `O(n)`            | `O(log n)`          |
| **Eliminación**   | `O(log n)`          | `O(log n)`          | `O(n)`            | `O(log n)`          |
| **Encontrar Mín/Máx**| `O(log n)`          | `O(log n)`          | `O(n)`            | `O(log n)`          |
| **Recorrido (cualquiera)**| `O(n)`              | `O(n)`              | `O(n)`            | `O(n)`              |
| **Acceso por Índice**| `O(n)`              | `O(n)`              | `O(n)`            | `O(n)`              |

*(Nota: Los Árboles Rojo-Negro también son auto-balanceados y garantizan O(log n), a menudo con costos de actualización ligeramente menores en promedio que los AVL, aunque las búsquedas pueden ser marginalmente más lentas debido a un balance menos estricto).*

### 🧩 Relación con Otras Estructuras

*   **vs. BSTs no balanceados:** Un AVL es una mejora directa. Resuelve el problema del peor caso `O(n)` garantizando `O(log n)` mediante balanceo automático.
*   **vs. Red-Black Trees:** Ambos son BSTs auto-balanceados `O(log n)`. AVL mantiene un balance más estricto (diferencia de altura <= 1), mientras que Rojo-Negro permite una diferencia de altura mayor pero requiere menos rotaciones en promedio por actualización. Los Rojo-Negro son a menudo preferidos en implementaciones estándar por sus costos de actualización más consistentes y ligeramente menores en la práctica, mientras que los AVL podrían ser marginalmente mejores si las búsquedas son desproporcionadamente más frecuentes.
*   **vs. Arrays / Linked Lists:** Supera su rendimiento `O(n)` para búsqueda/modificación en medio con `O(log n)`.
*   **vs. Hash Tables:** Las Tablas Hash tienen `O(1)` promedio para búsqueda/modificación (más rápido), pero los AVL mantienen el orden y permiten búsquedas de rango y mínimo/máximo eficientes.

---

**Conclusión:**

Los Árboles AVL son BSTs auto-balanceados que, al mantener una estricta propiedad de balance (Factor de Balance -1, 0, o 1), garantizan un rendimiento **`O(log n)` en el peor caso** para búsqueda, inserción y eliminación. Implementan rotaciones para corregir el balance después de las actualizaciones. Aunque su implementación es más compleja que la de los BSTs no balanceados y pueden tener costos de actualización ligeramente mayores que otros árboles auto-balanceados como los Rojo-Negro, su garantía de rendimiento logarítmico los convierte en una excelente opción para aplicaciones donde la velocidad y predictibilidad de la búsqueda y modificación son primordiales y los datos necesitan estar ordenados.
