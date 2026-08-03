# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        pre     = None 
        first   = head
        second  = head.next
        third   = None
        while first is not None and second is not None:
            third = second.next

            second.next = first
            first.next = third
            if pre is None:
                head = second
            else:
                pre.next = second
            # //update
            pre = first
            first = third
            if third is not None:
                second = third.next
            else:
                second = None 

        return head

            

            





            





            

        
            
        


