class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum_arr = 0
        for i in range(n):
            sum_arr += i+1
        return sum_arr -sum(nums) 


            
        