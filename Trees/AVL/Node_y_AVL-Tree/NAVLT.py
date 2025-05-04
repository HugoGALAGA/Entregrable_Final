class Node:
    """Representa un nodo individual en el árbol AVL."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1 # La altura del nodo (una hoja tiene altura 1)

class AVLTree:
    """Implementación básica de un Árbol AVL (Auto-balanceado)."""
    def __init__(self):
        self.root = None

    # --- Funcionalidades de Altura y Balance ---

    def get_height(self, node):
        """Retorna la altura de un nodo (o 0 si es None)."""
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node):
        """Calcula el factor de balance de un nodo."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _update_height(self, node):
        """Actualiza la altura de un nodo basado en las alturas de sus hijos."""
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # --- Rotaciones (para balancear) ---

    def _rotate_right(self, y):
        """Realiza una rotación a la derecha con 'y' como raíz desbalanceada."""
        x = y.left
        T2 = x.right

        # Realizar rotación
        x.right = y
        y.left = T2

        # Actualizar alturas
        self._update_height(y)
        self._update_height(x)

        return x # Nueva raíz del subárbol

    def _rotate_left(self, x):
        """Realiza una rotación a la izquierda con 'x' como raíz desbalanceada."""
        y = x.right
        T2 = y.left

        # Realizar rotación
        y.left = x
        x.right = T2

        # Actualizar alturas
        self._update_height(x)
        self._update_height(y)

        return y # Nueva raíz del subárbol

    # --- Insertar ---

    def insert(self, data):
        """Inserta un nuevo nodo y rebalancea si es necesario."""
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Método auxiliar recursivo para insertar y rebalancear."""
        # 1. Inserción normal de BST
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        else: # Ignorar duplicados para este ejemplo
            return node

        # 2. Actualizar altura del nodo actual
        self._update_height(node)

        # 3. Obtener factor de balance y rebalancear si es necesario
        balance = self.get_balance_factor(node)

        # Casos de desbalance:
        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self._rotate_left(node)

        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node # Retorna el nodo (posiblemente después de rebalancear)

    # --- Eliminar ---

    def delete(self, data):
        """Elimina un nodo y rebalancea si es necesario."""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        """Método auxiliar recursivo para eliminar y rebalancear."""
        # 1. Eliminación normal de BST
        if not node:
            return node # Nodo no encontrado

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else: # Nodo a eliminar encontrado
            # Caso 1: Nodo con 0 o 1 hijo
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            # Caso 2: Nodo con 2 hijos
            temp = self._find_min_node(node.right) # Encontrar el sucesor in-order
            node.data = temp.data # Copiar dato del sucesor al nodo actual
            node.right = self._delete_recursive(node.right, temp.data) # Eliminar el sucesor

        # Si el árbol tenía solo un nodo, retornamos ahora
        if not node:
            return node

        # 2. Actualizar altura del nodo actual
        self._update_height(node)

        # 3. Obtener factor de balance y rebalancear si es necesario
        balance = self.get_balance_factor(node)

        # Casos de desbalance:
        # Left Left Case
        if balance > 1 and self.get_balance_factor(node.left) >= 0:
            return self._rotate_right(node)

        # Left Right Case
        if balance > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and self.get_balance_factor(node.right) <= 0:
            return self._rotate_left(node)

        # Right Left Case
        if balance < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node # Retorna el nodo (posiblemente después de rebalancear)


    def _find_min_node(self, node):
        """Encuentra el nodo con el valor mínimo en un subárbol."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    # --- Búsqueda (Igual que BST, pero performance garantizada) ---

    def search(self, data):
        """Busca un nodo, aprovechando la propiedad BST y la altura O(log n)."""
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        """Método auxiliar recursivo para buscar."""
        if not node:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    # --- Recorridos (útiles para visualización y verificación del orden) ---

    def inorder_traversal(self):
        """Recorrido en orden (siempre ordenado en BST/AVL)."""
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.data)
            self._inorder_recursive(node.right, elements)

    def preorder_traversal(self):
        """Recorrido pre-orden."""
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements

    def _preorder_recursive(self, node, elements):
        if node:
            elements.append(node.data)
            self._preorder_recursive(node.left, elements)
            self._preorder_recursive(node.right, elements)

    # --- Otras Funcionalidades ---

    def get_size(self):
        """Retorna el número total de nodos."""
        return self._get_size_recursive(self.root)

    def _get_size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._get_size_recursive(node.left) + self._get_size_recursive(node.right)

    def find_min(self):
        """Encuentra el valor mínimo (el más a la izquierda). O(log n) garantizado."""
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        """Encuentra el valor máximo (el más a la derecha). O(log n) garantizado."""
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def visualize(self):
        """Función de ayuda simple para visualizar la estructura (solo in-order y altura/balance)."""
        print("In-order:", self.inorder_traversal())
        print("Pre-order:", self.preorder_traversal())
        print("Raíz:", self.root.data if self.root else None)
        print("Altura del árbol:", self.get_height(self.root))
        print("Balance de la raíz:", self.get_balance_factor(self.root) if self.root else 0)
        # Una visualización completa de la estructura requiere más código (ej. imprimir por niveles con indentación)
        # Esto es solo para dar una idea rápida.
