import random
import pytest
from red_black_tree import RedBlackTree
from red_black_tree import Color


class TestRedBlackTreeInsert:
    """
    -------------------------------------INSERT TESTS-------------------------------------
    """

    def test_insert_in_empty_tree(self):
        """
        Insert in empty tree
        Successfully
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        assert red_black_tree._root.val == 5
        assert red_black_tree._root.color == Color.BLACK
        assert red_black_tree._root.left is None
        assert red_black_tree._root.right is None

    def test_insert_in_right_subtree(self):
        """
        Insert in right subtree
        Successfully
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        red_black_tree.insert(10)
        left_tree = red_black_tree.search(5)
        right_inserted_node = red_black_tree.search(10)
        assert right_inserted_node.parent is left_tree
        assert left_tree.right is right_inserted_node

    def test_insert_in_left_subtree(self):
        """
        Insert in left subtree
        Successfully
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        red_black_tree.insert(4)
        left_inserted_node = red_black_tree.search(4)
        right_tree = red_black_tree.search(5)
        assert left_inserted_node.parent is right_tree
        assert right_tree.left is left_inserted_node

    def test_insert_already_existing_value(self):
        """
        Insert already existing value
        Successfully
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        red_black_tree.insert(6)
        red_black_tree.insert(7)
        red_black_tree.insert(8)
        red_black_tree.insert(9)
        searching_elem = 9
        red_black_tree.insert(searching_elem)
        num_of_necessary_nodes = 0
        list_of_nodes = red_black_tree.travers_tree("LNR")
        for val in list_of_nodes:
            if val == searching_elem:
                num_of_necessary_nodes += 1
        assert num_of_necessary_nodes == 1

    def test_insert_p_red_u_red(self):
        """
        Insert
        Parent is red and Uncle is red
        Successfully

               61-B                         61-B
               /  \                         /  \
              /    \                       /    \
           52-B    85-B     -> + 100 ->  52-B   85-R
                   /   \                        /  \
                  /     \                      /    \
                76-R    93-R                76-B   93-B
                                                     \
                                                      \
                                                     100-R
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(61)
        red_black_tree.insert(52)
        red_black_tree.insert(85)
        red_black_tree.insert(76)
        red_black_tree.insert(93)
        red_black_tree.insert(100)
        node_61 = red_black_tree.search(61)
        node_52 = red_black_tree.search(52)
        node_85 = red_black_tree.search(85)
        node_76 = red_black_tree.search(76)
        node_93 = red_black_tree.search(93)
        node_100 = red_black_tree.search(100)
        assert node_100.color == Color.RED
        assert node_93.color == Color.BLACK
        assert node_76.color == Color.BLACK
        assert node_85.color == Color.RED
        assert node_52.color == Color.BLACK
        assert node_61.color == Color.BLACK

    def test_p_right_child_of_g_and_k_right_child_of_p(self):
        """
        Insert
        Parent is right child of grandParent ant inserted node
        is right child of parent
        Successfully

           61-B                         61-B
           /  \                         /  \
          /    \                       /    \
       52-B    85-B     -> + 100 ->  52-B   93-B
                   \                        /  \
                    \                      /    \
                   93-R                85-R   100-R
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(61)
        red_black_tree.insert(52)
        red_black_tree.insert(85)
        red_black_tree.insert(93)
        red_black_tree.insert(100)
        node_61 = red_black_tree.search(61)
        node_52 = red_black_tree.search(52)
        node_85 = red_black_tree.search(85)
        node_93 = red_black_tree.search(93)
        node_100 = red_black_tree.search(100)
        assert node_100.color == Color.RED
        assert node_93.color == Color.BLACK
        assert node_85.color == Color.RED
        assert node_52.color == Color.BLACK
        assert node_61.color == Color.BLACK

    def test_p_right_child_of_g_and_k_left_child_of_p(self):
        """
        Insert
        Parent is right child of grandParent ant inserted node
        is left child of parent
        Successfully

           61-B                         61-B
           /  \                         /  \
          /    \                       /    \
       52-B    85-B     -> + 87 ->   52-B   87-B
                   \                        /  \
                    \                      /    \
                   93-R                  85-R   93-R
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(61)
        red_black_tree.insert(52)
        red_black_tree.insert(85)
        red_black_tree.insert(93)
        red_black_tree.insert(87)
        node_61 = red_black_tree.search(61)
        node_52 = red_black_tree.search(52)
        node_85 = red_black_tree.search(85)
        node_93 = red_black_tree.search(93)
        node_87 = red_black_tree.search(87)
        assert node_93.color == Color.RED
        assert node_85.color == Color.RED
        assert node_87.color == Color.BLACK
        assert node_52.color == Color.BLACK
        assert node_61.color == Color.BLACK


class TestRedBlackTreeSearch:
    """
    -------------------------------------SEARCH TESTS-------------------------------------
    """

    def test_find_func_all_found(self):
        """
        Searching all inserted values
        Successfully
        """
        num_of_elements = 100
        possible_values = list(range(-100000, 100000))
        elements = [random.choice(possible_values) for _ in range(num_of_elements)]
        red_black_tree = RedBlackTree()
        for elem in elements:
            red_black_tree.insert(elem)
        random.shuffle(elements)
        for elem in elements:
            assert red_black_tree.search(elem).val == elem

    def test_find_func_search_for_not_existing(self):
        """
        Searching for not existing value
        Successfully
        """
        num_of_elements = 100
        possible_values = list(range(-100000, 100000))
        elements = [random.choice(possible_values) for _ in range(num_of_elements)]
        different_element = 100001
        red_black_tree = RedBlackTree()
        for elem in elements:
            red_black_tree.insert(elem)

        assert red_black_tree.search(different_element) is None


class TestRedBlackTreeLeftRotation:
    """
    -------------------------------------LEFT ROTATION TESTS-------------------------------------

             |                            |
            (x)                          (y)
            / \                        /    \
           /   \                      /      \
          a     (y)        ->        (x)      c
               /   \                /   \
              /     \              /     \
             b       c            a       b
    """

    def test_left_rotation_with_two_nodes(self):
        """
        Left rotation
        Only two nodes
        Successfully

             N                            N
             |                            |
            (5)                         (10)
            / \                        /    \
           /   \                      /      \
          N     (10)        ->       (5)      N
               /   \                /   \
              /     \              /     \
             N       N            N       N
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        red_black_tree.insert(10)
        node_to_rotate = red_black_tree.search(5)
        red_black_tree._left_rotation(node_to_rotate)
        new_left_node = red_black_tree.search(5)
        new_right_node = red_black_tree.search(10)
        assert new_right_node.parent is None
        assert new_right_node.right is None
        assert new_right_node.left is new_left_node
        assert new_left_node.parent is new_right_node
        assert new_left_node.right is None
        assert new_left_node.left is None

    def test_left_rotation_with_one_node(self):
        """
        Left rotation
        Only one node
        Successfully

             N                            N
             |                            |
            (5)          ->              (5)
            / \                        /    \
           /   \                      /      \
          N    (N)                   N       (N)
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        node_to_rotate = red_black_tree.search(5)
        red_black_tree._left_rotation(node_to_rotate)
        new_node = red_black_tree.search(5)
        assert new_node is node_to_rotate

    def test_left_rotation(self):
        """
        Left rotation
        All nodes(Common case)
        Successfully

             N                            N
             |                            |
            (5)                          (7)
            / \                        /    \
           /   \                      /      \
          4     (7)        ->       (5)       8
               /   \                /   \
              /     \              /     \
             6       8            4       6
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        red_black_tree.insert(4)
        red_black_tree.insert(7)
        red_black_tree.insert(6)
        red_black_tree.insert(8)
        node_to_rotate = red_black_tree.search(5)
        red_black_tree._left_rotation(node_to_rotate)
        new_left_node = red_black_tree.search(5)
        new_right_node = red_black_tree.search(7)
        assert new_right_node.parent is None
        assert new_right_node.right.val == 8
        assert new_right_node.right.parent is new_right_node
        assert new_right_node.left is new_left_node
        assert new_left_node.parent is new_right_node
        assert new_left_node.left.val == 4
        assert new_left_node.left.parent is new_left_node
        assert new_left_node.right.val == 6
        assert new_left_node.right.parent is new_left_node


class TestRedBlackTreeRightRotation:
    """
    -------------------------------------RIGHT ROTATION TESTS-------------------------------------

                 |                    |
                (y)                  (x)
                /  \                 / \
               /    \               /   \
             (x)     c      ->     a    (y)
             / \                        / \
            /   \                      /   \
           a     b                    b     c
    """

    def test_right_rotation_with_two_nodes(self):
        """
        Right rotation
        Only two nodes
        Successfully

                 N                    N
                 |                    |
                (10)                 (5)
                /  \                 / \
               /    \               /   \
             (5)     N      ->     N    (10)
             / \                        / \
            /   \                      /   \
           N     N                    N     N
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(10)
        red_black_tree.insert(5)
        node_to_rotate = red_black_tree.search(10)
        red_black_tree._right_rotation(node_to_rotate)
        new_left_node = red_black_tree.search(5)
        new_right_node = red_black_tree.search(10)
        assert new_right_node.parent is new_left_node
        assert new_right_node.right is None
        assert new_right_node.left is None
        assert new_left_node.parent is None
        assert new_left_node.right is new_right_node
        assert new_left_node.left is None

    def test_right_rotation_with_one_node(self):
        """
        Right rotation
        Only one node
        Successfully

             N                            N
             |                            |
            (5)           ->             (5)
            / \                        /    \
           /   \                      /      \
          (N)   N                   (N)       N
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(5)
        node_to_rotate = red_black_tree.search(5)
        red_black_tree._right_rotation(node_to_rotate)
        new_node = red_black_tree.search(5)
        assert new_node is node_to_rotate

    def test_right_rotation(self):
        """
        Right rotation
        All nodes(Common case)
        Successfully

                 N                    N
                 |                    |
                (8)                  (6)
                /  \                 / \
               /    \               /   \
             (6)     9      ->     4    (8)
             / \                        / \
            /   \                      /   \
           4     7                    7     9
        """
        red_black_tree = RedBlackTree()
        red_black_tree.insert(8)
        red_black_tree.insert(9)
        red_black_tree.insert(6)
        red_black_tree.insert(4)
        red_black_tree.insert(7)
        node_to_rotate = red_black_tree.search(8)
        red_black_tree._right_rotation(node_to_rotate)
        new_left_node = red_black_tree.search(6)
        new_right_node = red_black_tree.search(8)
        assert new_right_node.parent is new_left_node
        assert new_right_node.right.val == 9
        assert new_right_node.right.parent is new_right_node
        assert new_right_node.left.val == 7
        assert new_right_node.left.parent is new_right_node
        assert new_left_node.left.val == 4
        assert new_left_node.left.parent is new_left_node
        assert new_left_node.right is new_right_node


class TestRedBlackTreeTravers:
    """
    -------------------------------------TRAVERS TESTS-------------------------------------
    """
    @pytest.fixture()
    def create_tree(self):
        red_black_tree = RedBlackTree()
        red_black_tree.insert(14)
        red_black_tree.insert(35)
        red_black_tree.insert(10)
        red_black_tree.insert(19)
        red_black_tree.insert(31)
        red_black_tree.insert(42)
        return red_black_tree

    @pytest.mark.parametrize("traversal_mode, right_order", [
        # in-order
        ("LNR", [10, 14, 19, 31, 35, 42]),
        # pre-order
        ("NLR", [14, 10, 31, 19, 35, 42]),
        # post-order
        ("LRN", [10, 19, 42, 35, 31, 14]),
        # wrong argument
        ("Smth wrong", [])
    ])
    def test_traversal(self, traversal_mode, right_order, create_tree):
        red_black_tree = create_tree
        assert red_black_tree.travers_tree(traversal_mode) == right_order
