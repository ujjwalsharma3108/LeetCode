class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ar = sorted(list(s))
        t_ar = sorted(list(t))
        return s_ar == t_ar