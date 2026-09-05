class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if seen.get(n) is not None:
                return True
            seen[n] = True
        return False