class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = prices[0]
        max_profit = 0

        for price in prices: 
            if price < buying_price: 
                buying_price = price
                continue

            curr_profit = price - buying_price

            max_profit = max(curr_profit, max_profit)

        return max_profit
        
        