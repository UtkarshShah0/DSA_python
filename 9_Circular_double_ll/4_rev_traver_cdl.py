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

    
# 2 Insertion in circular DLL
    def insertCDLL(self, value, location):
        if self.head is None:
            return "CDLL doesn't exist"
        else:
            newNode = Node(value)
            
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode

                self.head = newNode

            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode

                self.tail = newNode

            else:
                tempNode = self.head
                index = 0

                while index < location -1:
                    tempNode = tempNode.next                        #Time O(n)
                    index += 1                                      #Space O(1)

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                nextNode.prev = newNode

            return "The node has been inserted"
        
# 3 Traversal in CDLL
    def traversalCDLL(self):
        if self.head is None:
            print("The cdll  doesn't exist")
        else:
            tempNode = self.head
            
            while tempNode:
                print(tempNode.value)                   #Time O(n)
                tempNode = tempNode.next                #Space O(1)
                if tempNode == self.tail.next:
                    break

# 4 Reverse Traversal in CDLL
    def reverseTraversalCDLL(self):
        if self.head is None:
            print("CDLL doesn't exist")
        else:
            tempNode = self.tail

            while tempNode:                             #Time O(n)
                print(tempNode.value)                   #Space O(1)
                tempNode = tempNode.prev
                if tempNode == self.head.prev:
                    break


    
circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(6,1)
circularDLL.insertCDLL(7,2)
print([node.value for node in circularDLL])

circularDLL.traversalCDLL()

circularDLL.reverseTraversalCDLL()
