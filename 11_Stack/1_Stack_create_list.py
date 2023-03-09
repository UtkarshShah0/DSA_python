#1 Stack Creation Using List

class Stack:
    def __init__(self):
        self.list = []                                  #Time O(1)
                                                        #Space O(1)
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.test]
        return "\n".join(values)
        
 
