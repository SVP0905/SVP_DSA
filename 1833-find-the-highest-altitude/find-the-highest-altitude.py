class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=[0]*(len(gain)+1)
        prefix[0]=gain[0]

        for i in range(len(gain)):
            prefix[i]=prefix[i-1]+gain[i]
        
        return max(prefix)
