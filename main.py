from cgitb import small
import math
from operator import le
import time
from typing import List


def backspace_compare(str1, str2):
    pointer1, pointer2 = len(str1) - 1, len(str2) - 1
    while pointer1 > 0 or pointer2 > 0:
        if pointer1 > 0 and str1[pointer1] == "#":
            count = 0
            while pointer1 > 0 and str1[pointer1] == "#":
                count += 1
                pointer1 -= 1

            while count > 0:
                pointer1 -= 1
                if pointer1 < 0 or str1[pointer1] != "#":
                    count -= 1
                else:
                    count += 1
            continue

        if pointer2 > 0 and str2[pointer2] == "#":
            count = 0
            while pointer2 > 0 and str2[pointer2] == "#":
                count += 1
                pointer2 -= 1
            while count > 0:
                pointer2 -= 1
                if pointer2 < 0 or str2[pointer2] != "#":
                    count -= 1
                else:
                    count += 1
            continue

        if pointer1 < 0 or pointer2 < 0:
            return False

        if str1[pointer1] != str2[pointer2]:
            return False

        if pointer1 > 0 and pointer2 > 0:
            pointer1 -= 1
            pointer2 -= 1

    if (pointer1 < 0 and pointer2 >= 0) or (pointer2 < 0 and pointer1 >= 0):
        return False
    return True


def findUnsortedSubarray(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < len(nums) - 1 and nums[low + 1] >= nums[low]:
        low += 1
    while high > 0 and nums[high - 1] <= nums[high]:
        high -= 1

    if low == len(nums) - 1:
        return 0
    if low == 0 and high == len(nums) - 1:
        return len(nums)

    lowest = nums[low]
    highest = nums[high]
    for i in range(low, high + 1):
        lowest = min(lowest, nums[i])
        highest = max(highest, nums[i])

    while low > 0 and nums[low - 1] > lowest:
        low -= 1
    while high < len(nums) - 1 and nums[high + 1] < highest:
        high += 1

    return high - low + 1


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    # TODO: Write your code here
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))


if __name__ == "__main__":
    st = time.time()
    main()

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
