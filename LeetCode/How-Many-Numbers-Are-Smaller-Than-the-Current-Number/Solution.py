1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        sorted_nums = sorted(nums)
4        ans = []
5        for num in nums:
6            ans.append(sorted_nums.index(num))
7        return ans
8        # sorted_nums = sorted(nums)
9        # count = {} 
10        # for i in range (len(sorted_nums)): 
11        #     if sorted_nums[i] not in count: 
12        #         count[sorted_nums[i]] = i
13        # return [count[num] for num in nums] 