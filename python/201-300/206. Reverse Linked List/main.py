# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_list = None

        while curr:
            next_node = curr.next
            curr.next = new_list
            new_list = next_node
        
        return new_list