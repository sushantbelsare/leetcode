class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = nums[0]
        n = len(nums)
        if fuel == 0 and n > 1:
            return False

        for i in range(1, n):
            if nums[i] >= fuel:
                fuel = nums[i]
            else:
                fuel -= 1
                if nums[i] == fuel == 0:
                    return i == n - 1

        return True
