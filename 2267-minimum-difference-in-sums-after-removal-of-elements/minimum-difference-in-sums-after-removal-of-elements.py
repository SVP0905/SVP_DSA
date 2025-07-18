class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N=len(nums)
        n=N//3
        leftMinSum=[0]*N
        rightMaxSum=[0]*N
        minheap=[]
        maxheap=[]

        curLeftSum=0
        for i in range(2*n):
            heapq.heappush(maxheap,-nums[i])
            curLeftSum+=nums[i]
            if len(maxheap)>n:
                curLeftSum-=-heapq.heappop(maxheap)
            
            leftMinSum[i]=curLeftSum
        
        curRightSum=0
        for i in range(N-1,n-1,-1):
            heapq.heappush(minheap,nums[i])
            curRightSum+=nums[i]

            if len(minheap)>n:
                curRightSum-=heapq.heappop(minheap)
            
            rightMaxSum[i]=curRightSum
        
        min_=float('inf')
        for i in range(n-1,2*n):
            min_=min(min_,leftMinSum[i]-rightMaxSum[i+1])
        return min_

