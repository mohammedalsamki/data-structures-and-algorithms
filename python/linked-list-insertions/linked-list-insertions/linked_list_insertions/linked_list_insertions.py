class Node():

    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list():
    counting =0

    def __init__(self):
        self.head=None

    def append(self,value):

        node =Node(value)
        Linked_list.counting+=1
        if self.head is None:
            self.head =node
        else:
            current = self.head
            while current.next !=None:
                current = current.next
            current.next = node
    def insert_at_begining(self,value):
        """
        """
        node =Node(value)
        Linked_list.counting +=1
        if self.head == None:
            self.head = node
        else:
            node.next=self.head
            self.head=node

    def is_include(self,searchValue):
        current = self.head
        while current:
            if current.value == searchValue:
                return True
            current=current.next
        return False


    def insert_before(self,value,newValue):

        newNode=Node(newValue)
        current=self.head

        if current is not None:
            while current.next is not None:
                if current.value == value:
                    print('in the if state',current.value)
                    newNode.next=self.head
                    self.head=newNode
                    break
                if current.next.value == value:
                    print('in the while loop',current.value)
                    newNode.next=current.next
                    current.next = newNode
                    break
                else:
                    current = current.next


    def insert_after(self,value,newValue):
        newNode = Node(newValue)
        current=self.head

        if current is not None:
            while current.next is not None:
                if current.value==value:
                    newNode.next=current.next
                    current.next=newNode
                    break
                else:
                    current=current.next
            if current.next==None:
                current.next=newNode


    def __str__(self):

        result=""
        if self.head is None:
            result = "empty list"
        else:
            current = self.head
            while current:
                result +="{ "+f"{current.value}"+" } -> "
                current=current.next
        result+= "NULL"
        return result

if __name__=="__main__":

    test =Linked_list()

    test.insert_at_begining(300)
    test.insert_at_begining(50)
    test.insert_at_begining(20)
    test.insert_at_begining(10)

    test.insert_before(50,70)
    test.insert_before(50,30)

    test.insert_after(300,500)
    test.insert_after(10,120)

    print(test)





