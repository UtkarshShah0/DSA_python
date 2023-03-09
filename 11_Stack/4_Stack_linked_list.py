# Stack using Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        tempNode  = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()          #Creating object of linkedlist(head)

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)


    def isEmpty(self):
        if self.LinkedList.head is None:                        #Time O(1)
            return True                                         #Space O(1)
        else:
            return False


    def push(self, value):                                      #Time O(1)
        node = Node(value)                                      #Space O(1)
        node.next = self.LinkedList.head
        self.LinkedList.head = node


    def pop(self):
        if self.isEmpty():
            return "LinkedList is Empty"                        #Time O(1)
        else:                                                   #Space O(1)
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue


    def peek(self):
        if self.isEmpty():                                      #Time O(1)
            return "LinkedList is Empty"                        #Space O(1)
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None

        
        
a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.pop()
print(a.peek())
print(a)
