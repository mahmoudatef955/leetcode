import enum
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        if len(nums2) < len(nums1):
            for i, num in enumerate(nums2):
                if num in nums1:
                    intersect.append(num)
                    nums1.remove(num)

        else:
            for i, num in enumerate(nums1):
                if num in nums2:
                    intersect.append(num)
                    nums2.remove(num)

        return intersect


if __name__ == "__main__":
    sln = Solution()
    sss = sln.intersect([3, 1, 2], [1, 1])
    print(sss)
