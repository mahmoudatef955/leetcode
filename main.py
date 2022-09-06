from __future__ import print_function
from ast import List
from termios import FFDLY
import time


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end="")
            temp = temp.next
        print()


def reverse_linked_list(head):
    prev = None
    while head is not None:
        current = head.next
        head.next = prev
        prev = head
        head = current
    return prev


def reorder(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    reversed_second_half = reverse_linked_list(slow)

    head_copy = head
    while reversed_second_half is not None and head.next is not None:
        head_next = head.next
        reversed_second_half_next = reversed_second_half.next
        head.next = reversed_second_half
        head.next.next = head_next
        head = head.next.next
        reversed_second_half = reversed_second_half_next

    head.next = None
    head = head_copy

    return


class Solution:
    def merge1(self, intervals):
        if len(intervals) < 2:
            return intervals

        merged_intervals = []

        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                merged_intervals.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        merged_intervals.append([start, end])

        return merged_intervals


def main():
    print(Solution().merge1([[1, 3], [2, 6], [8, 10], [15, 18]]))


main()


if __name__ == "__main__":
    st = time.time()
    main()

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
