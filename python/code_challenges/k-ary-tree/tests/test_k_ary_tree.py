from k_ary_tree import __version__

from k_ary_tree.k_ary_tree import  binarysearchtree



# def test_version():
#     assert __version__ == '0.1.0'



# first test "successfully instantiate an empty tree"
def test_empty_tree():
    tree = binarysearchtree()
    actual = tree.root
    expected = None
    assert actual == expected

# second test "successfully instantiate a tree with a single root node"
def test_single_root_node():
    test = binarysearchtree()
    test.add(1)
    test.add(2)
    test.add(3)
    test.add(4)
    actual = test.root.value
    expected = 1
    assert actual == expected

# third test "successfully add a left child and right child to a single root node"
def test_left_and_right_single_root_node():
    test = binarysearchtree()
    test.add(10)
    test.add(2)
    test.add(30)
    actual = (test.root.left.value, test.root.right.value)
    expected = (2,30)
    assert actual == expected

# fourth test "successfully return a collection from an inorder traversal"
def test_inorder_traversal():
    test = binarysearchtree()
    test.add(1)
    test.add(5)
    test.add(2)
    test.add(7)
    test.add(11)
    test.add(3)
    actual = test.inorder()
    expected = [1, 2, 3, 5, 7, 11]
    assert actual == expected

# fifth test "successfully return a collection from a preorder traversal"
def test_preorder_traversal():
    test = binarysearchtree()
    test.add(1)
    test.add(5)
    test.add(2)
    test.add(7)
    test.add(11)
    test.add(3)
    actual = test.preorder()
    expected = [1, 5, 2, 3, 7, 11]
    assert actual == expected

# sixth test "successfully return a collection from a postorder traversal"
def test_postorder_traversal():
    test = binarysearchtree()
    test.add(1)
    test.add(5)
    test.add(2)
    test.add(7)
    test.add(11)
    test.add(3)
    actual = test.postorder()
    expected = [3, 2, 11, 7, 5, 1]
    assert actual == expected

# extra test "successfully return the value "dose not exist" in the tree "
def test_value_dne():
    test = binarysearchtree()
    test.add(1)
    test.add(5)
    test.add(2)
    test.add(7)
    test.add(11)
    test.add(3)
    actual = test.Contains(4)
    expected = "dose not exist"
    assert actual == expected

# extra test "successfully return if the valeu exist in the tree "
def test_value_exist():
    test = binarysearchtree()
    test.add(1)
    test.add(5)
    test.add(2)
    test.add(7)
    test.add(11)
    test.add(3)
    actual = test.Contains(11)
    expected = "the value is exist"
    assert actual == expected
