# 4 Traversal Binary Heap

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


newBinaryHeap = Heap(5)
print(sizeHeap(newBinaryHeap))