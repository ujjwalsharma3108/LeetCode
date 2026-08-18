class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = 0
        s1_ar = list(s1)
        s1_ar.sort()
        s2_ar = list(s2)
        while a <= len(s2)-len(s1):
            s2_sorted_ar = s2_ar[a:a + len(s1)]
            s2_sorted_ar.sort()
            if s2_sorted_ar == s1_ar:
                return True
            a+=1
        return False