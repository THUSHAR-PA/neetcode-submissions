class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = float("-inf")
        for i in prices:
            if i < min_price:
                min_price = i
            profit = i - min_price
            if profit > max_price:
                max_price = profit
        return max_price