class Node():

    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list():
    counting =0

    def __init__(self):
        self.head=None


    def kFromEnd(self,k):
        """
        """
        count = 0
        current =self.head
        while current:
            current = current.next
            count = count + 1
        k+=1
        if count==1:
            return self.head.value
        else:
            while k>0 and k<count:
                if count>= k :
                    current = self.head
                    for i in range(count - k ):
                        current =current.next
                    return current.value
            if k<=0:
                return 'you entered a negative index'
            if k-1 == count:
                return f'you have to enter a number between 0 and {count}'
            if k>count:
                return 'you enter a number biggest than length of the liked-list'

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

    def zipLists(self, list1, list2):
        current1 = list1.head
        current2 = list2.head

        while current1 != None and current2 != None:

            save_curr1_next = current1.next
            save_curr2_next = current2.next


            current1.next = current2
            current2.next= save_curr1_next


            current1 = save_curr1_next
            current2 = save_curr2_next


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
    test2=Linked_list()

    test.insert_at_begining(300)
    test.insert_at_begining(50)
    test.insert_at_begining(20)
    test.insert_at_begining(10)

    test.insert_before(50,70)
    test.insert_before(50,30)

    test.insert_after(300,500)
    test.insert_after(10,120)

    print(test.kFromEnd(3))
    print("========================")

    print(test)
    print("========================")

    print(test2)

    test.zipLists(test,test2)




