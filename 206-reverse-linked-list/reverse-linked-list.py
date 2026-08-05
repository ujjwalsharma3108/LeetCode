# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None :
            return head 
        
        pre = None
        curr = head 
        nxt = head.next

        while curr is not None :
            if pre is None:
                curr.next = None
            else:
                curr.next = pre
            
            # update
            pre = curr
            if nxt is not None:
                curr = nxt
                nxt  = nxt.next
            else:
                head = curr
                curr = None

        return head

        