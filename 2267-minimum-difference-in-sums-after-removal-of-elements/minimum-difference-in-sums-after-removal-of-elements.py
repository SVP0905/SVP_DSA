class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N=len(nums)
        n=N//3
        minheap=[]
        maxheap=[]
        leftMinSum=[0]*N
        rightMaxSum=[0]*N

        leftSum=0
        for i in range(N-n):
            heapq.heappush(maxheap,-nums[i])
            leftSum+=nums[i]
            if len(maxheap)>n:
                leftSum-=-heapq.heappop(maxheap)
            
        
            leftMinSum[i]=leftSum
        
        
        rightSum=0
        for i in range(N-1,n-1,-1):
            heapq.heappush(minheap,nums[i])
            rightSum+=nums[i]
            if len(minheap)>n:
                rightSum-=heapq.heappop(minheap)
            
            rightMaxSum[i]=rightSum
    
        
        print(leftMinSum)
        print(rightMaxSum)
        min_=float('inf')
        for i in range(n-1,2*n):
            min_= min(min_,leftMinSum[i]-rightMaxSum[i+1])
        
        return min_
                