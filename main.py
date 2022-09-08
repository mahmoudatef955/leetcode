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


def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1

    # skip (and add to output) all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    # insert the new_interval
    merged.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


class Solution:
    def insert(self, intervals, newInterval):
        # [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
        if len(intervals) == 0:
            return [newInterval]
        if len(intervals) == 1 and newInterval[0] > intervals[0][1]:
            intervals.append(newInterval)
            return intervals
        start = 0
        end = 0
        while start < len(intervals) and intervals[start][1] < newInterval[0]:
            start += 1
        # start -= 1
        end = start
        while end < len(intervals) and intervals[end][0] < newInterval[1]:
            end += 1

        while start >= len(intervals):
            start -= 1
        while end >= len(intervals):
            end -= 1

        if newInterval[1] < intervals[end][0] and end > 0:
            end -= 1

        if start == end == 0 and newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        c = [
            min(intervals[start][0], newInterval[0]),
            max(intervals[end][1], newInterval[1]),
        ]
        print(c)
        return intervals[:start] + [c] + intervals[end + 1 :]


def main():
    st = time.time()
    print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(Solution().insert([[1, 5]], [0, 3]))
    print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
    print(Solution().insert([[1, 5]], [6, 8]))
    print(Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1]))
    et = time.time()
    elapsed_time = et - st
    print("\nExecution time :", elapsed_time, "seconds\n")

    st = time.time()
    print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(insert([[1, 5]], [0, 3]))
    print(insert([[1, 3], [6, 9]], [2, 5]))
    print(insert([[1, 5]], [6, 8]))
    print(insert([[2, 5], [6, 7], [8, 9]], [0, 1]))
    et = time.time()
    elapsed_time = et - st
    print("\nExecution time :", elapsed_time, "seconds\n")


main()


if __name__ == "__main__":
    main()
