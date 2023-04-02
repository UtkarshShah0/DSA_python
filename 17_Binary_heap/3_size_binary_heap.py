# 3 Size Binary Heap

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
    

newBinaryHeap = Heap(5)
print(sizeHeap(newBinaryHeap))