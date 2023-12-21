# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        curr = head

        if not curr:
            return head
        else:
            while curr.next:
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            
            return head


self = Solution()

head = [1,1,2]
print(Solution.deleteDuplicates(self, head))

head = [1,1,2,3,3]
print(Solution.deleteDuplicates(self, head))