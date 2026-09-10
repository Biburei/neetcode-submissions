class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]

        for i in range(1, len(prices), 1):
            if prices[i] < minimum:
                minimum = prices[i]
            difference = prices[i] - minimum
            if difference > profit:
                profit = difference
        if profit < 0:
            return 0
        return profit
