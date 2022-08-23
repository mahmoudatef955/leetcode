from ast import List


class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        arr.sort()
        for i in range(len(arr) - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            first_target = target - arr[i]
            for j in range(i + 1, len(arr) - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                second_target = first_target - arr[j]
                left, right = j + 1, len(arr) - 1
                while left < right:
                    if arr[left] + arr[right] == second_target:
                        quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        while arr[left] == arr[left - 1] and left < right:
                            left += 1

                        right -= 1
                        while (
                            right != len(arr) - 1 and arr[right] == arr[right + 1]
                        ) and left < right:
                            right -= 1
                    elif arr[left] + arr[right] < second_target:
                        left += 1
                    else:
                        right -= 1
        return quadruplets
