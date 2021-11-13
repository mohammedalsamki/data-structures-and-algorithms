from stack_and_queue.node import Node

class EmtyQueue(Exception):
    pass
class Queue:
    """
    """

    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        node=Node(value)

        if not self.rear:
            self.rear=node
            self.front=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        if self.front is None:
            raise EmtyQueue("this queue is empty")
        temp=self.front
        self.front=self.front.next
        temp.next=None
        return temp.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise EmtyQueue("this queue is empty")

    def is_empty(self):
        return self.front == None
