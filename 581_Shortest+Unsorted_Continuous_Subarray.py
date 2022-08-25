class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < len(nums) - 1 and nums[low + 1] >= nums[low]:
            low += 1
        while high > 0 and nums[high - 1] <= nums[high]:
            high -= 1

        if low == len(nums) - 1:
            return 0
        if low == 0 and high == len(nums) - 1:
            return len(nums)

        lowest = nums[low]
        highest = nums[high]
        for i in range(low, high + 1):
            lowest = min(lowest, nums[i])
            highest = max(highest, nums[i])

        while low > 0 and nums[low - 1] > lowest:
            low -= 1
        while high < len(nums) - 1 and nums[high + 1] < highest:
            high += 1

        return high - low + 1
