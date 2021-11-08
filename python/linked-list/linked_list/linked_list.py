class Node():
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_list():
    count =0
    def __init__(self):
        self.head=None

    def append(self, value):

        node = Node(value)
        Linked_list.count+=1
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insert_at_beginning(self, value):


        node =Node(value)
        Linked_list.count+=1
        if self.head == None:
            self.head = node
        else:
            node.next=self.head
            self.head=node

    def is_include(self,lookforValu):


        current=self.head
        while current:
            if current.value == lookforValu:
                return True

            current=current.next
        return False

    def insert_before(self,value,newvalue):

        newNode=Node(newvalue)
        current=self.head

        if current is not None:

            while current.next is not None:
                if current.value == value:
                    print('in if state val ',current.value)
                    newNode.next=self.head
                    self.head=newNode
                    break
                if current.next.value == value:
                    print('in while loop val ',current.value)
                    newNode.next = current.next
                    current.next = newNode
                    break

                else:
                    current = current.next

    def insert_after(self, value, newvalue):

        newNode= Node(newvalue)
        current=self.head

        if current is not None:

            while current.next is not None:
                if current.value == value:
                    newNode.next= current.next
                    current.next = newNode
                    break
                else:
                    current =current.next

            if current.next == None:
                current.next = newNode




    def __str__(self):

        result = ""
        if self.head is None:
            result = "empty linked list"
        else:
            current = self.head
            while current:
                result += "{ "+f"{current.value}"+" } -> "
                current = current.next
        result += "NULL"
        return result


if __name__ == "__main__":
     test = Linked_list()
     test.insert_at_beginning(500)
     test.insert_at_beginning(700)
     test.insert_at_beginning(20)
     test.insert_at_beginning(60)
     test.insert_before(700,100)
     test.insert_before(700,30)
     test.insert_after(500,750)
     test.insert_after(20,99)

     print(test)

