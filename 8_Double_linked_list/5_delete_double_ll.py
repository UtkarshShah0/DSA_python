#5 delete node in double ll
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
        if self.head is None:
            print("Double LL doesn't exist")
        else:
            tempNode= self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev


    #5 Searching in double linked list
    def searchDLL(self, search):
        if self.head is None:
            print("Double LL doesn't exist")
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if(tempNode.value == search):
                    print("value = ",tempNode.value, "Location =", index)
                    break
                tempNode = tempNode.next
                index += 1
            print("Element doesn't exist")

    #6 Deletion in double linked list
    def deleteNode(self, location):
        if self.head is None:
            print("Double LL doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
                    
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            else:
                tempNode = self.head
                index = 0
                
                while index < location -1:
                    tempNode = tempNode.next                  #Time O(n)
                    index += 1                                #Space O(1)
                currNode = tempNode.next
                nextNode = currNode.next
                tempNode.next = nextNode
                nextNode.prev = tempNode
                
        

doublyLL = DoublyLinkedList()
doublyLL.createDLL(0)

print([node.value for node in doublyLL])

#doublyLL.insertNode(0,0)
doublyLL.insertNode(1,1)
doublyLL.insertNode(2,1)
doublyLL.insertNode(3,1)
doublyLL.insertNode(4,1)
doublyLL.insertNode(5,1)

print([node.value for node in doublyLL])

#doublyLL.traverseDLL()
#oublyLL.reverseTraversal()

#doublyLL.searchDLL(99)
#doublyLL.deleteNode(0)
#doublyLL.deleteNode(1)
doublyLL.deleteNode(3)

print([node.value for node in doublyLL])


print([node.value for node in doublyLL])
