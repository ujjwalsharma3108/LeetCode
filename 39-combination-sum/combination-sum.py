class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        running = []
        def backtrack(i, curr_sum):
            if curr_sum == target:
                ans.append(running.copy())
                return

            if curr_sum > target or i == len(candidates):
                return

            running.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            running.pop()

            backtrack(i + 1, curr_sum)
        backtrack(0, 0)
        return ans

