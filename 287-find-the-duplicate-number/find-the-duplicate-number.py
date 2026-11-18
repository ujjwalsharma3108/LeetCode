class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        i = 0
        while i >= 0 :
            if nums[i] > 0:
                nums[i] = -1 * nums[i]
                i = -1 * nums[i]
                continue
            return i
