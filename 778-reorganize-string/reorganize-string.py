import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        fmap = Counter(s)

        freq_heap = []
        heapq.heapify(freq_heap)

        for k, v in fmap.items():
            heapq.heappush(freq_heap, (-v, k))

        ans = ""
        while freq_heap:
            k, v = heapq.heappop(freq_heap)
            if ans and ans[-1] == v:
                if freq_heap:
                    prev = (k, v)
                    k, v = heapq.heappop(freq_heap)
                    heapq.heappush(freq_heap, prev)
                else:
                    return ""
            ans += v
            k += 1
            if k < 0:
                heapq.heappush(freq_heap, (k, v))

        return ans