class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum([i+1 for i in range(len(nums))]) -sum(nums) 


            
        