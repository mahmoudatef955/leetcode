from cgitb import small
from inspect import stack
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


def isPalindrome(x: int) -> bool:
    num_str = str(x)
    pointer1, pointer2 = 0, len(num_str) - 1
    while pointer1 != pointer2:
        if num_str[pointer1] != num_str[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def wis_palindromic_linked_list(head):
    fast, slow = head, head
    first_half_stack = []
    first_half_stack.append(head.val)
    count = 0

    # find the middle of the list
    while fast is not None and fast.next is not None:
        slow = slow.next
        first_half_stack.append(slow.val)
        count += 1
        print(slow.val)
        fast = fast.next.next

    # pointer = head
    # n = first_half_stack.pop()
    # slow = slow.next
    if count % 2 == 0:
        first_half_stack.pop()

    while slow is not None:
        n = first_half_stack.pop()
        print(n, slow.val)
        if n != slow.val:
            return False
        slow = slow.next

    # print(first_half_stack.is)
    if len(first_half_stack) > 0:
        return False

    return True


def reverse_linked_list(head):
    prev = None
    while head is not None:
        current = head.next
        head.next = prev
        prev = head
        head = current
    return prev


def is_palindromic_linked_list(head):
    if head.next is None or head is None:
        return True
    fast, slow = head, head

    # find the middle of the list
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    reversed_second_half = reverse_linked_list(slow)
    reversed_second_half_copy = reversed_second_half

    while head is not None and reversed_second_half is not None:
        print(head.val, reversed_second_half.val)
        if head.val != reversed_second_half.val:
            break
        head = head.next
        reversed_second_half = reversed_second_half.next

    reverse_linked_list(reversed_second_half_copy)

    if head is None or reversed_second_half is None:
        return True

    return False


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(4)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    # head.next.next.next.next.next = Node(2)
    # print("Is palindrome: " + str(is_palindromic_linked_list(head)))


if __name__ == "__main__":
    st = time.time()
    main()

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
