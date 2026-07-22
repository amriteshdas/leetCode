class Solution(object):
    def maxProfit(self, prices):
        min_prices = prices[0]
        max_profit = 0
        for price in prices:
            if min_prices > price:
                min_prices = price
            profit = price - min_prices
            if profit > max_profit:
                max_profit=profit
        return max_profit

        