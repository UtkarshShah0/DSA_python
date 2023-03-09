#3 Stack creation using List with limited size

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #push
    def push(self, value):
        if self.isFull():
            return "The Stack is Full"                                  #Time O(1)
        else:                                                           #Space O(1)
            self.list.append(value)
            return "The value has been inserted successfully"

    #pop
    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty"                                 #Time O(1)
        else:                                                           #Space O(1)
            return self.list.pop()
            
    #peek
    def peek(self):
        if self.isEmpty():                                          #Time O(1)
            return "There is not any element in Stack"              #Space O(1)
        else:
            return self.list[-1]

    #delete
    def delete(self):
        self.list = None


        

a = Stack(4)
print(a.isEmpty())
print(a.isFull())
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print(a.isFull())
print(a)

