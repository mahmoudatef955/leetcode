from __future__ import print_function
from ast import List
from errno import ENEEDAUTH
from termios import FFDLY
from heapq import *
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


def eraseOverlapIntervals(intervals) -> int:
    intervals.sort(key=lambda x: x[0])
    overlapCount = 0
    i = 0
    while i < len(intervals) - 1:
        j = i + 1
        while j < len(intervals) and intervals[j][0] < intervals[i][1]:
            overlapCount += 1
            if intervals[i][1] > intervals[j][1]:
                i += 1
            j += 1
        i = j
    return overlapCount


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.start < other.start


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)

    maxLoad = 0
    currentLoad = 0
    jobsHeap = []

    for job in jobs:

        while len(jobsHeap) > 0 and job.start >= jobsHeap[0].end:
            currentLoad -= jobsHeap[0].cpu_load
            heappop(jobsHeap)

        heappush(jobsHeap, job)
        currentLoad += job.cpu_load
        maxLoad = max(maxLoad, currentLoad)

    return maxLoad


def find_corrupt_numbers(nums):
    numsLength = len(nums)
    s1 = numsLength
    s2 = 0
    i = 0
    d = None
    m = None

    while i < numsLength:
        if nums[i] != i + 1:
            tmp = nums[nums[i] - 1]
            if tmp == nums[i]:
                d = tmp
                m = i + 1
                i += 1
            else:
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp

        else:
            s1 += i
            s2 += nums[i]
            i += 1

    s2 -= d
    return [d, s1 - s2, m]


def firstMissingPositive(nums) -> int:
    i, numsLength = 0, len(nums)
    while i < numsLength:
        if (
            nums[i] > 0
            and nums[i] <= numsLength
            and nums[i] != i + 1
            and nums[i] != nums[nums[i] - 1]
        ):
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1


def main():
    #                    1  2  3  4  5  > 15
    print(firstMissingPositive([1, 1]))
    # print(firstMissingPositive([3, 4, -1, 1]))
    # print(firstMissingPositive([7, 8, 9, 11, 12]))
    # print(find_corrupt_numbers([1]))


if __name__ == "__main__":
    main()
