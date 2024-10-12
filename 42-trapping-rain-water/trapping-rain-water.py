class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_left, max_right = height[i], height[j]
        res = 0
        while i < j:
            ans = 0
            if max_left < max_right:
                i += 1
                ans += min(max_left, max_right) - height[i]
                max_left = max(max_left, height[i])
            else:
                j -= 1
                ans += min(max_left, max_right) - height[j]
                max_right = max(max_right, height[j])

            if ans > 0:
                res += ans
        
        return res