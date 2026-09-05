class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        i = 0
        while i < len(nums):
            if max(nums[:i+1]) - min(nums[i:]) <= k:   
                return i
            i+=1
        return -1

        