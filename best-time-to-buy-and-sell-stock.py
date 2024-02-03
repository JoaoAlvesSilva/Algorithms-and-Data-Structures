// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        least = prices[0]

        for price in prices:
            if price < least : 
                least = price
            elif price - least > profit:
                profit = price - least
        return profit
        