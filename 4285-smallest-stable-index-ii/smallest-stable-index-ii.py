class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_arr = [nums[-1]]*len(nums)
        i = len(nums)-2
        min_val = nums[-1]
        while i >= 0:
            if min_val > nums[i]:
                min_arr[i] = nums[i]
                min_val = nums[i]
            else:
                min_arr[i] = min_val
            i-=1
        max_val = nums[0]
        for i in range(len(nums)):
            if max_val < nums[i]:
                max_val = nums[i]

            if max_val - min_arr[i] <= k:
                return i 
        return -1