
from ast import List


def search_triplets(arr: List[int]):
    triplets = []
    arr.sort()
    # print(arr)
    for i in range(len(arr) - 2):
        if i>0 and arr[i] == arr[i-1]:
            continue
        right = len(arr) - 1
        left = i + 1
        target_sum = 0 - arr[i]
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            if current_sum < target_sum:
                left += 1
            if current_sum > target_sum:
                right -= 1

    return triplets
