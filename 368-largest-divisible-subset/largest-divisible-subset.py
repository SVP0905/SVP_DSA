class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        n=len(nums)
        nums.sort()
        dp=[1]*n
        prev_ele=[-1]*n
        max_=0
        max_idx=-1
        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    prev_ele[i]=j
            
            if dp[i]>max_:
                max_=dp[i]
                max_idx=i
        
        res=[]
        cur_idx=max_idx
        while cur_idx!=-1:
            res.append(nums[cur_idx])
            cur_idx=prev_ele[cur_idx]
        
        return res[::-1]
