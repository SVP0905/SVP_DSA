class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        l=0
        res=''
        while l<=n-3:
            r=l
            while r<n and num[l]==num[r]:
                r+=1
            
            window_len=r-l

            if window_len>=3:
                str_=num[l:l+3]
                if str_>res:
                    res=str_
            
            l=r
        
        return res