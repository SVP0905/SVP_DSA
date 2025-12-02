class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        distinct_elements=set(nums)
        MEX=1
        while MEX in distinct_elements:
            MEX+=1
        
        return MEX