# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        if list1 != None:
            p= list1
        else:
            return list2

        if list2 != None:
            q= list2
        else:
            return list1
        head= None

        

        while (p != None and q != None):

            if p.val <= q.val:
                if head == None:
                    head= p
                temp= p
                p= p.next
                if p and p.val <= q.val:
                    temp.next= p
                else:
                    temp.next= q

            else:
                if head == None:
                    head= q
                temp= q
                q= q.next
                if q and q.val < p.val:
                    temp.next= q
                else:
                    temp.next= p

        return head
