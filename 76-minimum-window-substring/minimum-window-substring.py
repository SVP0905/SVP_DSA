class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict={}
        for ch in t:
            t_dict[ch]=t_dict.get(ch,0)+1
        
        needed=len(t_dict)
        
        l,r=0,0
        window={}
        ans=(float('inf'),0,0)
        formed=0
        for r in range(len(s)):
            ch=s[r]
            window[ch]=window.get(ch,0)+1
            if ch in t_dict and window[ch]==t_dict[ch]:
                formed+=1
                
            
            while formed==needed:
                cur_len=r-l+1
                if cur_len<ans[0]:
                    ans=(cur_len,l,r)
                
                window[s[l]]-=1
                
                if s[l] in t_dict and window[s[l]]<t_dict[s[l]]:
                    formed-=1 
                l+=1
        
        if ans[0]==float('inf'):
            return ''
        else:
            return s[ans[1]:ans[2]+1]