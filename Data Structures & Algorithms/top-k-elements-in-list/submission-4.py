from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for n, freq in freqs.items():
            buckets[freq].append(n)

        result = []
        highest_bucket = -1
        for i in range(k):
            found = False
            while not found:
                if len(buckets[highest_bucket]) != 0:
                    result.append(buckets[highest_bucket].pop())
                    found = True
                else:
                    highest_bucket -= 1

        return result