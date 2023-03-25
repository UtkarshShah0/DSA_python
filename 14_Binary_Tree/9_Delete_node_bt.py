#9 Deleting node in binary tree (most left possible)

import QueueLL as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#Creation
newBT = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")     #T/S O(1)

newBT.left = hot
newBT.right = cold

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.left = tea
hot.right = coffee

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

#PostOrder
def postTraver(rootNode):
    if not rootNode:
        return
    postTraver(rootNode.left)       #O(n/2)         T/S  O(n)
    postTraver(rootNode.right)      #O(n/2)
    print(rootNode.data)


#LevelOrder
def levOrdTraver(rootNode):
    if not rootNode:
        return
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)

        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()
            print(root.value.data)

            if (root.value.left):
                custQueue.enqueue(root.value.left)

            if (root.value.right):
                custQueue.enqueue(root.value.right)
    


#Search binary tree
def searchBT(rootNode, search):
    if not rootNode:
        return "The BT does not exist"
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)

        while not(custQueue.isEmpty()):                                 #Time O(n)
            root = custQueue.dequeue()                                  #Space O(n)
            if root.value.data == search:
                return "Found"
            else:
                if (root.value.left):
                    custQueue.enqueue(root.value.left)
                
                if(root.value.right):
                    custQueue.enqueue(root.value.right)

        return "Not Found"
    

#Insert node in bt
def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)

        while not(custQueue.isEmpty()):                                #Time O(n)
            root = custQueue.dequeue()                                 #Space O(n)

            if root.value.left:
                custQueue.enqueue(root.value.left)
            else:
                root.value.left = newNode
                return "Success left"
            
            if root.value.right:
                custQueue.enqueue(root.value.right)
            else:
                root.value.right = newNode
                return "Success right"
            

# Deepest Node
def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)

        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()

            if(root.value.left):
                custQueue.enqueue(root.value.left)
            
            if(root.value.right):
                custQueue.enqueue(root.value.right)
        return root.value
    
    
#Delete last node
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)

        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()

            if root.value is dNode:
                root.value = None
                return
            
            if root.value.right:
                if root.value.right is dNode:
                    root.value.right = None
                    return
                else:
                    custQueue.enqueue(root.value.right)

            if root.value.left:
                if root.value.left is dNode:
                    root.value.left = None
                    return
                else:
                    custQueue.enqueue(root.value.left)



def deleteNodeBT(rootNode, node):
    if not rootNode:                                                    # O(1)
        return "The BT does not exist"
    else:
        custQueue = queue.Queue()                                       #O(1)
        custQueue.enqueue(rootNode)

        while not(custQueue.isEmpty()):                                 #O(n)
            root = custQueue.dequeue()

            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data                            #O(n)
                deleteDeepestNode(rootNode, dNode)
                return "The Node has been successfully deleted"
                                                                        #O(1)
            if root.value.left:
                custQueue.enqueue(root.value.left)

            if root.value.right:
                custQueue.enqueue(root.value.right)                     #Time/Space O(n)

        return "Failed to delete"


# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)
deleteNodeBT(newBT, "Hot")
levOrdTraver(newBT)