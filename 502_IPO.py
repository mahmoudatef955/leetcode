from heapq import *


class Solution:
    def findMaximizedCapital(self, numberOfProjects: int, initialCapital: int, profits: List[int],
                             capital: List[int]) -> int:
        minHeapCapital = []
        maxHeapProfit = []

        for i in range(len(capital)):
            heappush(minHeapCapital, (capital[i], i))

        for i in range(numberOfProjects):
            while minHeapCapital and minHeapCapital[0][0] <= initialCapital:
                c = heappop(minHeapCapital)
                heappush(maxHeapProfit, -profits[c[1]])

            if maxHeapProfit:
                initialCapital += -heappop(maxHeapProfit)

        return initialCapital
