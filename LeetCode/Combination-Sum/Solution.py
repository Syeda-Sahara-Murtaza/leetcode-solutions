1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        ans = []
4        path = []
5        def backtrack(i, target):
6            if target == 0:
7                ans.append(path[:])
8                return
9            if target < 0:
10                return
11            if i == len(candidates):
12                return
13            # Take
14            path.append(candidates[i])
15            backtrack(i, target - candidates[i])
16            path.pop()
17            # Skip
18            backtrack(i + 1, target)
19        backtrack(0, target)
20        return ans