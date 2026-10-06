class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        diff = 0
        hold_day = 0

        for i in range(len(prices)-1):
            if hold_day == 0 and prices[i] < prices[i+1]:
                hold_day = i+1
            elif hold_day != 0 and prices[i] > prices[i+1]:
                diff += prices[i] - prices[hold_day-1]
                hold_day = 0
        
        if hold_day != 0 and prices[-1] > prices[hold_day - 1]:
            diff+= prices[-1] - prices[hold_day - 1] 
        return diff