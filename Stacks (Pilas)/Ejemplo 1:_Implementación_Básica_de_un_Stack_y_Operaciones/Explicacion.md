# Explicación del Ejemplo 1 Implementación Básica
* ***Concepto:*** Un Stack es una colección LIFO. Implementarlo con una lista de Python es eficiente porque añadir y quitar del final (append() y pop()) son operaciones de tiempo constante amortizado (O(1)).
  + ***Clase Stack:*** Se define una clase para encapsular la lógica de la pila. La lista self.items almacena los elementos.
  + ***__init__:*** Crea una lista vacía al inicializar el Stack.
  + ***is_empty():*** Retorna True si la lista está vacía, False de lo contrario. Eficiencia O(1).
  + ***push(item):*** Usa self.items.append(item) para añadir el nuevo elemento al final de la lista, que consideramos el "tope" del Stack. Eficiencia O(1) (amortizado).
  + ***pop():*** Primero verifica si el Stack está vacío para evitar errores. Si no lo está, usa self.items.pop() para eliminar y devolver el último elemento (el tope). Eficiencia O(1).
  + ***peek():*** También verifica si está vacío. Si no lo está, usa self.items[-1] para acceder al último elemento (el tope) sin eliminarlo. Eficiencia O(1).
  + ***size():*** Usa len(self.items) para obtener el número de elementos. Eficiencia O(1).
  + ***__str__:*** Proporciona una forma sencilla de imprimir el contenido del Stack.
#### Este ejemplo demuestra cómo las operaciones clave de un Stack se mapean directamente a operaciones eficientes en el final de una lista de Python, haciendo que esta implementación sea práctica.
