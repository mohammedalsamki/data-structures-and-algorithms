from stack_and_queue.stack import Stack
class Pseudo_Queue:
    def __init__(self,s):
        # stack1 hold data at first
        self.stack1 = Stack()
        # stack2 will be empty
        self.stack2 = Stack()
        self.stack1=s


    def enqueue(self, value):
        """
        this method use stack methods which is push and peek to implement enqueue method
        """
        result=''
        if self.stack1.is_empty():
            self.stack1.push(value)
        while not self.stack1.is_empty():

            if self.stack1.is_empty():
                break
            else:
                self.stack1.push(value)
                break

        while not self.stack1.is_empty():
            if self.stack1.tos.next != None:
                result+='['+str(self.stack1.peek())+']'+'->'
                self.stack1.tos = self.stack1.tos.next

            else:
               result+='['+str(self.stack1.peek())+']'
               break
            if self.stack1.is_empty():
                break

        return result

    def dequeue(self):
        """
        this method use stack methods which is pop and peek to implement dequeue method
        """
        while not self.stack1.is_empty():
            if self.stack1.is_empty():
                break
            else:
                self.stack2.push(self.stack1.pop())
        poped_value=self.stack2.pop()

        # to re-pack every thing inside stack1 in the right order after remove the first item from queue

        # while not self.stack2.is_empty():
        #     if self.stack2.is_empty():
        #         break
        #     else:
        #         self.stack1.push(self.stack2.pop())
        return poped_value


if __name__ == "__main__":
    stack= Stack()
    stack.push(20)
    stack.push(15)
    stack.push(10)
    pseudo_queue = Pseudo_Queue(stack)
    print('queue after add 5: ',pseudo_queue.enqueue(5))
    print('the removed value: ',pseudo_queue.dequeue())
