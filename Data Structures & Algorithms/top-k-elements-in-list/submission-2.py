from collections import defaultdict, deque
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # element to freq (hash map) O(n) to make DS
        # freq to element (maybe heap? -> no log(n) time for 1 update) Max O(n) times to update this DS
        # return max of freq to element

        frequencies = defaultdict(int)
        for n in nums:
            frequencies[n] += 1
        
        # result = []
        # for uniq_n, freq in frequencies.items():
        #     heappush(result, (-freq, uniq_n))

        # return [heappop(result)[1] for i in range(k)]

        result = []
        for uniq_n, freq in frequencies.items():
            heappush(result, (freq, uniq_n))
            if len(result) > k:
                heappop(result)

        return [heappop(result)[1] for i in range(k)]
