#3 traversal in single linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #insert in linkedlist
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
                
            else:
                tempNode = self.head
                index = 0
                while(index < location - 1):
                    tempNode = tempNode.next            #Time O(n)
                    index += 1                          #Space O(1)
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSLL(self):
        if self.head is None:
            print("SLL doesn't exist")
        else:
            node = self.head
            while node is not None:         #Time O(n)
                print(node.value)           #Space O(1)
                node  = node.next

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 0)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(6, 1)


print([node.value for node in singlyLinkedList])

print(singlyLinkedList.traverseSLL())

            
