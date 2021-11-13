from stack_and_queue.stack import EmptyStack,Stack
import pytest
def test_push(stack):
    actual=stack.top.value
    excepted="34"
