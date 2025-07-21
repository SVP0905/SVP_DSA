class Solution:
    def makeFancyString(self, s: str) -> str:
        res=''
        res+=s[0]
        prev=s[0]
        cnt=1
        for i in range(1,len(s)):
            if s[i]==prev:
                cnt+=1
                if cnt>=3:
                    continue
                else:
                    res+=s[i]
            else:
                prev=s[i]
                cnt=1
                res+=s[i]
        return res

        