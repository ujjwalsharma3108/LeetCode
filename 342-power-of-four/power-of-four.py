class Solution(object):
    def isPowerOfFour(self, n):
        if n == -1 or n == 0:
            return False
        
        def recurTask(n):
            if n == 1:
                return True

            if n % 4 == 0:
               return recurTask(n/4)
            else:
                return False

        return recurTask(n)
        