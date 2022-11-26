class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            subset_l = len(result)

            for i in range(subset_l):
                c = list(result[i])
                c.append(num)
                result.append(c)

        return result
