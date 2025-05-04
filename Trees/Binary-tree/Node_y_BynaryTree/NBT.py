class Node:
    """Representa un nodo individual en el árbol binario."""
    def __init__(self, data):
        self.data = data
        self.left = None  # Rama izquierda
        self.right = None # Rama derecha

class BinaryTree: # Usaremos un BST para los ejemplos
    """Implementación básica de un Árbol Binario de Búsqueda (BST)."""
    def __init__(self):
        self.root = None # La raíz del árbol

    # --- Funcionalidades Principales ---

    def insert(self, data):
        """Inserta un nuevo nodo con 'data' en el árbol."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        """Método auxiliar recursivo para insertar."""
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        elif data > current_node.data: # Para BST, no permitimos duplicados o los tratamos como mayores/menores
             if current_node.right is None:
                current_node.right = Node(data)
             else:
                self._insert_recursive(current_node.right, data)
        # else: data is equal, do nothing (simple BST usually avoids duplicates)

    def search(self, data):
        """Busca un nodo con 'data' en el árbol."""
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

    def inorder_traversal(self):
        """Realiza un recorrido en orden (Left -> Root -> Right)."""
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

    def get_size(self):
        """Retorna el número total de nodos en el árbol."""
        return self._get_size_recursive(self.root)

    def _get_size_recursive(self, current_node):
        """Método auxiliar recursivo para obtener el tamaño."""
        if current_node is None:
            return 0
        return 1 + self._get_size_recursive(current_node.left) + self._get_size_recursive(current_node.right)

    def find_min(self):
        """Encuentra el valor mínimo en el BST."""
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node.data

    def find_max(self):
        """Encuentra el valor máximo en el BST."""
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node.data
