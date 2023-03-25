#4 Inorder Traversal in Binary Tree LL 
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#Creation
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")     #T/S O(1)

newBT.left = leftChild
newBT.right = rightChild

#PreTraverse
def preTraver(rootNode):
    if not rootNode:
        return
    print(rootNode.data)              #O(1)
    preTraver(rootNode.left)          #O(n/2)      T/S  O(n)
    preTraver(rootNode.right)         #O(n/2)

#Inorder
def inOrdTrav(rootNode):
    if not rootNode:
        return
    inOrdTrav(rootNode.left)        #O(n/2)
    print(rootNode.data)            #O(1)           T/S  O(n)
    inOrdTrav(rootNode.right)       #O(n/2)

inOrdTrav(newBT)