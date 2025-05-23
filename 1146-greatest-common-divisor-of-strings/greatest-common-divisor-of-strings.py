class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ''
        
        def gcd(a,b):
            while a>0 and b>0:
                if a>b:
                    a=a%b
                else:
                    b=b%a
            return a if b==0 else b
        
        gcd_len=gcd(len(str1),len(str2))

        return str2[:gcd_len]