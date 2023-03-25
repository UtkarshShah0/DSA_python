#16 Binary tree delete node and delete full using python list
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

    
    def levOrder(self, index):
        for i in range(index, self.lastUsedIndex+1):                    #Time O(n)
            print(self.customList[i])                                   #Spacde O(1)


    def deleteNode(self, valueNode):
        if self.lastUsedIndex == 0:
            return "No node to delete"
        
        for i in range(1, self.lastUsedIndex+1):
            if (self.customList[i] == valueNode):                                  #Time O(n)
                self.customList[i] = self.customList[self.lastUsedIndex]           #Space O(1)
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Successfully Deleted Node"
            

    def deleteBT(self):
        self.customList = None                                        #Time / Space O(1)

newBT = binaryTree(8)

newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

newBT.deleteNode("Cold")
newBT.deleteBT()
newBT.levOrder(1)



