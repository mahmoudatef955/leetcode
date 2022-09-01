# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverse_linked_list(self, head):
        prev = None
        while head is not None:
            current = head.next
            head.next = prev
            prev = head
            head = current
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None or head is None:
            return True
        fast, slow = head, head

        # find the middle of the list
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        reversed_second_half = self.reverse_linked_list(slow)
        reversed_second_half_copy = reversed_second_half

        while head is not None and reversed_second_half is not None:
            print(head.val, reversed_second_half.val)
            if head.val != reversed_second_half.val:
                break
            head = head.next
            reversed_second_half = reversed_second_half.next

        self.reverse_linked_list(reversed_second_half_copy)

        if head is None or reversed_second_half is None:
            return True

        return False
