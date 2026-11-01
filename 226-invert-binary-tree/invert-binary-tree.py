# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        return self.invertNode(root)    

    def invertNode(self,node):
        lt = None
        rt = None
        if node is None :
            return node

        if node.left is not None:
            lt = node.left 

        if node.right is not None:
            rt = node.right
        
        node.right = lt
        node.left  = rt

        if node.left is not None:
            self.invertNode(node.left)
        
        if node.right is not None:
            self.invertNode(node.right)
        
        return node
