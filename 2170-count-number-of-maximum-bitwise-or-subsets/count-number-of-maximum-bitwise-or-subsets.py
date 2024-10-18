class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_num = 0

        for num in nums:
            max_num = max_num | num

        counter = 0
        memo = {}

        def count(i, n):
            nonlocal max_num
            nonlocal counter
            res = [nums[i]]

            if i in memo:
                return memo[i]

            if res[-1] == max_num:
                counter += 1

            if i == n - 1:
                memo[i] = res
                return memo[i]
            
            for j in range(i + 1, n):
                temp_res = []
                for k in count(j, n):
                    res.append(nums[i] | k)
                    if res[-1] == max_num:
                        counter += 1

                res += temp_res

            memo[i] = res
                
            return memo[i]

        count(0, len(nums))
        return counter