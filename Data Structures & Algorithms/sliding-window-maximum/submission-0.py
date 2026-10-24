import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        maxes.append(-heap[0][0])
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            # print(r, heap)
            while heap[0][1] <= r - k:
                heapq.heappop(heap)

            maxes.append(-heap[0][0])

        return maxes