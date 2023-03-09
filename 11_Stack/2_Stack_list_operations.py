#2 Stack Using List Operations

class Stack:
    def __init__(self):
        self.list = []                                  #Time O(1)
                                                        #Space O(1)
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
        
    #isEmpty
    def isEmpty(self):
        if self.list == []:                             #Time O(1)
            return True                                 #Space O(1)
        else:
            return False

    #push
    def push(self, value):                              #Time O(1)
        self.list.append(value)                         #Space O(1)                         
        return "The element has been inserted successfully"

    #pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in Stack"              #Time O(1)
        else:                                                       #Space O(1)
            #self.list = self.list.reverse()
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

        
    
a = Stack()
print(a.push(1))
print(a.push(2))        #Dont print stack between the operations
print(a.push(3))
a.pop()
print(a.peek())
print()
a.delete()
print(a)

