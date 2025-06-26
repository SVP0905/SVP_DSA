class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros=0
        for ch in s:
            if ch=='0':
                zeros+=1
        
        current_val=0
        ones=0
        for i,ch in enumerate(reversed(s)):
            if ch=='1':
                bit_val=2**i
                if current_val+bit_val<=k:
                    current_val+=bit_val
                    ones+=1
        
        return zeros+ones
