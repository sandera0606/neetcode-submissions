class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, highest = 0, 0
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] > prices[highest]:
                highest = i
                maxProfit = max(prices[highest] - prices[lowest], maxProfit)
            elif prices[i] < prices[lowest]:
                lowest = i
                highest = i
        return maxProfit