# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        len= 0
        temp= head
        while temp:
            len+=1
            temp= temp.next

        n_from_start= len - n + 1
        if n_from_start == 1:
            head= head.next
            return head
            
        p, q= head, None
        while n_from_start != 1:
            q= p
            p= p.next
            n_from_start-=1

        q.next= p.next

        return head

