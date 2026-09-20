class Solution:
    def reverseDegree(self, s: str) -> int:
        s = list(s)
        sum = 0
        for i in range(len(s)):
            sum += (123 - ord(s[i])) * (i+1)
        return sum