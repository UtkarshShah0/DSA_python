#14 Binary tree pre-in-post-order search using python list
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
    
    
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):                                   #Time O(n)
            if self.customList[i] == nodeValue:                                 #Space O(1)
                return "Success {}".format(i)
        return "Not found"
 

    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])                                   #Time O(n/2) -> O(n)
        self.preOrder(index*2)                                          #Space O(n)
        self.preOrder(index*2+1)


    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrder(index*2)                                           #Time/ Space O(n)
        print(self.customList[index])
        self.inOrder(index*2 + 1)


    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return 
        self.postOrder(index*2)                                         #Time/Space O(n)
        self.postOrder(index*2 + 1)
        print(self.customList[index])

newBT = binaryTree(8)

newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

print("PreOrder NLR")
newBT.preOrder(1)
print()

print("Inorder LNR")
newBT.inOrder(1)
print()

print("PostOrder LRN")
newBT.postOrder(1)
print()

