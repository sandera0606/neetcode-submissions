class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
            return
        # push to appropriate heap
        if self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        
        # reorganize heaps
        if len(self.minHeap) - len(self.maxHeap) > 1:
            # pop from minHeap
            move = heapq.heappop(self.minHeap)
            # push to maxHeap
            heapq.heappush_max(self.maxHeap, move)
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            # pop from maxHeap
            move = heapq.heappop_max(self.maxHeap)
            # push to minHeap
            heapq.heappush(self.minHeap, move)
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0])/2
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return self.maxHeap[0]
        