class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        idx=0
        n=len(chars)

        while i<n:
            j=i
            while j<n and chars[i]==chars[j]:
                j+=1
            
            cnt=j-i
            chars[idx]=chars[i]
            idx+=1

            if cnt>1:
                for digit in str(cnt):
                    chars[idx]=digit
                    idx+=1
            
            i=j
        return idx