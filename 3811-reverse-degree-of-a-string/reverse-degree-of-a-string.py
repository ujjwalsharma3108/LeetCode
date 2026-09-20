class Solution:
    def reverseDegree(self, s: str) -> int:
        s = list(s)
        sum = 0
        for i in range(len(s)):
            ind_val = 27 - (ord(s[i]) - 96)
            sum += ind_val * (i+1)
        return sum