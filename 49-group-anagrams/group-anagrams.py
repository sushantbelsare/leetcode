class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        group = []
        for word in strs:
            key = "".join(sorted(word))
            if key not in hash_map:
                hash_map[key] = len(group)
                group.append([word])
            else:
                group[hash_map[key]].append(word)

        return group
