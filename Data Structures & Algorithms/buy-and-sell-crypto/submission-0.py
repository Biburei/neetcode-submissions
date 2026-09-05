class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            total = prices[i] - min_value
            if total > max_profit:
                max_profit = total
        return max_profit

