# Explicación del Ejemplo 1: Operaciones Básicas
* ***Concepto:*** Un array (lista en Python) es una colección ordenada donde cada elemento tiene un índice numérico (empezando en 0). Permite un acceso y modificación muy rápidos si conoces la posición del elemento.
* **Operaciones:**
  + ***Creación:**** Se muestra cómo inicializar listas vacías o con datos. Las listas de Python son dinámicas y pueden contener elementos de diferentes tipos.
  + ***Acceso ([]):*** Permite obtener o modificar un elemento individual usando su índice (ej: array[0], array[-1]). Es una operación muy eficiente, con complejidad de tiempo O(1) (tiempo constante), ya que la ubicación del elemento se calcula directamente.
  + ***Tamaño (len):*** Obtener el número de elementos también es O(1).
  + ***Recorrido (for):*** Iterar sobre todos los elementos es una operación fundamental con complejidad O(n), donde n es el número de elementos.
  + ***Búsqueda (in, index):*** Buscar si un elemento existe o encontrar su índice requiere, en el peor caso, recorrer todos los elementos. Esto es una búsqueda lineal con complejidad O(n). Intentar acceder a un índice inexistente o buscar un valor inexistente con .index() causa errores (IndexError, ValueError).
  + ***Slicing (:):*** Permite extraer sub-arrays (partes de la lista) o incluso crear una copia o invertir la lista de forma concisa.
