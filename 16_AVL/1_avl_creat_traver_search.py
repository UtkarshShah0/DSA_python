#1 AVL tree creation traversal search
import QueueLL as queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None                                        #Time/ Space O(1)
        self.right = None
        self.height = 1


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)                                           #Time/ Space O(n)
    preOrder(rootNode.left)
    preOrder(rootNode.right)


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)                                          #Time/ Space O(n)
    print(rootNode.data)
    inOrder(rootNode.right)


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)                                        #Time/ Space O(n)
    postOrder(rootNode.right)
    print(rootNode.data)


def levelOrder(rootNode):
    if not rootNode:
        return
    
    custQueue = queue.Queue()
    custQueue.enqueue(rootNode)

    while not(custQueue.isEmpty()):
        root = custQueue.dequeue()
        print(root.value.data)                                                #Time/ Space O(n)

        if root.value.left:
            custQueue.enqueue(root.value.left)

        if root.value.right:
            custQueue.enqueue(root.value.right)



def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        return "Found Value"
    
    elif nodeValue < rootNode.data:
        if rootNode.left.data == nodeValue:                                 #Time/ Space O(logn)
            print("Found Value")
        else:
            searchNode(rootNode.left, nodeValue)

    else:
        if rootNode.right.data == nodeValue:
            print("Found Value")
        else:
            searchNode(rootNode.rigth, nodeValue)


#To get height 
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


#Right Rotation for AVL Tree
def rightRotate(disBalancedNode):
    newRoot = disBalancedNode.left                              #Time/ Space O(1)
    disBalancedNode.left = newRoot.right
    newRoot.right = disBalancedNode
    disBalancedNode.height = 1 + max(getHeight(disBalancedNode.left), getHeight(disBalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot



#Left Rotation for AVL tree
def leftRotate(disBalancedNode):
    newRoot = disBalancedNode.right
    disBalancedNode.right = newRoot.left                        #Time/ Space O(1)
    newRoot.left = disBalancedNode
    disBalancedNode.height = 1 + max(getHeight(disBalancedNode.left), getHeight(disBalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


#To get self balancing factor
def getBalance(rootNode):
    if not rootNode:
        return 0                                                                #Time/ Space O(1)
    return getHeight(rootNode.left) - getHeight(rootNode.right)




#Insert Node in AVL Tree
def insertNode(rootNode, nodeValue):
    if not rootNode: 
        return AVLNode(nodeValue)
    
    elif (nodeValue <= rootNode.data):
        rootNode.left = insertNode(rootNode.left, nodeValue)                    #Time/ Space O(logn)
        # if rootNode.left == None:
        #     rootNode.left = AVLNode(nodeValue)
        #     return "Success Left"
        # else:
        #     insertNode(rootNode.left, nodeValue)

    else:
        rootNode.right = insertNode(rootNode.right, nodeValue)
        # if rootNode.right == None:
        #     rootNode.right = AVLNode(nodeValue)
        #     return "Success Right"
        # else:
        #     insertNode(rootNode.right, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)

    #LL Condition
    if balance > 1 and nodeValue < rootNode.left.data:
        return rightRotate(rootNode)

    #LR Condition 
    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)

    #RR Condition
    if balance < -1 and nodeValue > rootNode.right.data:
        return leftRotate(rootNode)
    
    #RL Condition
    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode

    

newAVL = AVLNode(20)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 30)
newAVL = insertNode(newAVL, 40)
newAVL = insertNode(newAVL, 50)
newAVL = insertNode(newAVL, 60)

levelOrder(newAVL)
