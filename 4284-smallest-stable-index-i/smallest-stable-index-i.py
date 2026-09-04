class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_index = len(nums)
        mv = k

        for i in range(len(nums)):
            max_val = max(nums[:i+1])
            min_val = min(nums[i:])

            if max_val - min_val <= mv:
                min_index = i if min_index > i else min_index
                return min_index

        return -1

        