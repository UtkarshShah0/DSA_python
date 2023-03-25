#12 Binary tree using python list
class binaryTree:
    def __init__(self, size):
        self.customList = size * [None]                 #Time O(1)
        self.lastUsedIndex = 0                          #Space O(n)
        self.maxSize = size

        
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "BT is full"                                                 #Time/ Space O(1) 
        self.lastUsedIndex += 1
        self.customList[self.lastUsedIndex] = value
        return "The value has been inserted successfully"
 
newBT = binaryTree(8)

print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))