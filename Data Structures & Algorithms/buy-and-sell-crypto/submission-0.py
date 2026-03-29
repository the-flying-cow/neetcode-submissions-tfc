class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit= 0

        for i in range(len(prices)):
            buy_at= prices[i]
            for j in range(i+1, len(prices)):
                sell_at= prices[j]
                current_profit= sell_at - buy_at
                
                max_profit= max(current_profit, max_profit)


        return max_profit
