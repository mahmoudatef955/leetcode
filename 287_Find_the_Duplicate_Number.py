from ast import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                tmp = nums[nums[i] - 1]
                if tmp == nums[i]:
                    return tmp
                else:
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = tmp
            else:
                i += 1
