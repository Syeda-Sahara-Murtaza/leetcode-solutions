1# class Solution:
2#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        # n = len(nums)
4        # result = [-1] * n
5        # stack = []
6        # for i in range(2 * n):
7        #     while stack and nums[stack[-1]] < nums[i % n]:
8        #         result[stack.pop()] = nums[i % n]
9        #     if i < n:
10        #         stack.append(i)
11        # return result
12class Solution:
13    def nextGreaterElements(self, nums: List[int]) -> List[int]:
14        n = len(nums)
15        result = [-1] * n
16        stack = []
17        for i in range(n):
18            stack.append(i)
19        while stack:
20            i = stack.pop()
21            for j in range(1, n):
22                next_index = (i + j) % n
23                if nums[next_index] > nums[i]:#here we check values
24                    result[i] = nums[next_index]
25                    break
26        return result