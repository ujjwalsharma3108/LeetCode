class Solution(object):
    def fib(self, n): 
        if n == 0  or n is None:
            return int(0)
        if n == 1:
            return int(1)
        if n >= 2:
            return self.fib(n-1) + self.fib(n-2)
        
        