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


def intervalIntersection(firstList, secondList):
    if len(firstList) == 0 or len(secondList) == 0:
        return []

    intersections = []
    secondListPointer = 0
    firstListPointer = 0

    while firstListPointer < len(firstList) and secondListPointer < len(secondList):
        x = max(firstList[firstListPointer][0], secondList[secondListPointer][0])
        y = min(firstList[firstListPointer][1], secondList[secondListPointer][1])
        if y >= x:
            intersections.append([x, y])

        if y >= firstList[firstListPointer][1]:
            firstListPointer += 1
        if y >= secondList[secondListPointer][1]:
            secondListPointer += 1

    return intersections


def main():
    st = time.time()
    print(
        "Intervals Intersection: "
        + str(intervalIntersection([[2, 3], [5, 7]], [[1, 3], [5, 6], [7, 9]]))
    )
    # print(
    #     "Intervals Intersection: "
    #     + str(intervalIntersection([[1, 3], [5, 7], [9, 12]], [[5, 10]]))
    # )
    # print(
    #     "Intervals Intersection: "
    #     + str(
    #         intervalIntersection(
    #             [[0, 2], [5, 10], [13, 23], [24, 25]],
    #             [[1, 5], [8, 12], [15, 24], [25, 26]],
    #         )
    #     )
    # )
    et = time.time()
    elapsed_time = et - st
    print("\nExecution time :", elapsed_time, "seconds\n")


if __name__ == "__main__":
    main()
