class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain=[0]*(len(gain)+1)

        for i in range(1,len(gain)+1):
            max_gain[i]=max_gain[i-1]+gain[i-1] 
        
        return max(max_gain)