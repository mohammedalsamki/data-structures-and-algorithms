from linked_list_insertions import __version__

from linked_list_insertions.linked_list_insertions import Node,Linked_list

import pytest

def test_version():
    assert __version__ == '0.1.0'

# Can successfully instantiate an empty linked list
def test_empty_list():
    link_list=Linked_list()
    expected = None
    actual= link_list.head
    assert actual == expected

# Can properly insert into the linked list
def test_insert():
    link_list=Linked_list()
    link_list.insert_at_begining(50)
    expected="{ 50 } -> NULL"
    actual=link_list.__str__()
    assert actual== expected

# The head property will properly point to the first node in the linked list
def test_head(linkedlist):
    expected="hi"
    actual=linkedlist.head.value
    assert expected==actual


# Can properly insert multiple nodes into the linked list
def test_insert_4_nodes(linkedlist):
    expected="{ hi } -> { 70 } -> { 50 } -> NULL"
    actual=linkedlist.__str__()
    assert actual== expected

# Will return true when finding a value within the linked list that exists
def test_is_include_50(linkedlist):
    expected=True
    actual=linkedlist.is_include(50)
    assert actual== expected

# Will return false when searching for a value in the linked list that does not exist
def test_is_include_6(linkedlist):
    expected=False
    actual=linkedlist.is_include(6)
    assert actual== expected

# Can properly return a collection of all the values that exist in the linked list
def test_prit_list(linkedlist):
    expected="{ hi } -> { 70 } -> { 50 } -> NULL"
    actual=linkedlist.__str__()
    assert actual== expected

# Can successfully add a node to the end of the linked list
def test_append(linkedlist):
    linkedlist.append(4)
    expected = "{ hi } -> { 70 } -> { 50 } -> { 4 } -> NULL"
    actual = linkedlist.__str__()
    assert expected == actual

# Can successfully add multiple nodes to the end of a linked list
def test_append_2_nodes(linkedlist):
    linkedlist.append(4)
    linkedlist.append(10)
    expected = "{ hi } -> { 70 } -> { 50 } -> { 4 } -> { 10 } -> NULL"
    actual = linkedlist.__str__()
    assert expected == actual
# Can successfully insert a node before a node located i the middle of a linked list
def test_insert_befor_node(linkedlist):
    linkedlist.insert_before(50,"welcome")
    expected = "{ hi } -> { 70 } -> { welcome } -> { 50 } -> NULL"
    actual = linkedlist.__str__()
    assert expected == actual

# Can successfully insert a node before the first node of a linked list
def test_insert_befor_first_node(linkedlist):
    linkedlist.insert_before("hi",50)
    expected = "{ 50 } -> { hi } -> { 70 } -> { 50 } -> NULL"
    actual = linkedlist.__str__()
    assert expected == actual

# Can successfully insert after a node in the middle of the linked list
def test_insert_after_node(linkedlist):
    linkedlist.insert_after('hi',"welcome")
    expected = "{ hi } -> { welcome } -> { 70 } -> { 50 } -> NULL"
    actual = linkedlist.__str__()
    assert expected == actual

# Can successfully insert a node after the last node of the linked list
def test_insert_after_last_node(linkedlist):
    linkedlist.insert_after(50,"welcome")
    expected = "{ hi } -> { 70 } -> { 50 } -> { welcome } -> NULL"
    actual = linkedlist.__str__()
    assert expected == actual

@pytest.fixture
def linkedlist():
    link_list=Linked_list()
    link_list.insert_at_begining(50)
    link_list.insert_at_begining(70)
    link_list.insert_at_begining('hi')
    return link_list


# Where k is greater than the length of the linked list
def test_k_greater_than__the_length(linkedlist):
    length=2
    expected = 'you enter a number biggest than length of the liked-list'
    actual = linkedlist.kFromEnd(5)
    assert expected == actual

# Where k and the length of the list are the same
def test_k_same_with_the_length(linkedlist):
    lenght=2
    expected = f'you have to enter a number between 0 and 3'
    actual = linkedlist.kFromEnd(3)
    assert expected == actual

# Where k is not a positive integer
def test_k_is_the_negative(linkedlist):
    lenght=3
    expected = 'you entered a negative index'
    actual = linkedlist.kFromEnd(-1)
    assert expected == actual

# Where the linked list is of a size 1
def test_list_of_the_one_node():
    test=Linked_list()
    test.append(7)
    expected = 7
    actual = test.kFromEnd(0)
    assert expected == actual

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_kth_the_index(linkedlist):
    lenght=3
    expected = 70
    actual = linkedlist.kFromEnd(1)
    assert expected == actual

@pytest.fixture
def linkedlist():
    test = Linked_list()
    test.insert_at_begining(50)
    test.insert_at_begining(70)
    test.insert_at_begining('hi')
    return test
