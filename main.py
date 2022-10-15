from __future__ import print_function

from collections import deque


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


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    queue = deque()
    queue.append(root)
    while queue:
        l_size = len(queue)
        for i in range(l_size):
            node = queue.popleft()
            if node:
                if i < l_size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    return root


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


if __name__ == "__main__":
    main()
