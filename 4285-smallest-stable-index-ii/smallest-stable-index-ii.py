class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_arr = [nums[0]]*len(nums)
        min_arr = [nums[-1]]*len(nums)
        i = 1
        while i < len(nums):
            if max_arr[i-1] < nums[i]:
                max_arr[i] = nums[i]
            else:
                max_arr[i] = max_arr[i-1]
            if min_arr[len(nums)-i] > nums[len(nums)-i-1]:
                min_arr[len(nums)-i -1] = nums[len(nums)-i-1]
            else:
                min_arr[len(nums)-i-1] = min_arr[len(nums)-i]
            i+=1

        for i in range(len(nums)):
            if max_arr[i] - min_arr[i] <= k:
                return i 
        return -1