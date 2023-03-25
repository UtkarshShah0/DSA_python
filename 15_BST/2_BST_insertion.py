#2 BST insertion

class BSTNode:
    def __init__(self, data):
        self.data = data                                #Time / Space O(1)
        self.left = None
        self.right = None

    
def insertBST(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
        return "Success "
        
    elif(nodeValue <= rootNode.data):
        if(rootNode.left == None):                                  #Time O(logn)
            rootNode.left = BSTNode(nodeValue)                      #Space O(logn)
            return "Success Left"                               
        else:                                                       #Worst skewed Tree O(n)
            insertBST(rootNode.left, nodeValue)

    else:
        if(rootNode.right == None):
            rootNode.right = BSTNode(nodeValue)
            return "Success Right"
        else:
            insertBST(rootNode.right, nodeValue)



newBST = BSTNode(None)
insertBST(newBST, 10)
insertBST(newBST, 70)