class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, highest = prices[0], prices[0]
        maxProfit = 0

        for price in prices:
            if price < lowest:
                lowest = price
                highest = price
            elif price > highest:
                highest = price
                maxProfit = max(maxProfit, highest - lowest)
        return maxProfit