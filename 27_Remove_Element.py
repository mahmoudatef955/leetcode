from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[next_pointer] = nums[i]
                next_pointer += 1
        print(nums)
        return next_pointer
