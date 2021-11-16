from stack_queue_brackets import __version__


def test_version():
    assert __version__ == '0.1.0'

from stack_queue_brackets.stack_balanced_parens import is_paren_balanced

def test_case_1():
    assert is_paren_balanced("{}") == True

def test_case_2():
    assert is_paren_balanced("{}(){}") == True

def test_case_3():
    assert is_paren_balanced("()[[]]") == True

def test_case_4():
    assert is_paren_balanced("(){}[[]]") == True

def test_case_5():
    assert is_paren_balanced("(](") == False

def test_case_6():
    assert is_paren_balanced("{(})") == False
