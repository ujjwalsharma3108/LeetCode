class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        while n > 0:
            hw += n & 1
            n >>=1
        return hw