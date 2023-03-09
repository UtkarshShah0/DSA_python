
from LinkedList import LinkedList

# Method 1
def removeDups(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        a=set([currNode.value])
        while currNode.next:
            nextNode = currNode.next                    #Time O(n)
            if nextNode.value in a:                     #Space O(n)
                currNode.next = nextNode.next
            else:
                a.add(nextNode.value)
                currNode = currNode.next
        return ll
    
# Method 2
def removeDups1(ll):
    if ll.head is None:
        return

    currNode = ll.head
    while currNode:                                     #Time O(n**2)
        runner = currNode
        while runner.next:
            if runner.next.value == currNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currNode = currNode.next
    return ll




LL = LinkedList()
LL.generate(10 ,0 ,5)
print(LL)
removeDups(LL)
print(LL)
