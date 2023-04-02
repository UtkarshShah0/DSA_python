# 2 Peek Binary Heap

class Heap:
    def __init__(self, size) -> None:
        self.customList = [None]*(size+1)
        self.heapSize = 0                                        #Time O(1)
        self.maxSize = size + 1                                  #Space O(n)


def peekHeap(rootNode):
    if not rootNode:                                               #Time/ Space O(1)
        return
    else:
        return rootNode.customList[1]
newBinaryHeap = Heap(5)