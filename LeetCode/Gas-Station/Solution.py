1class Solution:
2    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
3        total = 0
4        tank = 0
5        start = 0
6        for i in range(len(gas)):
7            total += gas[i] - cost[i]
8            tank += gas[i] - cost[i]
9            if tank < 0:
10                start = i + 1
11                tank = 0
12        if total < 0:
13            return -1
14        return start