class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toFrequencies(string):
            counts = [0 for i in range(26)]
            # counts = {}
            for s in string:
                idx = ord(s) - ord("a")
                counts[idx] += 1
            return tuple(counts)
        
        groups = []
        ids = {}
        for string in strs:
            str_counts = toFrequencies(string)
            if str_counts in ids:
                idx = ids[str_counts]
                groups[idx].append(string)
            else:
                ids[str_counts] = len(groups)
                groups.append([string])
                
        return groups