import math
from operator import le
import time
from typing import List


def search_quadruplets(arr: List[int], target):
    quadruplets = []
    arr.sort()
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        first_target = target - arr[i]
        for j in range(i + 1, len(arr) - 1):
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


if __name__ == "__main__":
    st = time.time()

    # print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))
    # print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    # print(search_quadruplets([0, 0, 0, 0], 0))
    print(search_quadruplets([-2, -1, -1, 1, 1, 2, 2], 0))
    # print(search_quadruplets([1, -2, -5, -4, -3, 3, 3, 5], -11))

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
