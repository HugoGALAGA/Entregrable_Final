---

## 📦 Stacks (Pilas)

Una estructura de datos lineal que sigue el principio **LIFO** (Last-In, First-Out - Último en Entrar, Primero en Salir).

---

### 🤔 ¿Qué son?

Una Pila es una colección de elementos con dos operaciones principales:

*   **Agregar** un elemento a la parte superior de la pila (`push`).
*   **Eliminar** el elemento de la parte superior de la pila (`pop`).

Piensa en una pila como una **pila de platos**: solo puedes poner un plato nuevo encima del último que pusiste (`push`), y solo puedes quitar el plato que está justo en la parte superior (`pop`). El último plato que pones es, necesariamente, el primero que quitas.

### ⚙️ ¿Cómo Funcionan Internamente?

Las pilas se implementan típicamente utilizando otras estructuras de datos subyacentes:

*   **Usando Arrays (Arreglos):**
    *   Se usa un array y un índice para rastrear la "cima" de la pila.
    *   `push`: Se añade el elemento al final lógico del array y se incrementa el índice de la cima.
    *   `pop`: Se devuelve el elemento en el índice de la cima y se decrementa el índice.
    *   *Consideraciones:* Requiere manejo de tamaño fijo o implementación de array dinámico (que redimensiona el array subyacente si se llena, lo cual es costoso).
*   **Usando Listas Enlazadas:**
    *   Se usa una lista enlazada simple, donde la "cima" de la pila es la cabeza de la lista.
    *   `push`: Se crea un nuevo nodo y se convierte en la nueva cabeza de la lista, apuntando a la antigua cabeza.
    *   `pop`: Se devuelve el valor de la cabeza actual, y la cabeza se actualiza al siguiente nodo.
    *   *Consideraciones:* No hay problema de tamaño fijo, pero cada nodo tiene el overhead de un puntero.

Independientemente de la implementación subyacente, las operaciones `push` y `pop` se diseñan para ser muy rápidas, centrándose siempre en un extremo (la "cima").

### ⏰ Operaciones Comunes y su Complejidad

Las operaciones fundamentales de una Pila se enfocan en la "cima". Su eficiencia es la principal razón para usarlas en ciertos escenarios.

*   **`push(elemento)`:**
    *   **¿Cómo?** Agrega un `elemento` a la cima de la pila.
    *   **Complejidad de Tiempo:** `O(1)` (Constante).
    *   **Explicación:** La operación solo implica añadir al final de un array (si hay espacio) o al inicio de una lista enlazada, lo cual es una operación de tiempo constante.

*   **`pop()`:**
    *   **¿Cómo?** Elimina y devuelve el elemento de la cima de la pila.
    *   **Complejidad de Tiempo:** `O(1)` (Constante).
    *   **Explicación:** Similar a `push`, solo implica remover del final de un array (ajustando el índice) o del inicio de una lista enlazada, lo cual es O(1). Se debe manejar el caso de pila vacía.

*   **`peek()` / `top()`:**
    *   **¿Cómo?** Devuelve el elemento de la cima de la pila *sin eliminarlo*.
    *   **Complejidad de Tiempo:** `O(1)` (Constante).
    *   **Explicación:** Solo requiere acceder al elemento referenciado por el puntero/índice de la cima. Se debe manejar el caso de pila vacía.

*   **`isEmpty()`:**
    *   **¿Cómo?** Verifica si la pila no contiene elementos.
    *   **Complejidad de Tiempo:** `O(1)` (Constante).
    *   **Explicación:** Generalmente se basa en verificar si el índice de la cima es -1 o si el puntero a la cabeza es nulo.

*   **`size()`:**
    *   **¿Cómo?** Devuelve el número de elementos en la pila.
    *   **Complejidad de Tiempo:** `O(1)` (Constante), si se mantiene un contador. `O(n)` si requiere recorrer todos los elementos (implementación ineficiente).
    *   **Explicación:** Si la implementación incluye un contador que se incrementa en `push` y decrementa en `pop`, obtener el tamaño es instantáneo.

### ✅ Ventajas de las Pilas

*   **Simplicidad:** Conceptualmente sencillas de entender.
*   **Eficiencia Extrema para Operaciones Principales:** `push`, `pop`, `peek`, `isEmpty` son todas `O(1)`. Esto las hace muy rápidas para sus operaciones específicas.
*   **Enfocan en el Principio LIFO:** Esto es una ventaja cuando la lógica del problema se alinea con este orden (ej: deshacer, historial reciente).

### ❌ Desventajas de las Pilas

*   **Acceso Limitado:** Solo puedes acceder al elemento superior. No permiten acceso aleatorio a elementos en medio o al fondo sin alterar la pila (sacando elementos superiores).
*   **Búsqueda Ineficiente:** Encontrar un elemento específico (que no sea la cima) es `O(n)` en el peor caso, ya que requiere vaciar parcialmente la pila hasta encontrarlo.

### 💡 Utilidad y Casos de Uso Comunes

Las pilas son muy útiles en escenarios donde el orden LIFO es natural o requerido:

*   **Pila de Llamadas a Funciones (Call Stack):** Los lenguajes de programación usan una pila para gestionar las llamadas a funciones. Cuando llamas a una función, su contexto se "apila". Cuando termina, su contexto se "desapila".
*   **Funcionalidad Deshacer/Rehacer (Undo/Redo):** Cada acción que realizas se "apila". Para deshacer, "desapilas" la última acción.
*   **Evaluación de Expresiones:** Usado en compiladores para convertir expresiones (como `a + b * c`) a formas que son más fáciles de evaluar (como notación postfija o prefija).
*   **Recorridos en Grafos/Árboles (DFS):** En algoritmos de Búsqueda en Profundidad (Depth-First Search), se puede usar una pila explícitamente para rastrear los nodos a visitar.
*   **Navegación Web (Historial 'Atrás'):** El historial de páginas visitadas a menudo se maneja como una pila. Cuando presionas "Atrás", "desapilas" la página actual para volver a la anterior.
*   **Verificación de Parentesis Balanceados:** Para asegurarse de que los paréntesis, corchetes y llaves en una expresión estén correctamente anidados y cerrados.

---

Las Pilas son estructuras simples pero poderosas gracias a la eficiencia `O(1)` de sus operaciones clave. Son la elección natural cuando necesitas manejar elementos en un estricto orden LIFO, a pesar de su limitado acceso a elementos que no están en la cima.
