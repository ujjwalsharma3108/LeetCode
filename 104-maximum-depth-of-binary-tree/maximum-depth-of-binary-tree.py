# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is not None:
            return self.depth(root)
        return 0

    def depth(self,node):
        ld = rd = 0
        if node.left is not None:
            ld = self.depth(node.left)
        
        if node.right is not None:
            rd = self.depth(node.right)
        
        return 1 + max(ld,rd)