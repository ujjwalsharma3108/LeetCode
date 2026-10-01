# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []
        def orderLevelTraversal(queue):
            if len(queue) == 0:
                return 
                
            n = len(queue)
            while n > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

                n -= 1
            ans.append(node.val)

            orderLevelTraversal(queue)
        
        if root is not None:
            orderLevelTraversal([root])
        return ans
        
            



