
from LinkedList import LinkedList

def n_to_kth_element(ll,n):
    node1 = ll.head
    node2 = ll.head
    
    for i in range(n-1):                        #O(n)
        if node2 is None:
            return None
        node2 = node2.next

    while node2.next:                #O(n)          #Time O(n)
        node1= node1.next                           #Space O(1)
        node2 = node2.next 

    return node1.value

LL = LinkedList()
LL.generate(10 ,0 ,5)
print(LL)
print(n_to_kth_element(LL, 3))
print(LL)
