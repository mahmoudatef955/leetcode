class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search_acc_rec(arr, key, lower, upper):
            if lower > upper or lower == len(arr):
                return -1

            middle = (lower + upper) // 2

            if arr[middle] == key:
                return middle
            elif arr[middle] < key:
                return binary_search_acc_rec(arr, key, middle + 1, upper)
            else:
                return binary_search_acc_rec(arr, key, lower, middle - 1)

        return binary_search_acc_rec(nums, target, 0, len(nums))
