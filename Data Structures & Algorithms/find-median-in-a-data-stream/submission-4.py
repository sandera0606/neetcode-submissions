class MedianFinder:

    def __init__(self):
        self.upperHalf = [] # min heap
        self.lowerHalf = [] # max heap

    def addNum(self, num: int) -> None:
        if not self.upperHalf:
            heapq.heappush(self.upperHalf, num)
        elif num > self.upperHalf[0]:
            heapq.heappush(self.upperHalf, num)
        else:
            heapq.heappush_max(self.lowerHalf, num)
        
        # reorganize
        if len(self.upperHalf) > len(self.lowerHalf) + 1:
            value = heapq.heappop(self.upperHalf)
            heapq.heappush_max(self.lowerHalf, value)
        elif len(self.upperHalf) + 1 < len(self.lowerHalf):
            value = heapq.heappop_max(self.lowerHalf)
            heapq.heappush(self.upperHalf, value)


    def findMedian(self) -> float:
        if len(self.upperHalf) == len(self.lowerHalf):
            return (self.upperHalf[0] + self.lowerHalf[0]) / 2
        elif len(self.upperHalf) > len(self.lowerHalf):
            return self.upperHalf[0]
        else:
            return self.lowerHalf[0]