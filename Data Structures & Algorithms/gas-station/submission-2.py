class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if len(gas) == 1:
        #     return 0 if gas[0] >= cost[0] else -1
        if sum(cost) > sum(gas): return -1

        test_start = 0
        budget = 0
        for i in range(len(gas)):
            if budget < 0:
                budget = 0
                test_start = i
            budget += gas[i] - cost[i]
        return test_start