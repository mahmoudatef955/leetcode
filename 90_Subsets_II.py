class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        added = {}

        nums.sort()

        count = 0
        for index in range(len(nums)):
            subset_l = len(result)
            if index > 0 and nums[index] == nums[index - 1]:
                prev_count = count
                count = 0
                for i in range(subset_l - prev_count, subset_l):
                    c = list(result[i])
                    c.append(nums[index])
                    count += 1
                    result.append(c)
            else:
                count = 0
                for i in range(subset_l):
                    c = list(result[i])
                    c.append(nums[index])
                    count += 1
                    result.append(c)

        return result
