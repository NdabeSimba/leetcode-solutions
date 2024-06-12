# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head.next
        slow = head

        # iterate through the ListNode

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
