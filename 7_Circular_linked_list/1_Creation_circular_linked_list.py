#1 Creation of Circular Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Creation of circular Singly Linked List
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)                                  #Time O(1)
        node.next = node                                        #Space O(1)
        self.head = node
        self.tail = node
        return "The CSLL has been created. "
        
    
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)



print([node.value for node in circularSLL])
