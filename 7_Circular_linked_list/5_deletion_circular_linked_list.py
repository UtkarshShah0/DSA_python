#5 Deletion in Circular Linked List

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
        print("The CSLL has been created. ")



    # Insertion in Circulat Linked List
    def insertCSLL(self, value, location):
        if self.head is None:
            print("CSLL doesn't exist")
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
            print("The node has been successfully added")



    # Traversal in circular Singly Linked List
    def traversalCSLL(self):
        if self.head is None:
            print("CSLL doesn't exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)                       #Time O(n)
                tempNode = tempNode.next                    #Space O(1)
                if tempNode.next == self.tail.next:
                    break

    # Searching Circular Singly Linked List
    def searchCSLL(self, nodeValue):
        if self.head is None:
            print("CSLL does't exist")
        else:
            tempNode = self.head
            index = 0
            while tempNode:                                     #Time O(n)
                if tempNode.value == nodeValue:                 #Space O(1)
                    print("value = ",nodeValue,"index = ",index)
                    break
                tempNode = tempNode.next
                index += 1
                if tempNode == self.tail.next:
                    print("value doesn't exist ")
                    break



    # Deletion of a node of Circular Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node in CSLL.")
        else:
            if(location == 0):
                node=self.head
                if self.head == self.tail:
                    node.next = None  #first remove next
                    self.head = None 
                    self.tail = None
                else:
                    nextNode = node.next
                    self.head = nextNode
                    self.tail.next = nextNode

            elif location == 1:  #last
                node=self.head
                if self.head == self.tail:
                    node.next = None
                    self.head = None
                    self.tail = None

                else:
                    node = self.head
                    while node:
                        if(node.next == self.tail):
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = nextNode.next
                    
                  
    
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(0)

circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(4,1)

#circularSLL.traversalCSLL()
#circularSLL.searchCSLL(6)
#circularSLL.searchCSLL(10)

print([node.value for node in circularSLL])

circularSLL.deleteNode(2)
print([node.value for node in circularSLL])
