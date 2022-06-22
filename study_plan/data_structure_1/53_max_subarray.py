from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = {}
        for i, n in enumerate(nums):
            max_sum[i] = i


if __name__ == "__main__":
    sln = Solution()
    sss = sln.maxSubArray([1, 1, 2])
    print(sss)
