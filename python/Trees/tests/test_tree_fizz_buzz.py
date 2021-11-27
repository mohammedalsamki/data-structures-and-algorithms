import pytest

from trees.tree_fizz_buzz import fizz_buzz_tree,traverse_breadth_first
from trees.k_ary import KAryTree
from trees.node import Node

def test_fizz_buzz_tree_happy(k_ary_tree):
    new_k_ary_tree = fizz_buzz_tree(k_ary_tree)
    assert new_k_ary_tree.root.value == 'Buzz'

def test_fizz_buzz_tree_raises_exception():
    k_ary_tree = KAryTree()
    with pytest.raises(Exception):
        fizz_buzz_tree(k_ary_tree)

def test_fizz_buzz_tree_failur(k_ary_tree):
    new_k_ary_tree = fizz_buzz_tree(k_ary_tree)
    assert new_k_ary_tree.root.value != 'Fizz'

def test_fizz_buzz_tree_traverse_breadth_first(k_ary_tree):
    new_k_ary_tree = fizz_buzz_tree(k_ary_tree)
    assert ['Buzz', 'Fizz', '7', '8', 'FizzBuzz', 'Fizz', 'Buzz', 'Fizz', 'Buzz', 'Fizz', 'Buzz', 'Fizz', 'Buzz', '13', '2', '13', '2'] == traverse_breadth_first(new_k_ary_tree)


@pytest.fixture
def k_ary_tree():
    k_ary_tree = KAryTree()
    k_ary_tree.root = Node(5)
    k_ary_tree.root.children.append(Node(3))
    k_ary_tree.root.children.append(Node(7))
    k_ary_tree.root.children.append(Node(8))
    k_ary_tree.root.children.append(Node(15))
    for child in k_ary_tree.root.children:
        child.children.append(Node(9))
        child.children.append(Node(5))

    for child in k_ary_tree.root.children[0].children:
        child.children.append(Node(13))
        child.children.append(Node(2))
    return k_ary_tree
