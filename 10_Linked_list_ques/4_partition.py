
from LinkedList import LinkedList

def partition(ll, x):
    currNode = ll.head
    ll.tail = currNode

    while currNode:                                                      #Time O(n)
        nextNode = currNode.next                                         #Space O(1)
        currNode.next = None

        if currNode.value < x:        
            currNode.next = ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None

LL = LinkedList()
LL.generate(10 ,0 ,99)
print(LL)
partition(LL, 50)
print(LL)
