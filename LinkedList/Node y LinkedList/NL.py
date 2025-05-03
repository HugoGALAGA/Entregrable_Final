class Node:
    """Representa un nodo individual en la lista enlazada."""
    def __init__(self, data):
        self.data = data  # El dato que guarda el nodo
        self.next = None  # Referencia al siguiente nodo, inicialmente None

class LinkedList:
    """Implementación básica de una lista enlazada simple."""
    def __init__(self):
        self.head = None # La cabeza de la lista, inicialmente vacía

    # --- Funcionalidades Principales ---

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if not self.head: # Si la lista está vacía
            self.head = new_node
            return
        # Si no está vacía, recorre hasta el último nodo
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node # El último nodo ahora apunta al nuevo

    def prepend(self, data):
        """Agrega un nuevo nodo al principio de la lista."""
        new_node = Node(data)
        new_node.next = self.head # El nuevo nodo apunta a la cabeza actual
        self.head = new_node      # La cabeza ahora es el nuevo nodo

    def delete_node(self, key):
        """Elimina el primer nodo que contiene el valor 'key'."""
        current_node = self.head

        # Caso 1: El nodo a eliminar es la cabeza
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None # Elimina la referencia
            return True # Indica que se eliminó

        # Caso 2: Buscar el nodo en el resto de la lista
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # Si el nodo no fue encontrado
        if current_node is None:
            #print(f"Advertencia: Nodo con data '{key}' no encontrado.") # Opcional
            return False # Indica que no se encontró

        # Si el nodo fue encontrado (current_node no es None)
        prev.next = current_node.next # El nodo anterior apunta al siguiente del nodo a eliminar
        current_node = None # Elimina la referencia
        return True # Indica que se eliminó

    def display(self):
        """Imprime los elementos de la lista enlazada."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)) if elements else "Lista Vacía")

    def search(self, key):
        """Busca un nodo con el valor 'key'."""
        current = self.head
        while current:
            if current.data == key:
                return True # Encontrado
            current = current.next
        return False # No encontrado

    def get_size(self):
        """Retorna el número de elementos en la lista."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.head is None
