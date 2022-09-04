from __future__ import print_function
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


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()


if __name__ == "__main__":
    st = time.time()
    main()

    et = time.time()
    elapsed_time = et - st
    # print('\nExecution time :', elapsed_time, 'seconds')
