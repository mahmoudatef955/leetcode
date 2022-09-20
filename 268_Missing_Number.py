from ast import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSums = len(nums)
        x = 0
        for i in range(len(nums)):
            numsSums += i
            x += nums[i]
        return numsSums - x
