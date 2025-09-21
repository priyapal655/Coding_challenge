class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        profit = 0
        max_profit = 0
        for price in prices:
            if(buy_price > price):
                buy_price = price
            profit = price-buy_price
            if(max_profit < profit):
                max_profit = profit
        
        return max_profit
