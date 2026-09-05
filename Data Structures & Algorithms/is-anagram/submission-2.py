class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts, t_counts = {}, {}
        if len(s) != len(t): return False
        length = len(s)
        for i in range(length):
            s_counts[s[i]] = 1 + s_counts.get(s[i], 0)
            t_counts[t[i]] = 1 + t_counts.get(t[i], 0)

        # if len(s_counts.keys()) != len(t_counts.keys()): return False
        # for s_key, s_num in s_counts.items():
        #     if t_counts.get(s_key, 0) != s_num: return False
        # return True
        return s_counts == t_counts

