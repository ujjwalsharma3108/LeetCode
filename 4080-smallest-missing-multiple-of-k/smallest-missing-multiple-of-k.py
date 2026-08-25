class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1,102):
            if (k*i) in nums:
                continue 

            return i*k

