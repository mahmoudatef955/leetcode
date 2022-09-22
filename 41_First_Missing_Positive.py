from ast import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, numsLength = 0, len(nums)
        while i < numsLength:
            if (
                nums[i] > 0
                and nums[i] <= numsLength
                and nums[i] != i + 1
                and nums[i] != nums[nums[i] - 1]
            ):
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return numsLength + 1
