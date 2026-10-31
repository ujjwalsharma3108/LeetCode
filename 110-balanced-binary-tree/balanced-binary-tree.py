# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        val = self.check_h(root)
        if val == -1:
            return False
        return True
        

        

    def check_h(self,node):

        if node.left is not None:
            lft_ht = self.check_h(node.left)

        if node.right is not None:
            rgt_ht = self.check_h(node.right)
            
        if node.left is None:
            lft_ht = 0
        if node.right is None:
            rgt_ht = 0

        if (lft_ht == -1 or rgt_ht == -1):
            return -1


        if abs(lft_ht - rgt_ht) > 1:
            return -1

        return 1 + max(lft_ht,rgt_ht)
        

        


