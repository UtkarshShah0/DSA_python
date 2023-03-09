#2 Insertion in Circular Linked List

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
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created. "



    # Insertion in Circulat Linked List
    def insertCSLL(self, value, location):
        if self.head is None:
            return "CSLL doesn't exist"
        else:
            newNode = Node(value)
            # At Beginning
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            #At the End
            elif location == 1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode

            #At any specific location
            else:
                tempNode = self.head
                index = 0
                while index < location -1:                  #Time O(n)
                    tempNode = tempNode.next                #Space O(1)
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully added"
            
                  
    
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(4,1)
circularSLL.insertCSLL(6,3)



print([node.value for node in circularSLL])
