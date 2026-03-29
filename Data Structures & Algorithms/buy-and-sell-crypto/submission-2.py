class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit= curr_profit= 0

        for i in range(len(prices)):
            buy= prices[i]
            for j in range(i+1, len(prices)):
                sell= prices[j]

                curr_profit= sell - buy
                max_profit= max(max_profit, curr_profit)


        return max_profit