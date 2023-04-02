# 1 Creation Binary Heap

class Heap:
    def __init__(self, size) -> None:
        self.customList = [None]*(size+1)
        self.heapSize = 0                                        #Time O(1)
        self.maxSize = size + 1                                  #Space O(n)

newBinaryHeap = Heap(5)