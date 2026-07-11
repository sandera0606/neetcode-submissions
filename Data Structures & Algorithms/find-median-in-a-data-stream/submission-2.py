class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def balanceHeaps(self):
        # heaps are two apart
        if len(self.minHeap) - len(self.maxHeap) >= 2:
            val = self.heapPop(True)
            self.heapAdd(val, False) # add value to maxHeap
        elif len(self.maxHeap) - len(self.minHeap) >= 2:
            val = self.heapPop(False)
            self.heapAdd(val, True) # add value to minHeap
        # otherwise it's ok, so do nothing

    def heapAdd(self, val, min: bool):
        heap = self.minHeap if min else self.maxHeap
        heap.append(val)
        self.fixUp(min)

    def heapPop(self, min: bool) -> int:
        heap = self.minHeap if min else self.maxHeap
        res = heap[0]
        val = heap.pop()
        heap[0] = val
        self.fixDown(min)
        return res

    def fixUp(self, min: bool):
        heap = self.minHeap if min else self.maxHeap
        index = len(heap) - 1
        while index > 0:
            parentIndex = (index - 1) // 2
            if min:
                if heap[index] < heap[parentIndex]:
                    # swap 
                    temp = heap[parentIndex]
                    heap[parentIndex] = heap[index]
                    heap[index] = temp
                else:
                    break
            else:
                if heap[index] > heap[parentIndex]:
                    # swap
                    temp = heap[parentIndex]
                    heap[parentIndex] = heap[index]
                    heap[index] = temp
                else:
                    break
            index = parentIndex
        
    def fixDown(self, min: bool):
        heap = self.minHeap if min else self.maxHeap
        # left child = 2 * i + 1
        # right child = 2 * i + 2
        index = 0
        while 2 * index < len(heap) - 1:
            left = 2 * index + 1
            right = 2 * index + 2
            # min heap
            if min:
                if right < len(heap) and heap[right] < heap[left] and heap[index] > heap[right]:
                    # swap with right
                    temp = heap[right]
                    heap[right] = heap[index]
                    heap[index] = temp
                    index = right
                elif heap[index] > heap[left]:
                    # swap w left
                    temp = heap[left]
                    heap[left] = heap[index]
                    heap[index] = temp
                    index = left
                else:
                    break
            else: # max heap
                if right < len(heap) and heap[right] > heap[left] and heap[index] < heap[right]:
                    # swap with right
                    temp = heap[right]
                    heap[right] = heap[index]
                    heap[index] = temp
                    index = right
                elif heap[index] < heap[left]:
                    # swap w left
                    temp = heap[left]
                    heap[left] = heap[index]
                    heap[index] = temp
                    index = left
                else:
                    break
    
    def peek(self, heap) -> int:
        if not heap:
            return None
        return heap[0]

    def addNum(self, num: int) -> None:
        bottomMax = self.peek(self.maxHeap)
        upperMin = self.peek(self.minHeap)

        if bottomMax is None and upperMin is None:
            self.minHeap.append(num) # just add to minHeap if nothing yet
            return
        
        if upperMin is None or num <= upperMin:
            # add to maxHeap
            self.heapAdd(num, False)
            self.balanceHeaps()
            return
        if bottomMax is None or num >= bottomMax:
            # add to minHeap
            self.heapAdd(num, True)
            self.balanceHeaps()
            return

    def findMedian(self) -> float:
        if len(self.minHeap) < len(self.maxHeap):
            return self.peek(self.maxHeap)
        elif len(self.maxHeap) < len(self.minHeap):
            return self.peek(self.minHeap)
        else:
            return (self.peek(self.maxHeap) + self.peek(self.minHeap)) / 2
        