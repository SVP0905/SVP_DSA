class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        M=10**9+7
        n=len(arr)
    
        even,odd,count,sum_=1,0,0,0
        for i in range(n):
            sum_+=arr[i]
            if sum_%2==0:
                count=(count+odd)%M
                even+=1
            else:
                count=(count+even)%M
                odd+=1
        
        return count