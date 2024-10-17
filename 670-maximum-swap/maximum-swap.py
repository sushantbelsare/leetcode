class Solution:
    #Test Case
    #   - Input: 2736   Output: 7236
    #   - Input: 1234   Output: 4231
    #   - Input: 4321   Output: 4321
    #   - Input: 1112   Output: 2111
    #   - Input: 432123 Output: 433122  
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        length = len(num_str)
        for i, (m, n) in enumerate(zip(num_str, sorted(num_str, reverse=True))):
            if m != n:
                j = length - 1
                while j >= 0 and num_str[j] != n:
                    j -= 1
                num_str = num_str[:j] + m + num_str[j + 1:]
                num_str = num_str[:i] + n + num_str[i + 1:]
                return int(''.join(num_str))
        return num