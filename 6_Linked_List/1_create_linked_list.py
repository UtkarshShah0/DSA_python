#1 creation of single linked list

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

singlyLinkedList = SlinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2
