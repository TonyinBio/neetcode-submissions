from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = Counter(s1)
        counts2 = defaultdict(int)
        m = len(s1)
        for c in s2[:m]:
            counts2[c] += 1
            if s1_chars == counts2: return True
        for r in range(m + 1, len(s2) + 1):
            l = r - m
            counts2[s2[l - 1]] -= 1
            counts2[s2[r - 1]] += 1
            if counts2[s2[l - 1]] == 0: 
                counts2.pop(s2[l - 1])
            print(counts2)
            if s1_chars == counts2: 
                return True

        return False