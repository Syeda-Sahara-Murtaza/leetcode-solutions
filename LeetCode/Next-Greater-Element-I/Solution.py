1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        stack = []
4        greater = {}
5        for num in nums2:
6            while stack and stack[-1] < num:
7                greater[stack.pop()] = num
8            stack.append(num)
9        while stack:
10            greater[stack.pop()] = -1
11        return [greater[num] for num in nums1]
12        
13 
14        
15
16
17
18
19
20
21
22# class Solution:
23#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
24        # ans = []
25        # for i in range(len(nums1)):
26        #     found = False
27        #     for j in range(len(nums2)):
28        #         if nums1[i] == nums2[j]:
29        #             for k in range(j + 1, len(nums2)):
30        #                 if nums2[k] > nums2[j]:
31        #                     ans.append(nums2[k])
32        #                     found = True
33        #                     break
34        #             if not found:
35        #                 ans.append(-1)
36        #             break
37        # return ans