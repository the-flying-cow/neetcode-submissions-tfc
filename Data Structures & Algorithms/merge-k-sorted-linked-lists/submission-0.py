# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # if array is only empty, return [] list
        
        if len(lists) == 0:
            return None

        merged = ListNode()
        tail = merged

        while True:

            min_val = float('inf')
            min_i = -1

            for i in range(len(lists)):
                if lists[i] != None and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_i = i

            if min_i == -1:
                break

            tail.next = lists[min_i]
            tail = tail.next

            lists[min_i] = lists[min_i].next

        return merged.next