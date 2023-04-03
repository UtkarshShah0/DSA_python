# 5 insert Binary Heap

class Heap:
    def __init__(self, size) -> None:
        self.customList = [None]*(size+1)
        self.heapSize = 0                                        #Time O(1)
        self.maxSize = size + 1                                  #Space O(n)

#peek method
def peekHeap(rootNode):
    if not rootNode:                                               #Time/ Space O(1)
        return
    else:
        return rootNode.customList[1]
    

#size/lenght method
def sizeHeap(rootNode):
    if not rootNode:
        return                                                  #Time/ Space O(1)
    else:
        return rootNode.heapSize


#Traversal Binary Heap
def levelOrder(rootNode):
    if not rootNode:                                                #Time O(1)
        return                                                      #Space O(n)
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])



#Insert Heapify
def insertHeapify(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[parentIndex] > rootNode.customList[index]:
            temp = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = rootNode.customList[index]                   #Time/ Space O(logn)
            rootNode.customList[index] = temp

        insertHeapify(rootNode ,parentIndex , "Min")
    
    elif heapType == "Max":
        if rootNode.customList[parentIndex] < rootNode.customList[index]:
            temp = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = rootNode.customList[index]
            rootNode.customList[index] = temp

        insertHeapify(rootNode, parentIndex, "Max")


#Insert Node in Binary Heap
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Binary Heap is full"
    
    rootNode.customList[rootNode.heapSize + 1] = nodeValue                      #Time/ Space O(logn)
    rootNode.heapSize += 1
    insertHeapify(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"





newHeap = Heap(5)

insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")

levelOrder(newHeap)

# print(sizeHeap(newBinaryHeap))