#4 BST search node  

import QueueLL as queue


class BSTNode:
    def __init__(self, data):
        self.data = data                                #Time / Space O(1)
        self.left = None
        self.right = None

 #Insering node in BST   
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


#Pre order traversal in BST
def preOrder(rootNode):
    if rootNode is None:
        return          

    print(rootNode.data)                            #Time/Space O(n)
    preOrder(rootNode.left)
    preOrder(rootNode.right)


#In order traversal in BST
def inOrder(rootNode):
    if rootNode is None:
        return 
    inOrder(rootNode.left)                          #Time/ Space O(n)
    print(rootNode.data)
    inOrder(rootNode.right)


#Post Order Traversal in BST
def postOrder(rootNode):
    if rootNode is None:
        return 
    postOrder(rootNode.left)                        #Time/Space O(n)
    postOrder(rootNode.right)
    print(rootNode.data)



#Level order traversal
def levelOrder(rootNode):
    if rootNode is None:
        return 
    
    custQueue = queue.Queue()                               #Time/ Space O(n)
    custQueue.enqueue(rootNode)

    while not(custQueue.isEmpty()):
        root = custQueue.dequeue()
        print(root.value.data)

        if root.value.left:
            custQueue.enqueue(root.value.left)

        if root.value.right:
            custQueue.enqueue(root.value.right)



#Search node
def searchNode(rootNode, valueNode):
    if rootNode.data == valueNode:
        print("Value Found")
    
    elif valueNode < rootNode.data:
        if rootNode.left.data == valueNode:                 #Time/ Space O(logn)
            print("Value Found")
        else:
            searchNode(rootNode.left, valueNode)

    else:
        if rootNode.right.data == valueNode:
            print("Value Found")
        else:
            searchNode(rootNode.right, valueNode)





newBST = BSTNode(None)
insertBST(newBST, 70)
insertBST(newBST, 50)
insertBST(newBST, 90)
insertBST(newBST, 30)
insertBST(newBST, 60)
insertBST(newBST, 80)
insertBST(newBST, 100)
insertBST(newBST, 20)
insertBST(newBST, 40)

searchNode(newBST, 100)