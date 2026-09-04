class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_index = len(nums)
        mv = k

        for i in range(len(nums)):
            max_val = max(nums[:i+1])
            min_val = min(nums[i:])

            if max_val - min_val <= mv:
                
                return i

        return -1

        