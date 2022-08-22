from ast import List


class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(arr) - 1

        for i in range(len(arr)):
            while arr[i] == 2 and i < right:
                temp = arr[right]
                arr[right] = arr[i]
                arr[i] = temp
                right -= 1

            while arr[i] == 0 and i > left:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
