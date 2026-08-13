class Solution(object):
    def fib(self, n):
        memo = {}

        def series(n):
            if (n == 0 or n == 1):
                return n
            
            if n in memo :
                return memo[n]
            
            else:
                memo[n] = series(n - 1) + series(n - 2)
                return memo[n]
        return series(n)

        
        