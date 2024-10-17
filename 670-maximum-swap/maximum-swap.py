class Solution:
    #Test Case
    #   - Input: 2736   Output: 7236
    #   - Input: 1234   Output: 4231
    #   - Input: 4321   Output: 4321
    #   - Input: 1112   Output: 2111
    #   - Input: 432123 Output: 433122  
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        reversed_num_str = sorted(num_str, reverse=True)
        i = 0
        n = len(num_str)

        while i < n and num_str[i] == reversed_num_str[i]:
            i += 1

        if i < n:
            j = i + 1
            swap_index = 0
            while j < n:
                if num_str[j] == reversed_num_str[i]:
                    swap_index = j
                j += 1
            num_str[swap_index] = num_str[i]
            num_str[i] = reversed_num_str[i]
            return int(''.join(num_str))
        return num