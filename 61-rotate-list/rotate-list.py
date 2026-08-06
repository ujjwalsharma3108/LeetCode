# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        B = A = head

        if head is None:
            return head
        c = 1
        h = k
        while h > 0:
            if B.next is None:
                B = head
                h = (k % c)  +1
            else :
                c += 1
                B = B.next
            h-=1
        
        while B.next is not None :
            B = B.next 
            A = A.next 

        B.next = head
        head = A.next
        A.next = None

        return head

        
        