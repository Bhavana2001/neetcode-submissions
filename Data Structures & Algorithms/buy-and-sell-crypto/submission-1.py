class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        buyIn = 0
        sellIn = buyIn + 1

        while sellIn < len(prices):
            print("buy index:", buyIn)
            print("sell index:", sellIn)
            if prices[buyIn] > prices[sellIn]:
                buyIn = sellIn
            elif prices[sellIn] - prices[buyIn] > max:
                max = prices[sellIn] - prices[buyIn]
            sellIn += 1

        return max