import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # n log max(b)
        l = 1
        r = max(piles)
        best_k = max(piles)
        while r >= l:
            k = (l + r) // 2

            # calculate num hours to eat piles
            time = 0 
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k)
                if time > h: break
            
            # print(k, l , r)
            # change bounds
            if time <= h:  # too fast, k be lower
                best_k = k
                r = k - 1
            elif time > h:
                l = k + 1
        # print(time)
        return best_k