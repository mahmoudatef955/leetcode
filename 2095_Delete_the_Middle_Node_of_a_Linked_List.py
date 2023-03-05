# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow, slow_prev = head, head, head

        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            slow_prev = slow_prev.next
            fast = fast.next.next

        if slow:
            slow_prev.next = slow.next
        else:
            head = None

        return head
