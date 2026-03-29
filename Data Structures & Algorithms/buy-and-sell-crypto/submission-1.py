class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy_at= 0
        sell_at= 1
        max_profit= 0

        while sell_at < len(prices):
            
            if prices[sell_at] > prices[buy_at]:
                max_profit= max(max_profit, prices[sell_at] - prices[buy_at])
            else:
                buy_at= sell_at
            
            sell_at += 1
        return max_profit

