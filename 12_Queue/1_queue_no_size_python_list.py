#Queue using python list no size

class Queue:
    def __init__(self):
        self.items=[]                                           #Time O(1)
                                                                #Space O(1)
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:                                    #Time O(1)
            return True                                         #Space O(1)
        else:
            return False
        

    def enqueue(self, value):
        self.items.append(value)                                #Time Amortized Worst Case O(n^2)
        return "The element inserted at end of queue"           #Space O(1)


    def dequeue(self):
        if self.isEmpty():                                      #Time O(n)
            return "There is no element in the array"           #Space O(1)
        else:
            return self.items.pop(0)


    def peek(self):
        if self.isEmpty():                                      #Time O(1)
            return "There is no element in the array"           #Space O(1)
        else:
            return self.items[0]

    def delete(self):                                           #Time O(1)
        self.items = None                                       #Space O(1)
        

a=Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
#print(a.dequeue())
print(a.peek())
a.delete()
