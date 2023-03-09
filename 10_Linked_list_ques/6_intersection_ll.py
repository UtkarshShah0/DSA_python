
from LinkedList import LinkedList, Node

def intsec(L1, L2):
    if L1.tail is not L2.tail:
        return False

    lenA = len(L1)                         #O(A)                     # Time O(A+B)
    lenB = len(L2)                         #O(B)                     # Space O(1)

    shorter = L1 if lenA < lenB else L2
    longer = L2 if lenA < lenB else L1

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

# Helper Addition Method
def addSameNode(L1, L2, value):
    tempNode = Node(value)
    L1.tail.next = tempNode
    L1.tail = tempNode
    L2.tail.next = tempNode
    L2.tail = tempNode


L1 = LinkedList()
L1.generate(3, 0, 10)

L2 = LinkedList()
L2.generate(4, 0, 10)

addSameNode(L1, L2, 11)
addSameNode(L1, L2, 14)

print(L1)
print(L2)

print(intsec(L1, L2))
