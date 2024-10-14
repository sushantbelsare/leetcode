class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        k = 0
        for i in range(1, n):
            dp[i + 1] = max(dp[i], prices[i] - prices[k])
            if prices[i] < prices[k]:
                k = i
        return dp[n]