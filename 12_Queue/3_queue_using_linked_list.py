#Circular Queue using Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Queue:
    def __init__(self):                                                 #Time O(1)
        self.linkedList = LinkedList()                                  #Space O(1)

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)


    def enqueue(self, value):
        newNode = Node(value)
        
        if self.linkedList.head == None:
            self.linkedList.head = newNode                                      #Time O(1)
            self.linkedList.tail = newNode                                      #Space O(1)

        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode 


    def isEmpty(self):
        if self.linkedList.head == None:                                        #Time O(1)
            return True                                                         #Space O(1)
        else:
            return False


    def dequeue(self):
        if self.isEmpty():
            return "There is not any node"
        else:
            tempNode = self.linkedList.head                                 
            if self.linkedList.head == self.linkedList.tail :                    #Time O(1)
                self.linkedList.head = None                                      #Space O(1)     
                self.linkedList.tail = None

            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode


    def peek(self):
        if self.isEmpty():                                                      #Time O(1)
            return "There is no node"                                           #Space O(1)
        else:
            return self.linkedList.head
        

    def delete(self):       
        self.linkedList.head = None                                             #Time O(1) 
        self.linkedList.tail = None                                             #Space O(1)

    
        
        
            
a = Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
print(a)
print(a.dequeue())
print(a.peek())

