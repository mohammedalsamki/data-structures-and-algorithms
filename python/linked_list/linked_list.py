class Node:
    '''
    A class representing a Node

    '''

    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class Linjedlist:
    """
    A class for creating instances of a Linked List.
    """
    def __init__(self):
        self.head=None


    def insrt(self,value):
        """
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down
        """
        self.head=Node(value,self.head)

    def icludes (self,value):
        """
        """
        ele=self.head
        while ele :
            if ele.data==value:
                return True
            elif ele.next is not None:
                ele=ele.next
            else:
                return False


    def to_string(self):
        """
        """
        strin =""
        ele =self.head
        while ele:
            strin +="{ "+str(ele.data)+"}-> "
            ele=ele.next
            return strin


samki = Linjedlist()
samki.insrt(2)

samki.insrt(5)
samki.insrt(8)
print(samki.to_string())
print(samki)
print("for 2 ",samki.icludes(2))
print("for 5 ",samki.icludes(5))
print("for 7 ",samki.icludes(8))
