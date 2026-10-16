class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b = 0, 1
        maxb = 0

        while b < len(prices):
            if prices[a] < prices[b]:
                profit = prices[b] - prices[a]
                maxb = max(maxb, profit)
            else:
                a = b
            b +=1
        return maxb


        