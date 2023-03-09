#1 creation of double ll
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #1 Creation of double linked list
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.prev = None                                        #Time O(1)
        self.head = node                                        #Space O(1
        )
        self.tail = node
        return "Double LL created successfully"

    

doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])
        
            
