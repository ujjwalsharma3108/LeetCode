class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = nums[0]
        for i in nums[1:]:
            a = a ^ i
        return a