from collections import deque

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        queue = deque()
        groups = 0
        max_groups = len(hand) // groupSize
        if max_groups != len(hand) / groupSize: return False

        # print(sorted(hand))
        for num in sorted(hand):
            # print(num, queue, end=" ")
            if queue and num > queue[0][0]:
                # print("A")
                return False
            # use the number to grow a group
            if queue and queue[0][0] == num:
                # print("B")
                val, lifespan = queue.popleft()
                val += 1
                lifespan -= 1
                if lifespan > 0:
                    queue.append((val, lifespan))
            # new group
            else:  
                # print("C")
                groups += 1
                if groups > max_groups:
                    return False
                if groupSize > 1:
                    queue.append((num + 1, groupSize - 1))
                
        return True