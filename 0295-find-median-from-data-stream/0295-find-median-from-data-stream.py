class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.small,-num)
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large,-tmp)
        else:
            heapq.heappush(self.large,num)
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small,-tmp)
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        else:
            return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()