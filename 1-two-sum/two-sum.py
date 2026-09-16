class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = len(sorted_nums) - 1
        
        while i < j:
            if sorted_nums[i] + sorted_nums[j] == target:
                first_index = nums.index(sorted_nums[i])
                second_index = nums.index(sorted_nums[j], first_index + 1) if sorted_nums[i] == sorted_nums[j] else nums.index(sorted_nums[j])
                return [first_index, second_index]
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                j -= 1