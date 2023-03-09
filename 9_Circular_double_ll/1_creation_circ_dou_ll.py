# Circular double linked list

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

# 1 Creation of circular double ll
    def createCDLL(self, nodevalue):
        newNode = Node(nodevalue)
        
        self.head = newNode
        self.tail = newNode                                 #Time O(1)
        newNode.next = newNode                              #Space O(1)
        newNode.prev = newNode
        return "The CDLL is created successfully"
    
circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
print([node.value for node in circularDLL])
