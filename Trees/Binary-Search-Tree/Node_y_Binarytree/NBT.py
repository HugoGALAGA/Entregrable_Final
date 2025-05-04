class Node:
    """Representa un nodo individual en el árbol binario."""
    def __init__(self, data):
        self.data = data
        self.left = None  # Rama izquierda
        self.right = None # Rama derecha

class BinarySearchTree: # Cambiamos el nombre para ser más específicos
    """Implementación básica de un Árbol Binario de Búsqueda (BST)."""
    def __init__(self):
        self.root = None # La raíz del árbol

    # --- Funcionalidades Principales de BST ---

    def insert(self, data):
        """Inserta un nuevo nodo con 'data' en el árbol, manteniendo la propiedad BST."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        """Método auxiliar recursivo para insertar."""
        # Ignoramos duplicados en esta implementación simple de BST
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        elif data > current_node.data:
             if current_node.right is None:
                current_node.right = Node(data)
             else:
                self._insert_recursive(current_node.right, data)
        # Si data == current_node.data, no hacemos nada (ignorar duplicados)

    def search(self, data):
        """Busca un nodo con 'data' en el árbol, aprovechando la propiedad BST."""
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current_node, data):
        """Método auxiliar recursivo para buscar."""
        if current_node is None:
            return False # No encontrado
        if data == current_node.data:
            return True # Encontrado
        if data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else: # data > current_node.data
            return self._search_recursive(current_node.right, data)

    def delete(self, data):
        """Elimina el nodo con 'data' del árbol, manteniendo la propiedad BST."""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, current_node, data):
        """Método auxiliar recursivo para eliminar."""
        if current_node is None:
            return current_node # El dato no fue encontrado

        # Buscar el nodo a eliminar
        if data < current_node.data:
            current_node.left = self._delete_recursive(current_node.left, data)
        elif data > current_node.data:
            current_node.right = self._delete_recursive(current_node.right, data)
        else: # data == current_node.data, este es el nodo a eliminar

            # Caso 1: Nodo con 0 o 1 hijo
            if current_node.left is None:
                return current_node.right # Reemplaza el nodo actual con su hijo derecho (o None si no hay)
            elif current_node.right is None:
                return current_node.left # Reemplaza con su hijo izquierdo

            # Caso 2: Nodo con 2 hijos
            # Encontrar el sucesor en orden (el menor en el subárbol derecho)
            temp_node = self._find_min_node(current_node.right)
            # Copiar el dato del sucesor al nodo actual
            current_node.data = temp_node.data
            # Eliminar el sucesor (que ahora está en el subárbol derecho del nodo actual)
            current_node.right = self._delete_recursive(current_node.right, temp_node.data)

        return current_node # Retorna la raíz del (sub)árbol modificado

    def _find_min_node(self, node):
        """Encuentra el nodo con el valor mínimo en un subárbol."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    # --- Recorridos (comunes a AB, pero Inorden es especial en BST) ---

    def inorder_traversal(self):
        """Realiza un recorrido en orden (Left -> Root -> Right). Produce datos ordenados en BST."""
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, current_node, elements):
        """Método auxiliar recursivo para recorrido en orden."""
        if current_node:
            self._inorder_recursive(current_node.left, elements)
            elements.append(current_node.data)
            self._inorder_recursive(current_node.right, elements)

    def preorder_traversal(self):
        """Realiza un recorrido pre-orden (Root -> Left -> Right)."""
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements

    def _preorder_recursive(self, current_node, elements):
        """Método auxiliar recursivo para recorrido pre-orden."""
        if current_node:
            elements.append(current_node.data)
            self._preorder_recursive(current_node.left, elements)
            self._preorder_recursive(current_node.right, elements)

    def postorder_traversal(self):
        """Realiza un recorrido post-orden (Left -> Right -> Root)."""
        elements = []
        self._postorder_recursive(self.root, elements)
        return elements

    def _postorder_recursive(self, current_node, elements):
        """Método auxiliar recursivo para recorrido post-orden."""
        if current_node:
            self._postorder_recursive(current_node.left, elements)
            self._postorder_recursive(current_node.right, elements)
            elements.append(current_node.data)

    # --- Otras Funcionalidades ---

    def get_size(self):
        """Retorna el número total de nodos en el árbol."""
        return self._get_size_recursive(self.root)

    def _get_size_recursive(self, current_node):
        """Método auxiliar recursivo para obtener el tamaño."""
        if current_node is None:
            return 0
        return 1 + self._get_size_recursive(current_node.left) + self._get_size_recursive(current_node.right)

    def find_min(self):
        """Encuentra el valor mínimo en el BST (el más a la izquierda)."""
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node.data

    def find_max(self):
        """Encuentra el valor máximo en el BST (el más a la derecha)."""
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node.data
