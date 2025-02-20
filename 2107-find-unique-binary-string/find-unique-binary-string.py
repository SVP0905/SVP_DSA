class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        res=[]
        for i in range(n):
            str_=nums[i][i]
            res.append('1' if str_=='0' else '0')
        
        return ''.join(res)