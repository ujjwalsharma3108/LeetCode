"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        curr = None
        new_head = None
        old_head = head
        while head is not None:
            node = Node(head.val)
            head = head.next
            if curr is None:
                curr = node
                new_head = node
            else:
                curr.next = node
                curr = curr.next
        new_head1 = new_head
        old_head1 = old_head
        
        while old_head1 is not None:
            curr1 = old_head
            new_curr1 = new_head
            if curr1.random is None:
                new_head1.random = None

            while curr1 is not None:
                if old_head1.random is curr1:
                    new_head1.random = new_curr1
                elif old_head1.random is None:
                    new_head1.random 
                curr1 = curr1.next
                new_curr1 = new_curr1.next


            old_head1 = old_head1.next 
            new_head1 = new_head1.next 

        return new_head
                
        
        