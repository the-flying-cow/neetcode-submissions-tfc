class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell= 0, 1
        curr_profit= 0
        max_profit= 0
        while sell < len(prices):

            if prices[buy] < prices[sell]:
                profit= prices[sell] - prices[buy]
                max_profit= max(profit, max_profit)
                sell+= 1

            else:
                buy= sell
                sell+= 1

        return max_profit