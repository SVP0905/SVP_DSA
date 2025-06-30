class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter=Counter(nums)
        longest=0
        for num in nums:
            if num+1 in counter:
                longest=max(longest,counter[num+1]+counter[num])
        return longest