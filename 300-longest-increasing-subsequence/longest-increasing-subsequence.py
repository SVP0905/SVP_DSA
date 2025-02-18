class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def binarySearch(subseq,target,size):
            left,right=0,size
            while left<right:
                mid=(left+right)//2
                if subseq[mid]<target:
                    left=mid+1
                else:
                    right=mid
            return left
        
        if not nums:
            return 0
        
        subseq=[0]*len(nums)
        size=0

        subseq[0]=nums[0]
        size=1

        for num in nums[1:]:
            if num<subseq[0]:
                subseq[0]=num
            elif num>subseq[size-1]:
                subseq[size]=num
                size+=1
            else:
                pos=binarySearch(subseq,num,size)
                subseq[pos]=num
        
        return size

            