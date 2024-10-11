import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = (left  + right) // 2
            h = sum((pile + mid - 1)//mid for pile in piles)
            if h <= H:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            