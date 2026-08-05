# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if head is None or head.next is None :
            return head

        A = B = head
        while B is not None and B.next is not None :
            A = A.next
            B = B.next.next
        
        return A
        