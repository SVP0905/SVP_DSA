class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=Counter(nums)
        for key,val in cnt.items():
            if val>math.floor(n//2):
                return key
            