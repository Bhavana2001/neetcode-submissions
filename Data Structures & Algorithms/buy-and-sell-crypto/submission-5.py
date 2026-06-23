class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]

        for i in prices:
            if i < min_price:
                min_price = i
            profit = i - min_price
            if profit > result:
                result = profit
        
        return result

        '''max = 0
        buyIn = 0
        sellIn = buyIn + 1

        while sellIn < len(prices):
            #print("buy index:", buyIn)
            #print("sell index:", sellIn)
            if prices[buyIn] > prices[sellIn]:
                buyIn = sellIn
            elif prices[sellIn] - prices[buyIn] > max:
                max = prices[sellIn] - prices[buyIn]
            sellIn += 1

        return max'''