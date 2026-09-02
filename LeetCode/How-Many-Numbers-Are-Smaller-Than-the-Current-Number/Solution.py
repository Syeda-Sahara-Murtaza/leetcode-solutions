1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        sorted_nums = sorted(nums)
4        count = {} 
5        for i in range (len(sorted_nums)): 
6            if sorted_nums[i] not in count: 
7                count[sorted_nums[i]] = i
8        return [count[num] for num in nums] 