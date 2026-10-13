from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = Counter(s1)
        # sub = defaultdict(int)
        m = len(s1)
        for r in range(m, len(s2) + 1):
            if s1_chars == Counter(s2[r - m:r]): 
                return True

        return False