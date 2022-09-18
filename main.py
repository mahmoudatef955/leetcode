from __future__ import print_function
from ast import List
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


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)

    minRoom = 0
    roomsHeap = []

    for meeting in meetings:

        while len(roomsHeap) > 0 and meeting.start >= roomsHeap[0].end:
            heappop(roomsHeap)

        heappush(roomsHeap, meeting)
        minRoom = max(minRoom, len(roomsHeap))

    return minRoom


def main():
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(
            min_meeting_rooms(
                [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]
            )
        )
    )


if __name__ == "__main__":
    main()
