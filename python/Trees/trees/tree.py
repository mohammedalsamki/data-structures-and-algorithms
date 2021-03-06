
class Node:
    """
    Binary Tree Node
    """
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.data = value

    def __str__(self):
        return '%s' % self.data


class Tree(Node):
    """

    """
    def __init__(self):
        self.root = None


    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items ordered by pre-order algorithm

        sub method : walk () to make the recursion staff
        """
        list_of_items = []
        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items
    def in_order(self):
        """
        A binary tree method which returns a list of items in post order

        input: None

        output: tree items ordered by in order algorithm
        """
        list_of_items = []
        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.data)
                if node.right:
                    walk(node.right)
        walk(self.root)
        return list_of_items
    def post_order(self):
        """
        A binary tree method which returns a list of items in post order

        input: None

        output: tree items ordered by post order algorithm
        """
        list_of_items = []
        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
                list_of_items.append(node.data)

        walk(self.root)
        return list_of_items


class BTree(Tree):

    def add(self,data):
        """
        adds a new node of given value in the correct location
        in the binary search tree.

        Each element in a binary tree can have only two children.

        A node???s left child must have a value less than its parent???s value,
        A node???s right child must have a value greater than its parent value.

        Args:
        value ([any]): the value of the new node to add

        """

        def btree(root):

            if not root:
                self.root = Node(data)
                return
            if root.data < data:
                if not root.left:
                    root.left = Node(data)
                else:
                    btree(root.left)
            else:

                if not root.right:
                    root.right = Node(data)
                else:
                    btree(root.right)

        btree(self.root)

    def contains(self,value):
        """
        method to return boolean indicating weather or not the value
        given is in the tree at least once.

        Args:
            value (any): node data
        """
        items = self.in_order()

        if len(items) == 0 :
            exception('No items in the tree')


        return True if value in items else False

    def get_max(self):
        """
        method to returns the maximum value in a Binary search tree

        """
        if not self.root :exception('No items in the tree')
        self.max_value = 0
        def walk(node):
            if node:
                if node.left:
                    walk(node.left)

                if node.data > self.max_value:
                        self.max_value = node.data

                if node.right:
                    walk(node.right)

        walk(self.root)

        return self.max_value






def exception(reason):
    raise Exception(reason)

