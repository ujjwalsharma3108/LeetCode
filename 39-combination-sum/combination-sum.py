class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        running = []
        def reoccurTask(ans,i,running,target):
            if sum(running) == target:
                ans.append(running.copy())
                return

            if sum(running) > target or i == len(candidates):
                return
            
            running.append(candidates[i])
            reoccurTask(ans,i,running,target)
            running.pop()
            reoccurTask(ans,i+1,running,target)

        reoccurTask(ans,0,running,target)

        return ans

