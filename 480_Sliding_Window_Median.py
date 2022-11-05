class Solution:
    minHeap = []
    maxHeap = []

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insert(self, num):
        if num is None:
            return
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, - heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, - heappop(self.minHeap))

    def cal_median(self):
        if not self.maxHeap and not self.minHeap:
            return 0

        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2 + self.minHeap[0] / 2
        else:
            return -self.maxHeap[0]

    def remove_num(self, num):
        if -num in self.maxHeap:
            ind = self.maxHeap.index(-num)
            self.maxHeap[ind] = self.maxHeap[-1]
            del self.maxHeap[-1]
            if ind < len(self.maxHeap):
                heapq._siftup(self.maxHeap, ind)
                heapq._siftdown(self.maxHeap, 0, ind)
            # heapify(self.maxHeap)

        elif num in self.minHeap:
            ind = self.minHeap.index(num)
            self.minHeap[ind] = self.minHeap[-1]
            del self.minHeap[-1]
            if ind < len(self.minHeap):
                heapq._siftup(self.minHeap, ind)
                heapq._siftdown(self.minHeap, 0, ind)

        # Rebalance
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, - heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, - heappop(self.minHeap))

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = []
        start_pointer = 0
        for i in range(len(nums)):
            self.insert(nums[i])

            if i - start_pointer == k - 1:
                result.append(self.cal_median())
                self.remove_num(nums[start_pointer])
                start_pointer += 1

        return result

