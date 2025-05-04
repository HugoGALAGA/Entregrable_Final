'''
AVL Tree
'''

import time  # Import the time module

class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1  # New: Height of the node, initialized to 1


    def __repr__(self):
        return '({})'.format(self.data)


class AVLTree:

    def __init__(self):
        self.root = None


    def traverse(self, subtree: Node):

        print(subtree)

        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left_child) - self._height(node.right_child)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left_child), self._height(node.right_child))

    def _rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child

        # Rotation
        y.left_child = z
        z.right_child = T2

        # Update heights
        self._update_height(z)
        self._update_height(y)

        return y  # New root after rotation

    def _rotate_right(self, z):
        y = z.left_child
        T3 = y.right_child

        # Rotation
        y.right_child = z
        z.left_child = T3

        # Update heights
        self._update_height(z)
        self._update_height(y)

        return y  # New root after rotation

    def _balance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1: # Left heavy
            if self._balance_factor(node.left_child) >= 0: # Left-Left case
                return self._rotate_right(node)
            else: # Left-Right case
                node.left_child = self._rotate_left(node.left_child)
                return self._rotate_right(node)

        if balance < -1: # Right heavy
            if self._balance_factor(node.right_child) <= 0: # Right-Right case
                return self._rotate_left(node)
            else: # Right-Left case
                node.right_child = self._rotate_right(node.right_child)
                return self._rotate_left(node)

        return node # No rotation needed


    def insert(self, value: int):

        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(value, self.root) # Root may change after balancing

    def _insert(self, value: int, subtree: Node):

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                subtree.left_child = self._insert(value, subtree.left_child)
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                subtree.right_child = self._insert(value, subtree.right_child)
        else:
            print('Value already exists in tree...')
            return subtree # No change if value exists

        return self._balance(subtree) # Balance the subtree and return the potentially new subtree root


    def search(self, key: int) -> bool:

        if self.root is None:
            return False
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:

        if key == subtree.data:
            return True
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)
        else:
            return False


    def find_min(self, subtree: Node) -> Node:

        while subtree.left_child is not None:
            subtree = subtree.left_child
        return subtree


    def find_max(self, subtree: Node) -> Node:

        while subtree.right_child is not None:
            subtree = subtree.right_child
        return subtree


    def print_pretty(self):
        if self.root is not None:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join(line.rstrip() for line in lines))
        else:
            print("\nEmpty tree...")


    def _build_tree_string(self, node: Node):
        if node.right_child is None and node.left_child is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right_child is None:
            lines, n, p, x = self._build_tree_string(node.left_child)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left_child is None:
            lines, n, p, x = self._build_tree_string(node.right_child)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left_child)
        right, m, q, y = self._build_tree_string(node.right_child)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def delete(self, value: int):
        """
        Deletes a node with the given value from the AVL Tree.
        """
        self.root = self._delete(value, self.root) # Root may change after balancing


    def _delete(self, value: int, subtree: Node) -> Node:
        """
        Recursive helper method to delete a node in AVL Tree and balance.
        """
        if not subtree:
            return subtree  # Value not found

        if value < subtree.data:
            subtree.left_child = self._delete(value, subtree.left_child)
        elif value > subtree.data:
            subtree.right_child = self._delete(value, subtree.right_child)
        else:  # Value found at subtree
            # Case 1: Leaf node or node with one child
            if not subtree.left_child:
                return subtree.right_child
            elif not subtree.right_child:
                return subtree.left_child
            # Case 2: Node with two children
            else:
                # Find in-order predecessor (max in left subtree)
                predecessor = self.find_max(subtree.left_child)
                subtree.data = predecessor.data  # Replace value
                # Delete the predecessor from the left subtree
                subtree.left_child = self._delete(predecessor.data, subtree.left_child)

        if not subtree: # Node might be deleted, so subtree can be None
            return subtree

        return self._balance(subtree) # Balance the subtree and return the potentially new subtree root


    def timed_search(self, key: int) -> tuple[bool, float]:
        """
        Searches for a key in the AVL Tree and measures the execution time.

        Args:
            key: The value to search for.

        Returns:
            A tuple containing:
            - A boolean indicating whether the key was found (True if found, False otherwise).
            - The time taken for the search in seconds (float).
        """
        start_time = time.perf_counter()
        found = self.search(key)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return found, elapsed_time