class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # ========== Negative Marking Approach ====================
        # i = 0
        # while i >= 0 :
        #     if nums[i] > 0:
        #         nums[i] = -1 * nums[i]
        #         i = -1 * nums[i]
        #         continue
        #     return i

        # ========== Floyd's Tortoise and Hare (Cycle Detection) ===

        # Phase 1: Find the intersection point of the two runners
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
