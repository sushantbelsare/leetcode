import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            
            hash_map[num] += 1

        freq = []
        heapq.heapify(freq)

        for key, v in hash_map.items():
            heapq.heappush(freq, (-v, key))
        
        ans = []
        while k:
            ans.append(heapq.heappop(freq)[1])
            k -= 1

        return ans