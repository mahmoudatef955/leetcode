from heapq import *


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_max_heap = []
        end_max_heap = []

        start_min_heap = []

        result = [-1 for _ in range(len(intervals))]

        for i in range(len(intervals)):
            heappush(start_max_heap, (-intervals[i][0], i))
            heappush(end_max_heap, (-intervals[i][1], i))

        while end_max_heap:
            c = heappop(end_max_heap)

            cc = heappop(start_max_heap)

            while start_max_heap and -start_max_heap[0][0] >= -c[0]:
                cc = heappop(start_max_heap)
                # heappush(start_min_heap, (-cc[0], cc[1]))

            if -cc[0] >= -c[0]:
                result[c[1]] = cc[1]

            heappush(start_max_heap, cc)

        return result
