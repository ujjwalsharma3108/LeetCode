# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        def subTree(arr):
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            if len(arr[:mid]) > 0: 
                node.left = subTree(arr[:mid])
            if len(arr[mid+1:]) > 0: 
                node.right = subTree(arr[mid+1:])
            return node     
        return subTree(nums)   