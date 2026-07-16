class Solution:
    def findGCD(self,a,b):
        if b==0:
            return a
        else:
            return self.findGCD(b,a%b)

    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        prefixGCD=[0]*n
        mxi=float("-inf")
        for i in range(n):
            mxi=max(mxi,nums[i])
            prefixGCD[i]=self.findGCD(nums[i],mxi)
        
        prefixGCD=sorted(prefixGCD)
        print(prefixGCD)
        l,r=0,n-1
        sum_=0
        while l<r:
            sum_+=self.findGCD(prefixGCD[l],prefixGCD[r])
            l+=1
            r-=1

        return sum_

        