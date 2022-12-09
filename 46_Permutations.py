from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        result = []
        permutations = deque()
        permutations.append([])

        for i in range(nums_length):
            per_len = len(permutations)

            for _ in range(per_len):
                current_per = list(permutations.popleft())
                for x in range(len(current_per) + 1):
                    new = current_per.copy()
                    new.insert(x, nums[i])

                    if len(new) == nums_length:
                        result.append(new)
                    else:
                        permutations.append(new)

        return result
