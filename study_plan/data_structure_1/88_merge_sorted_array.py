from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i2 = 0
        # for i in range(m, m + n):
        #     nums1[i] = nums2[i2]
        #     i2 += 1

        # nums1.sort()
        # print(nums1)

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        print(nums1)


if __name__ == "__main__":
    sln = Solution()
    sss = sln.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(sss)
