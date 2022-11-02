from heapq import *


class MedianFinder:
    # minHeap = []
    # maxHeap = []

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # print(num)
        if num is None:
            return
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        # print(self.maxHeap,self.minHeap)

    def findMedian(self) -> float:
        if not self.maxHeap and not self.minHeap:
            return 0.0
        if len(self.maxHeap) == len(self.minHeap):
            # print('median: ',-self.maxHeap[0] /2 + self.minHeap[0] / 2)
            return -self.maxHeap[0] / 2 + self.minHeap[0] / 2

        else:
            # print('median:  ',-self.maxHeap[0])
            return -self.maxHeap[0]

        # Your MedianFinder object will be instantiated and called as such:


# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
