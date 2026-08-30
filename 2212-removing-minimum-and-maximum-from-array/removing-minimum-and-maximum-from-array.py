class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_ind = 0
        max_ind = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_ind] :
                max_ind = i
            if nums[i] < nums[min_ind] :
                min_ind = i
        left = min(min_ind, max_ind)
        right = max(min_ind, max_ind)
        n = len(nums)
        
        mixed_cost = (left + 1) + (n - right)
        right_cost = n - left
        left_cost  = right +1
        return min(left_cost, right_cost, mixed_cost) 
        
        