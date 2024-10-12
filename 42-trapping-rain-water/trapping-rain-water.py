class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        dp = [-1 for _ in range(n)]
        collection = 0
        for i in range(1, n):
            if height[i-1] > height[i]:
                dp[i] = i - 1
            elif height[i-1] < height[i]:
                j = dp[i-1]
                k = i - 1
                dp[i] = -1
                while j != -1:
                    window = i - j - 1
                    collection += ((min(height[j], height[i]) - height[k]) * window)
                    if height[j] > height[i]:
                        dp[i] = j
                        break
                    k = j
                    j = dp[j]
            else:
                dp[i] = dp[i-1]
        return collection