class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        while n > 1:
            if n % 2 != 0:
                hw +=1
                n = n//2
            else:
                n = n/2
                
        if n == 1:
            hw +=1
        return hw