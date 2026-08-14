class Solution(object):
    def climbStairs(self, n):
        memo = {}
        def reoccurTask(n):
            if n == 1 or n ==2 :
                return n

            if n in memo:
                return memo[n]
            else:
                #memorization:
                memo[n] = reoccurTask(n-1) + reoccurTask(n-2)
                return memo[n]
        return reoccurTask(n)
        