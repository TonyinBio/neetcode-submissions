class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        if sum(cost) > sum(gas): return -1

        test_start = 0
        i = 1
        budget = gas[0] - cost[0]
        while i != 0:
            if i == test_start:
                return test_start
            if budget < 0:
                budget = 0
                test_start = i
            budget += gas[i] - cost[i]
            i = (i + 1) % len(gas)

        return test_start if budget >= 0 else -1