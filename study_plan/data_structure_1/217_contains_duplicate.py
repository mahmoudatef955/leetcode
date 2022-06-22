from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        else:
            return False


if __name__ == "__main__":
    sln = Solution()
    sss = sln.containsDuplicate([1, 1, 2])
    print(sss)
