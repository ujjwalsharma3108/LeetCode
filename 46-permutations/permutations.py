class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.getPermute(ans,0,nums)
        return ans
    def getPermute(self,ans,idx,nums):
        i = idx
        if i == len(nums):
            ans.append(nums.copy())
            return nums
        while i < len(nums):
            nums[i],nums[idx] = nums[idx],nums[i]
            self.getPermute(ans,idx+1,nums)
            nums[i],nums[idx] = nums[idx],nums[i]
            i+=1
        