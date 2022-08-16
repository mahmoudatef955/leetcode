from ast import List
import math


def triplet_sum_close_to_target(arr: List[int], target_sum: int):
    closest_sum = math.inf
    closest_diff = math.inf
    arr.sort()

    for i in range(len(arr)):
        # if i > 0 and arr[i] == arr[i - 1]:
        #     continue
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right] + arr[i]
            # print(current_sum)
            # if current_sum == -2960:
            #     print(abs(target_sum - current_sum))
            if abs(target_sum - current_sum) < closest_diff:
                closest_sum = arr[i] + arr[left] + arr[right]

                closest_diff = abs(target_sum - current_sum)
                # left += 1
                # right -= 1
                # while left < right and arr[left] == arr[left - 1]:
                #     left += 1
                # while left < right and arr[right] == arr[right + 1]:
                #     right -= 1
            if current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return closest_sum
