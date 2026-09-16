1from collections import deque
2class Solution:
3    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
4        dq = deque()#[1,2]   # stores indexes
5        result = []
6        for i in range(len(nums)):
7            #Remove indexes that are outside the window
8            if dq and dq[0] < i - k + 1:
9                dq.popleft()
10            #Remove smaller elements from the back
11            while dq and nums[dq[-1]] < nums[i]:#values on these indexes
12                dq.pop()
13            #Add current index
14            dq.append(i)
15            #Once first window is complete, add maximum
16            if i >= k - 1:
17                result.append(nums[dq[0]])
18        return result
19
20
21
22
23
24# class Solution:
25#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
26#         result = []
27#         for i in range(len(nums) - k + 1):
28#             window = nums[i:i+k]
29#             result.append(max(window))
30#         return result