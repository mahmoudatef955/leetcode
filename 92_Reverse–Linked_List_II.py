# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

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
