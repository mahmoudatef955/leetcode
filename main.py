from __future__ import print_function

from collections import deque


def find_permutations(nums):
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


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


if __name__ == "__main__":
    main()
