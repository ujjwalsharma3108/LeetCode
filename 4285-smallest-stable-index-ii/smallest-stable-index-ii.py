class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_arr = [nums[-1]]*len(nums)
        i = 1
        while i < len(nums):
            if min_arr[len(nums)-i] > nums[len(nums)-i-1]:
                min_arr[len(nums)-i -1] = nums[len(nums)-i-1]
            else:
                min_arr[len(nums)-i-1] = min_arr[len(nums)-i]
            i+=1
        max_val = nums[0]
        for i in range(len(nums)):
            if max_val < nums[i]:
                max_val = nums[i]
                
            if max_val - min_arr[i] <= k:
                return i 
        return -1