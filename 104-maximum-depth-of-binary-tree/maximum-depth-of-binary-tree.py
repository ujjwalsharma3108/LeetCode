# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # 1. Base case
        if root is None:
            return 0

        # 2. Solve left
        left = self.maxDepth(root.left)

        # 3. Solve right
        right = self.maxDepth(root.right)

        # 4. Combine
        return 1 + max(left, right)