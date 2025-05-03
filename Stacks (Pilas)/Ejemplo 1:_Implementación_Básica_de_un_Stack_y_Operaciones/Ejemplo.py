# Ejemplo 1: Implementación Básica de un Stack y Operaciones

print("--- Ejemplo 1: Implementación Básica ---")

class Stack:
    """
    Implementación básica de un Stack (Pila) usando una lista de Python.
    """
    def __init__(self):
        """Inicializa un Stack vacío."""
        self.items = [] # La lista para almacenar los elementos de la pila

    def is_empty(self):
        """Verifica si la pila está vacía."""
        # Si la lista está vacía, el Stack está vacío.
        return not self.items

    def push(self, item):
        """Añade un elemento a la parte superior del Stack."""
        # Añadir al final de la lista es eficiente en Python (O(1) amortizado).
        self.items.append(item)
        print(f"Push: '{item}' añadido al Stack.")

    def pop(self):
        """
        Elimina y devuelve el elemento de la parte superior del Stack.
        Lanza un error si el Stack está vacío.
        """
        if not self.is_empty():
            # pop() en listas de Python elimina y devuelve el último elemento (O(1)).
            elemento_superior = self.items.pop()
            print(f"Pop: '{elemento_superior}' eliminado del Stack.")
            return elemento_superior
        else:
            print("Pop: Error - El Stack está vacío.")
            # Puedes lanzar una excepción para manejar esto más formalmente
            # raise IndexError("pop from empty stack")
            return None # O retornar None/manejar el error de otra forma

    def peek(self):
        """
        Mira el elemento de la parte superior del Stack sin eliminarlo.
        Lanza un error si el Stack está vacío.
        """
        if not self.is_empty():
            # Acceder al último elemento [-1] es eficiente (O(1)).
            elemento_superior = self.items[-1]
            print(f"Peek: El elemento superior es '{elemento_superior}'.")
            return elemento_superior
        else:
            print("Peek: Error - El Stack está vacío.")
            # raise IndexError("peek from empty stack")
            return None

    def size(self):
        """Devuelve el número de elementos en el Stack."""
        # len() en listas de Python es eficiente (O(1)).
        tam = len(self.items)
        print(f"Size: El Stack contiene {tam} elemento(s).")
        return tam

    def __str__(self):
        """Representación amigable del Stack."""
        # Muestra los elementos, con el tope a la derecha.
        return f"Stack actual (tope a la derecha): {self.items}"

# --- Uso del Stack ---
mi_pila = Stack()

# 1. Verificar si está vacío
mi_pila.is_empty()
mi_pila.size()

# 2. Añadir elementos (Push)
mi_pila.push("Plato 1")
mi_pila.push("Plato 2")
mi_pila.push("Plato 3")
print(mi_pila) # Muestra el Stack actual

# 3. Mirar el elemento superior (Peek)
mi_pila.peek()

# 4. Verificar el tamaño
mi_pila.size()

# 5. Eliminar elementos (Pop)
mi_pila.pop() # Elimina Plato 3
print(mi_pila)
mi_pila.peek() # El nuevo tope es Plato 2
mi_pila.pop() # Elimina Plato 2
print(mi_pila)

# 6. Eliminar el último elemento
mi_pila.pop() # Elimina Plato 1
print(mi_pila)

# 7. Intentar Pop y Peek en un Stack vacío
mi_pila.is_empty()
mi_pila.pop()
mi_pila.peek()
mi_pila.size()


print("\n--- Fin Ejemplo 1 ---")
