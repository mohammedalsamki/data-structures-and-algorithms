from collections import deque

from trees.k_ary import KAryTree

from trees.node import Node

def fizz_buzz_converter(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"

    return str(value)

def fizz_buzz_tree(k_ary_tree):
    if not k_ary_tree.root:
        raise Exception("k-ary tree is empty")
    new_k_ary_tree = KAryTree()

    queue_original = deque()
    queue_new = deque()

    queue_original.append(k_ary_tree.root)

    new_k_ary_tree.root = Node(fizz_buzz_converter(k_ary_tree.root.value))
    queue_new.append(new_k_ary_tree.root)

    while queue_original:
        current_original = queue_original.popleft()
        current_new = queue_new.popleft()

        for idx, child in enumerate(current_original.children):
             queue_original.append(child)
             current_new.children.append(Node(fizz_buzz_converter(child.value)))
             queue_new.append(current_new.children[idx])

    return new_k_ary_tree


def traverse_breadth_first(k_ary_tree):
    if not k_ary_tree.root:
        raise Exception("k-ary tree is empty")
    k_ary_tree_values = []

    queue = deque()

    queue.append(k_ary_tree.root)

    while queue:
        current = queue.popleft()
        k_ary_tree_values.append(current.value)

        for  child in current.children:
             queue.append(child)


    return k_ary_tree_values



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
if __name__ == "__main__":
    k_ary_tree = k_ary_tree()
    print(traverse_breadth_first(k_ary_tree))
    fizz_buzz_tree = fizz_buzz_tree(k_ary_tree)
    print (traverse_breadth_first(fizz_buzz_tree))
