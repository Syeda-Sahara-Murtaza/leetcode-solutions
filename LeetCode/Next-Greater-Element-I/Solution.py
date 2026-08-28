1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        ans = []
4        for i in range(len(nums1)):
5            found = False
6            for j in range(len(nums2)):
7                if nums1[i] == nums2[j]:
8                    for k in range(j + 1, len(nums2)):
9                        if nums2[k] > nums2[j]:
10                            ans.append(nums2[k])
11                            found = True
12                            break
13                    if not found:
14                        ans.append(-1)
15                    break
16        return ans
17        