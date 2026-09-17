from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_topk = []
        self.k = k
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        # print(self.min_topk, self.k)
        if len(self.min_topk) == self.k and val > self.min_topk[0]:
            heappop(self.min_topk)
            heappush(self.min_topk, val)
        elif len(self.min_topk) < self.k:
            heappush(self.min_topk, val)
        return self.min_topk[0]
