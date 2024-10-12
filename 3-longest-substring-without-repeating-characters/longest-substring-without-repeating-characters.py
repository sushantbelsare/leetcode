class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        hash_map = {}
        max_len = 0
        last_repeated = -1
        for index, c in enumerate(s):
            if c in hash_map:
                max_len = max(max_len, index - last_repeated)
                while last_repeated < n and s[last_repeated] != c:
                    del hash_map[s[last_repeated]]
                    last_repeated += 1
                if last_repeated < n:
                    del hash_map[s[last_repeated]]
                    last_repeated += 1
            
            hash_map[c] = index
            if last_repeated == -1:
                last_repeated = index

        return max(max_len, len(s) - last_repeated)