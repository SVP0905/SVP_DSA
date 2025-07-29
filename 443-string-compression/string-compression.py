class Solution:
    def compress(self, chars: List[str]) -> int:
        r=0
        idx=0
        n=len(chars)
        while r<n:
            j=r
            while j<n and chars[j]==chars[r]:
                j+=1
            
            cnt=j-r
            chars[idx]=chars[r]
            idx+=1

            if cnt>1:
                for digit in str(cnt):
                    chars[idx]=digit
                    idx+=1
            
            r=j
        return idx