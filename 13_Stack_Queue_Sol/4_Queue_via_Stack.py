#Queue via 2 stack
class Stack():
    def __init__(self):
        self.list=[]
    
    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
    
class Queue():
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        res = self.outStack.pop()

        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return res
    
cQ = Queue()
cQ.enqueue(1)
cQ.enqueue(2)
cQ.enqueue(3)
print(cQ.dequeue())
cQ.enqueue(4)
print(cQ.dequeue())
print(cQ.inStack.list)

