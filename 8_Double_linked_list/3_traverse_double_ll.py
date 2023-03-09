#3 traversal of double ll
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
        self.head = node                                        #Space O(1)
        self.tail = node
        return "Double LL created successfully"

    #2 Insertion of double linked list
    def insertNode(self, nodeValue, location):
        if self.head is None:
            return "Double LL doesn't exist "
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif location == 1:
                newNode.next = None
                self.tail.next = newNode                        #Time O(n)
                newNode.prev = self.tail                        #Space O(1)
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                nextNode.prev = newNode

                
    #3 Traversal in double linked list           
    def traverseDLL(self):
        if self.head is None:
            print("Double LL doesn't exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    #4 Reverse Traveral in double linked list
    def reverseTraversal(self):
        if self.tail is None:
            print("Double LL doesn't exist")
        else:
            tempNode= self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev



doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])

doublyLL.insertNode(0,0)
doublyLL.insertNode(2,1)
doublyLL.insertNode(4,2)

print([node.value for node in doublyLL])

doublyLL.traverseDLL()
doublyLL.reverseTraversal()
