# Explicación del Ejemplo 2:
+ ***Concepto:*** Este ejemplo muestra la naturaleza "dinámica" de las listas en Python. Aunque aún mantienen la idea de elementos ordenados por índice, no tienen un tamaño fijo. Pueden crecer o encogerse.
+ Inserción (append, insert):
  + ***append:*** Añadir al final es rápido en promedio (O(1)). El motivo es que las listas reservan más memoria de la que necesitan inicialmente, dejando espacio para futuras adiciones al final. Solo cuando ese espacio extra se llena, el sistema necesita crear una nueva lista más grande y copiar todos los elementos, lo cual es O(n), pero esto es poco frecuente y el costo se "reparte" a lo largo de muchas operaciones.
  + ***insert:*** Añadir en cualquier otra posición (especialmente al principio o en medio) es costoso (O(n)). Esto se debe a que, para mantener el orden y la contigüidad lógica, todos los elementos que vienen después del punto de inserción deben ser movidos una posición a la derecha.
+ Eliminación (pop, remove):
  + ***pop():*** Eliminar el último elemento es rápido (O(1)), ya que no se necesita mover ningún otro elemento.
  + ***pop(index):*** Eliminar por índice es costoso (O(n)) si el índice no es el último, por la misma razón que insert: los elementos después del punto de eliminación deben ser movidos (esta vez a la izquierda) para llenar el hueco.
  + ***remove(value):*** Eliminar por valor tiene una complejidad de O(n) porque primero debe encontrar el valor (lo cual es O(n) en el peor caso) y luego eliminarlo (lo cual implica mover elementos, O(n)).
#### Este ejemplo ilustra que, si bien los arrays/listas permiten inserciones y eliminaciones, estas operaciones pueden ser ineficientes si no se realizan en los extremos, lo que contrasta con otras estructuras de datos como las listas enlazadas, donde la inserción/eliminación es O(1) en cualquier punto (si ya tienes una referencia al nodo), pero el acceso por índice es lento (O(n)).
