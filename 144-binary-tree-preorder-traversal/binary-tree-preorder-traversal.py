# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def preorderTraversal(self, root):
        stack = []
        ans = []
        curr = root

        while curr is not None or len(stack) > 0 :
            while curr is not None :
                ans.append(curr.val)
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            curr = node.right
        return ans
            

        
        
        