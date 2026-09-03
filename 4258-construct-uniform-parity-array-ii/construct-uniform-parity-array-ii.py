class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        is_odd = False
        if nums1[0] % 2 != 0 :
            is_odd = True
        
        for i in nums1:
            if is_odd == False and i%2 != 0:
                return False

        return True

        
        
