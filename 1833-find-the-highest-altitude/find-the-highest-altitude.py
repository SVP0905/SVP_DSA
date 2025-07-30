class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur=0
        max_=0
        for g in gain:
            cur+=g
            max_=max(max_,cur)
        return max_
