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
        if not head:
            return None

        mapping = {}

        # First pass: create copy nodes
        curr = head

        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: connect next and random
        curr = head

        while curr:
            mapping[curr].next = mapping.get(curr.next)
            mapping[curr].random = mapping.get(curr.random)
            curr = curr.next

        return mapping[head]
                
        
        