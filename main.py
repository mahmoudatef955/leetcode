import math
from operator import le
import time
from typing import List


def find_subarrays(arr, target):
    count = 0
    left, right = 0, 0

    return count


def dutch_flag_sort(arr):
    # [1, 0, 2, 1, 0]   [2, 2, 0, 1, 2, 0]   0 0 2 1 1
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

            # if arr[i] == 2 and i < right:
            #     temp = arr[right]
            #     arr[right] = arr[i]
            #     arr[i] = temp
            #     right -= 1

    return arr


if __name__ == "__main__":
    st = time.time()

    arr = [2, 0, 2, 1, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    # arr = [2, 1, 2]
    # dutch_flag_sort(arr)
    # print(arr)

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
