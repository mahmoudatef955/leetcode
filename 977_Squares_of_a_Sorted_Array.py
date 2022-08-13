from typing import List


def index_first_positive(nums: list) -> int:
    for i in range(len(nums)):
        if nums[i] >= 0:
            return i
    return len(nums) - 1


def sortedSquares(nums: List[int]) -> List[int]:
    sorted_square = []
    right = index_first_positive(nums)
    left = right - 1

    while left >= 0 and right < len(nums):
        if pow(nums[right], 2) < pow(nums[left], 2):
            sorted_square.append(pow(nums[right], 2))
            right += 1
        else:
            sorted_square.append(pow(nums[left], 2))
            left -= 1

    while left >= 0:
        sorted_square.append(pow(nums[left], 2))
        left -= 1
    while right < len(nums):
        sorted_square.append(pow(nums[right], 2))
        right += 1

    return sorted_square
