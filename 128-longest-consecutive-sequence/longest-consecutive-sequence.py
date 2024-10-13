class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        longest_seq = 0

        a = set()

        for num in nums:
            a.add(num)

        for num in nums:
            if num - 1 not in a:
                h = num
                c = 1

                while h + 1 in a:
                    h += 1
                    c += 1

                longest_seq = max(longest_seq, c)
            

        return longest_seq