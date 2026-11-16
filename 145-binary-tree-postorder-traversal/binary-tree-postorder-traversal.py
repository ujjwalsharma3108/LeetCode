# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        
        stack = [root]
        ans = []
        while len(stack) > 0:
            node = stack.pop()
            ans.append(node.val)

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            
        return [i for i in reversed(ans)]