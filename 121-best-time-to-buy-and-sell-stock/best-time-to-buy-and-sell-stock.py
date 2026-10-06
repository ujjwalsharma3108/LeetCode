class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        diff = 0
        for i in prices:
            if i < min :
                min = i
            elif diff < (i - min):
                diff = i - min
        return diff
