class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = n
        for i in range(n):
            ans ^= (nums[i] ^ i)
        return ans

            
        