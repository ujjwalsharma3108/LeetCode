class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        new_ar1 = [nums[0]] 
        new_ar2 = [nums[1]]
        
        for i in range(2,len(nums)):
            if (new_ar1[-1] > new_ar2[-1]):
                new_ar1.append(nums[i])
            else:
                new_ar2.append(nums[i])
        return new_ar1+new_ar2
