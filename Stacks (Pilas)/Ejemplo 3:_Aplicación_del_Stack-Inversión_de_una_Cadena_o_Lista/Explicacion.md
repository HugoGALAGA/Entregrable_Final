# Explicación del Ejemplo 3: Inversión de una Cadena o Lista
+ ***Problema:*** Obtener una nueva secuencia con los elementos en el orden opuesto al de la secuencia original.
+ ***Uso del Stack:*** La naturaleza LIFO de un Stack es inherentemente inversa al orden de entrada. Si añades elementos uno por uno, al sacarlos, el último que metiste (el tope) será el primero en salir, luego el penúltimo, y así sucesivamente, resultando en el orden inverso de la entrada.
+ ***Algoritmo:***
  + Inicializar un Stack vacío.
  + Recorrer la secuencia de entrada (cadena o lista). Para cada elemento, hacer push al Stack.
  + Inicializar una nueva secuencia vacía (una lista para construir el resultado).
  + Mientras el Stack no esté vacío, hacer pop para obtener el elemento del tope y añadirlo a la nueva secuencia.
  + Finalmente, si la entrada original era una cadena, unir los caracteres resultantes en una sola cadena. Si era una lista (u otro iterable), devolver la lista construida.
+ ***Complejidad:*** El algoritmo implica dos pasadas por los datos: una para empujar al Stack y otra para sacar y añadir al resultado. Cada elemento se empuja una vez y se saca una vez. Las operaciones de Stack (push, pop, is_empty) son O(1). Por lo tanto, la complejidad de tiempo es O(n), donde n es el número de elementos en la secuencia. La complejidad de espacio es O(n) porque el Stack necesita almacenar todos los elementos de la secuencia en el peor caso.
#### Este ejemplo ilustra cómo el Stack puede ser una herramienta útil cuando necesitas procesar elementos en el orden inverso a como fueron recibidos o generados, similar a cómo funciona la pila de llamadas de funciones en los lenguajes de programación.
