# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        arrA = []
        arrB = []

        def inOT(node,ans):
            ans.append(node.val)

            if node.left is not None:
                inOT(node.left,ans)
            else:
                ans.append(None)

            if node.right is not None:
                inOT(node.right,ans)
            else:
                ans.append(None)

            return 
        
        if p is not None:
            inOT(p,arrA)

        if q is not None:
            inOT(q,arrB)
        
        if arrA == arrB:
            return True
        return False

            