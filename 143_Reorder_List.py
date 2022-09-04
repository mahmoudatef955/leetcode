# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_linked_list(self, head):
        prev = None
        while head is not None:
            current = head.next
            head.next = prev
            prev = head
            head = current
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        reversed_second_half = self.reverse_linked_list(slow)

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
