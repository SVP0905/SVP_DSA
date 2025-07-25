class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails=[]
        for n in nums:
            l,r=0,len(tails)
            while l<r:
                mid=(l+r)//2
                if tails[mid]<n:
                    l=mid+1
                else:
                    r=mid
            
            if l==len(tails):
                tails.append(n)
            else:
                tails[l]=n
        
        return len(tails)