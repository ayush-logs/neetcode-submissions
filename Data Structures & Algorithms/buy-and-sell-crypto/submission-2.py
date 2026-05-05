class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        res = 0

        for i in range(len(prices)): 
            if prices[i] < bp:
                bp = prices[i]
                continue
            else: 
                curr_profit = prices[i] - bp
                res = max(curr_profit, res)

        
        return res

        
        