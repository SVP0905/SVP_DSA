class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        N=len(nums)
        for i in range(N):
            if i>0 and nums[i]==nums[i-1]:
                continue

            l,r=i+1,N-1

            while l<r:
                triplet_sum=nums[i]+nums[l]+nums[r]

                if triplet_sum==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif triplet_sum<0:
                    l+=1
                else:
                    r-=1
        return res
                    
        