class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''# move r to the right and lose from budget
            # if budget goes negative, 
            # try updating best so far
            # move l to the right to increase budget
            # problem: check for other letters to make the string
            # solution: heap to track the most common letter
            # budget = k - (heap - sub_len)
            # O(nlog26)
            # solution2: counter to track freqs
        '''
        freq = defaultdict(int)
        sub_len = 1
        l = r = 0
        best = 0
        best_freq = 0 # tracks the best freq we have ever seen
        while r < len(s):
            # print(l, r, end=" ")
            new_char = s[r]
            freq[new_char] += 1
            best_freq = max(best_freq, freq[new_char])
            budget = k + best_freq - sub_len
            # print(budget)
            if budget < 0:
                # shift window right to try find a new best_freq
                bye_char = s[l]
                freq[bye_char] -= 1
                l += 1
                sub_len -= 1
            else:  # valid substring
                best = max(best, sub_len)
            # budget = k + best_freq - sub_len
            r += 1
            sub_len += 1

        return best