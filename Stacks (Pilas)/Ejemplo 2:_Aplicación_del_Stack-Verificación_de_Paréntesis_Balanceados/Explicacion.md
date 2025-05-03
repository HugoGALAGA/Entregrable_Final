# Explicación del Ejemplo 2: Verificación de Paréntesis Balanceados
+ ***Problema:*** Determinar si cada delimitador de apertura ((, [, {) tiene un delimitador de cierre correspondiente (), ], }) en el orden correcto de anidación.
+ ***Uso del Stack:*** La propiedad LIFO del Stack es perfecta para esto. Cuando encontramos un delimitador de apertura, lo "recordamos" haciendo un push al Stack. Cuando encontramos un delimitador de cierre, sabemos que el delimitador de apertura más reciente (el que está en el tope del Stack) debería ser su pareja.
+ ***Algoritmo:***
  + Inicializar un Stack vacío.
  + Definir un mapeo que relacione cada delimitador de cierre con su correspondiente de apertura.
  + Iterar a través de la cadena de entrada carácter por carácter.
  + Si el carácter es un delimitador de apertura, hacer push a Stack.
  + Si el carácter es un delimitador de cierre:
    + Verificar si el Stack está vacío. Si lo está, hay un cierre sin un apertura previo -> la expresión no está balanceada.
    + Hacer pop al Stack para obtener el delimitador de apertura más reciente.
    + Comparar el delimitador sacado con el que debería corresponder al cierre actual (usando el mapeo). Si no coinciden, la anidación es incorrecta -> la expresión no está balanceada.
  + Después de procesar toda la cadena, si el Stack está vacío, significa que todos los delimitadores de apertura encontraron su pareja -> la expresión está balanceada. Si el Stack no está vacío, significa que quedaron delimitadores de apertura sin cerrar -> la expresión no está balanceada.
#### Complejidad: El algoritmo recorre la cadena de entrada una vez (O(n), donde n es la longitud de la cadena). Las operaciones de Stack (push, pop, is_empty) son O(1). Por lo tanto, la complejidad de tiempo total es O(n). La complejidad de espacio es O(k) en el peor caso, donde k es la anidación máxima de los delimitadores (es decir, el tamaño máximo que alcanza el Stack).
