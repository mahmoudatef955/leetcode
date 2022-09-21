from ast import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                tmp = nums[nums[i] - 1]
                if tmp == nums[i]:
                    duplicates.add(tmp)
                    i += 1
                else:
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = tmp
            else:
                i += 1

        return list(duplicates)
