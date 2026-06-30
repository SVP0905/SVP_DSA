class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        seen={'a':-1,'b':-1,'c':-1}

        cnt=0
        for r,char in enumerate(s):
            seen[char]=r

            if -1 not in seen.values():
                cnt+=min(seen.values())+1
        
        return cnt