class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq =[0]*26

        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        
        left_half=[]
        mid_ch=''

        for i in range(26):
            if freq[i]==0:
                continue
            
            ch=chr(ord('a')+i)

            if freq[i]%2!=0:
                mid_ch=ch
            
            left_half.append(ch*(freq[i]//2))
        

        left_str=''.join(left_half)

        return left_str+mid_ch+left_str[::-1]

            


