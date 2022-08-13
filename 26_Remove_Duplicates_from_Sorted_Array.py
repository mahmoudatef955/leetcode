from typing import List


class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        last_non_duplicate = 1

        pointer = 1
        while pointer < len(arr):
            if arr[pointer] != arr[pointer - 1]:
                arr[last_non_duplicate] = arr[pointer]
                last_non_duplicate += 1

            pointer += 1

        return last_non_duplicate
