class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l = i
            profit = prices[i] - prices[l]
            if profit > best:
                best = profit
            print(l)
        return best