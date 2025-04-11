class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of the overall min, and always compare the curr sell price
        # to that min buy price. update both buy and sell regardless each time.
        
        buy, sell = 0, 1
        maxProfit = 0
        minBuy = float('inf')

        while sell < len(prices):
            minBuy = min(minBuy, prices[buy])
            maxProfit = max(maxProfit, prices[sell] - minBuy)

            buy += 1
            sell += 1

        return maxProfit


        