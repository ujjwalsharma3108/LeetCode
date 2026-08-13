class Solution(object):
    def fib(self, n):
        memo = {i: 0 for i in range(2, n + 1)}

        def series(n):
            if (n == 0 or n == 1):
                return n
            
            if memo[n] != 0 :
                return memo[n]
            
            else:
                val1 = series(n-1)
                val2 = series(n-2)
                memo[n-1] = val1
                memo[n-2] = val2
                return val1 + val2
        return series(n)

        
        