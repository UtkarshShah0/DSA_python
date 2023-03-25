#11 Binary tree using python list
class binaryTree:
    def __init__(self, size):
        self.customList = size * [None]             #Time O(1)
        self.lastUsedIndex = 0                      #Space O(n)
        self.maxSize = size

newBT = binaryTree(8)