# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer, fast_pointer = head, head
        slow_pointer_count = 0
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            slow_pointer_count += 1
            if slow_pointer == fast_pointer:
                current = head
                nodes = {head}
                while True:
                    slow_pointer = slow_pointer.next
                    if slow_pointer in nodes:
                        return slow_pointer
                    current = current.next
                    nodes.add(current)

        return None
