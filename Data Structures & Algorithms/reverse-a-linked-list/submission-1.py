# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, q= None, head

        while q:
            next= q.next
            q.next= p
            p= q
            q= next

        head= p

        return head