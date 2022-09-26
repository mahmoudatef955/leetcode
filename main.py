from __future__ import print_function
from ast import List
from errno import ENEEDAUTH
from termios import FFDLY
from heapq import *
import time
from typing import Optional


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


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head):
    prev = None
    while head is not None:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp

    return prev


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Node, left: int, right: int) -> Node:

    if left == right:
        return head

    p_count = 1
    prev, last_before_reverse, first_after_reverse = None, None, None
    first_head = head
    ttt = None
    while head is not None and p_count <= right:
        if p_count < left:
            last_before_reverse = head
            head = head.next
            # p_count += 1
        else:
            if p_count == left:
                ttt = head
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        p_count += 1
        if p_count == right:
            first_after_reverse = head
            if head is not None and head.next is not None:
                ttt.next = head.next

    if last_before_reverse is not None and last_before_reverse.next is not None:
        last_before_reverse.next = first_after_reverse

    if left == 1:
        return first_after_reverse
    return first_head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverseBetween(head, 1, 2)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


if __name__ == "__main__":
    main()
