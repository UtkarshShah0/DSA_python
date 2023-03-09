#Circular Queue in Python with limited size

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]                           #Time O(1)
        self.maxSize = maxSize                                  #Space O(n)
        self.start = -1                                         #creating list of n size
        self.top = -1
        

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    

    def isFull(self):                                           #Time O(1)
        if self.top + 1== self.start:                           #Space O(1)
            return True
        elif self.start ==0 and self.top +1 == self.maxSize:
            return True
        else:
            return False
        

    def isEmpty(self):
        if self.top == -1:                                      #Time O(1)
            return True                                         #Space O(1)
        else:
            return False

        

    def enqueue(self, value):
        if self.isFull():                                       #Time O(1)
            return "The Circular Queue is Full"                 #Space O(1)
        else:
            if self.top + 1 == self.maxSize:
                self.top =0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

        

    def dequeue(self):
        if self.isEmpty():
            return "There is no element"
        else:
            firstElement = self.items[self.start]                          #Time O(1)
            start = self.start                                             #Space O(1)
            if self.start == self.top:
                self.start = -1
                self.top = -1
            if self.start +1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

        

    def peek(self):
        if self.isEmpty():                                                      #Time O(1)
            return "There is no element"                                        #Space O(1)
        else:
            return self.items[self.start]


    def delete(self):
        self.items = self.maxSize * [None]                                      #Time O(1)
        self.top = -1                                                           #Space O(1)
        self.start = -1



a = Queue(3)
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
print(a)
print(a.dequeue())
a.delete()
print(a)
