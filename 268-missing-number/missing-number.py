class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) 
        nums.sort()
        def checkMissing(start,end,arr) :
            if start == end:
                return start
            mid = (start+end) // 2
            if mid == nums[mid]: 
                return checkMissing(mid+1,end,arr)
            else: 
                return checkMissing(start,mid,arr)
        return checkMissing(0,n,nums)

            
        