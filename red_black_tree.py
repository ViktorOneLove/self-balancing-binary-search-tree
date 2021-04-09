from enum import Enum


class Color(Enum):
    RED = 0,
    BLACK = 1


class Node:
    def __init__(self, val):
        self.val = val
        self.color = Color.RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """
                    X's GrandFather
                 /                \
               /                   \
            X's Uncle            X's Father
                                 /       \
                                /         \
                            X's Sibling    X
    """
    def __init__(self):
        self._root = None

    def search(self, val):
        """
        Search for value

        :param val: value to search
        :return: associative node
        """
        cur_node = self._root
        while cur_node is not None and cur_node.val != val:
            if val < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return cur_node

    def insert(self, val):
        """
        Insert node in tree

        :param val: node to insert
        """
        node_to_insert = Node(val)
        inserted_node = self._bst_insert(node_to_insert)
        self._fix_tree(inserted_node)

    def _bst_insert(self, node):
        """
        Simply insert node like BST algorithm

        :param node: node to insert
        """
        if self._root is None:
            self._root = node
            return self._root

        cur_node = self._root
        while cur_node is not None:
            parent = cur_node
            if node.val == cur_node.val:
                return cur_node
            elif node.val < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        node.parent = parent
        if node.val < parent.val:
            parent.left = node
        else:
            parent.right = node
        return node

    def _fix_tree(self, node):
        """
        Fix tree, make it match invariants of red-black tree

        :param node: node from which start fix
        """
        while node is not self._root and node.color != Color.BLACK \
                and node.parent.color == Color.RED:
            parent = node.parent
            grand_parent = node.parent.parent

            if parent is grand_parent.left:
                uncle = grand_parent.right
                # The uncle of node is also red
                # Only recoloring required
                if uncle is not None and uncle.color == Color.RED:
                    grand_parent.color = Color.RED
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent
                else:
                    # node is right child of its parent
                    # left-rotation required
                    if node is parent.right:
                        self._left_rotation(parent)
                        node = parent
                        parent = node.parent
                    # Case : 3
                    # node is left child of its parent
                    # right-rotation required
                    else:
                        self._right_rotation(grand_parent)
                        parent.color, grand_parent.color = grand_parent.color, parent.color
                        node = parent

            else:
                uncle = grand_parent.left
                # The uncle of node is also red
                # Only recoloring required
                if uncle is not None and uncle.color == Color.RED:
                    grand_parent.color = Color.RED
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent
                else:
                    # node is left child of its parent
                    # right-rotation required
                    if node is parent.left:
                        self._right_rotation(parent)
                        node = parent
                        parent = node.parent
                    # node is right child of its parent
                    # left-rotation required
                    else:
                        self._left_rotation(grand_parent)
                        parent.color, grand_parent.color = grand_parent.color, parent.color
                        node = parent

        self._root.color = Color.BLACK

    def _left_rotation(self, node):
        if node is None or node.right is None:
            return

        right_sub_node = node.right
        node.right = right_sub_node.left
        if node.right is not None:
            node.right.parent = node

        right_sub_node.parent = node.parent

        if node.parent is None:
            self._root = right_sub_node
        elif node.parent.left is node:
            node.parent.left = right_sub_node
        else:
            node.parent.right = right_sub_node

        right_sub_node.left = node
        node.parent = right_sub_node

    def _right_rotation(self, node):
        if node is None or node.left is None:
            return

        left_sub_node = node.left
        node.left = left_sub_node.right
        if node.left is not None:
            node.left.parent = node

        left_sub_node.parent = node.parent

        if node.parent is None:
            self._root = left_sub_node
        elif node.parent.left is node:
            node.parent.left = left_sub_node
        else:
            node.parent.right = left_sub_node

        left_sub_node.right = node
        node.parent = left_sub_node

    def travers_tree(self, mode):
        """
        Traverse tree in chosen mode

        :param mode:
            Type of traversing:
            LNR — in order
            NLR — pre-order
            LRN — post order
        :return:
            List of values in nodes
        """
        list_of_nodes = []
        if mode == "LNR":
            self._in_order_helper(self._root, list_of_nodes)
        elif mode == "NLR":
            self._pre_order_helper(self._root, list_of_nodes)
        elif mode == "LRN":
            self._post_order_helper(self._root, list_of_nodes)
        return list_of_nodes


    def _in_order_helper(self, node, list_of_nodes):
        if node is not None:
            self._in_order_helper(node.left, list_of_nodes)
            list_of_nodes.append(node.val)
            self._in_order_helper(node.right, list_of_nodes)

    def _pre_order_helper(self, node, list_of_nodes):
        if node is not None:
            list_of_nodes.append(node.val)
            self._pre_order_helper(node.left, list_of_nodes)
            self._pre_order_helper(node.right, list_of_nodes)

    def _post_order_helper(self, node, list_of_nodes):
        if node is not None:
            self._post_order_helper(node.left, list_of_nodes)
            self._post_order_helper(node.right, list_of_nodes)
            list_of_nodes.append(node.val)
