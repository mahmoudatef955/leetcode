from ast import List


class Solution1:
    def removeDuplicates11(self, nums: List[int]) -> int:
        rr = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                rr.append(i)
        for i in rr:
            del nums[i]
        return len(nums)





    # function to remove duplicates from a sorted list in place (without extra memory)
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # i = 0
        # for j in range(1, len(nums)):
        #     if nums[i] != nums[j]:
        #         i += 1
        #         nums[i] = nums[j]
        # return i + 1


# 1 1 2 3 4 4 5 6 7 8 8 9 9
