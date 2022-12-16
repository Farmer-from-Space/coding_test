class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnum = 10000
        profit = 0

        for i in range(len(prices)):

            minnum = min(minnum, prices[i])
            profit = max(profit, prices[i] - minnum)
            
            
        return profit