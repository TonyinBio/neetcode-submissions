class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(numbers):
            if num in complement:
                return [complement[num], i + 1]
            complement[target - num] = i + 1
        