#Preorder Traversal in Binary Tree using LL
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
newBT = TreeNode("Drinks")
leftChild  = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.left = leftChild
newBT.right = rightChild

def preTraver(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preTraver(rootNode.left)
    preTraver(rootNode.right)

preTraver(newBT)
