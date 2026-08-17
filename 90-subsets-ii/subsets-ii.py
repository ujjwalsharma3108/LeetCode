class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        return_arr = []
        nums.sort()
        def reoccurTask(nums,ans,i,return_arr):
            if i == len(nums) :
                return_arr.append(ans.copy())
                return ans
            ans.append(nums[i])
            reoccurTask(nums,ans,i+1,return_arr)
            ans.pop()
            idx = i+1
            while idx < len(nums) and nums[idx] == nums[idx-1]:
                idx+=1    
            reoccurTask(nums,ans,idx,return_arr)
        
        reoccurTask(nums,ans,0,return_arr)
        return return_arr