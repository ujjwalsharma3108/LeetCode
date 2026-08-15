class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_ans = []
        ans = []
        def reoccurTask(nums,ans,i,all_ans):
            if i == len(nums):
                all_ans.append(ans.copy())
                return ans
            
            ans.append(nums[i])
            reoccurTask(nums,ans,i+1,all_ans)
            ans.pop()
            reoccurTask(nums,ans,i+1,all_ans)
        
        reoccurTask(nums,ans,0,all_ans)
        return all_ans