class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        sub_len = 0
        result = 0
        l = 0
        for r in range(len(s)):
            # print(s[r], sub_len, seen)
            result = max(result, sub_len)
            sub_len += 1
            if s[r] in seen:
                while s[l] != s[r] and sub_len > 0:
                    # print("   ", s[l], seen)
                    seen.remove(s[l])
                    sub_len -= 1
                    l += 1
                sub_len -= 1
                l += 1
            seen.add(s[r])
        return max(result, sub_len)