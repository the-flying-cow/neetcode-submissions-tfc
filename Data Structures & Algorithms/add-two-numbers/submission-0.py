# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry= 0
        temp1, temp2= l1, l2

    # resulting list
        res= ListNode()
        temp3= res

        while temp1 or temp2 or carry:
            val1= temp1.val if temp1 else 0
            val2= temp2.val if temp2 else 0
            
            sum= val1 + val2 + carry
            carry= sum // 10

            temp3.next= ListNode(sum % 10)
            
            temp3= temp3.next
            temp1= temp1.next if temp1 else None
            temp2= temp2.next if temp2 else None
            
        return res.next
