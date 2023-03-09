
from LinkedList import LinkedList

def sumList(L1, L2):
    n1 = L1.head
    n2 = L2.head
    Carry = 0
    ll = LinkedList()
    Sum = 0 
    
    while n1 or n2:                                                 
        Sum = Carry
        
        if n1:
            Sum += n1.value                                         #Time O(n)
            n1 = n1.next                                            #Space O(n)
        if n2:
            Sum += n2.value
            n2 = n2.next
            
        ll.add(int(Sum%10))
        Carry = Sum//10

    return ll

a = LinkedList()
a.generate(3 ,0 ,9)
print(a)

b = LinkedList()
b.generate(4 ,0 ,9)
print(b)


print(sumList(a,b))
        
