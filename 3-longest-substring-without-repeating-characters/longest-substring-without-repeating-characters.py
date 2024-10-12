class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hash_map = {}
        max_len = 0
        repeated_indexes = deque()
        for index, c in enumerate(s):
            if c in hash_map:
                max_len = max(max_len, index - repeated_indexes[0])
                while repeated_indexes and s[repeated_indexes[0]] != c:
                    del hash_map[s[repeated_indexes.popleft()]]
                if repeated_indexes and s[repeated_indexes[0]] == c:
                    del hash_map[s[repeated_indexes.popleft()]]
            
            hash_map[c] = index
            repeated_indexes.append(index)

        return max(max_len, len(s) - repeated_indexes[0])