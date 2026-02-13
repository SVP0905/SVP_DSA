class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        max_len=0
        cnt=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                cnt+=1
            else:
                max_len=max(max_len,cnt)
                cnt=1
        
        max_len=max(max_len,cnt)

        cnt1,cnt2=0,0

        pairs=[('a','b','c'),('a','c','b'),('b','c','a')]

        for c1,c2,forbidden in pairs:
            segments=s.split(forbidden)
            
            for seg in segments:
                if not seg:
                    continue

                map_={0:-1}
                c1_cnt,c2_cnt=0,0
                diff=0
                for i,ch in enumerate(seg):
                    if ch==c1:
                        c1_cnt+=1
                    else:
                        c2_cnt+=1

                    diff=c1_cnt-c2_cnt

                    if diff in map_:
                        max_len=max(max_len,i-map_[diff])
                    else:
                        map_[diff]=i
        

        state_map={(0,0):-1}

        c_a,c_b,c_c=0,0,0

        for i,ch in enumerate(s):
            if ch=='a':
                c_a+=1
            elif ch=='b':
                c_b+=1
            else:
                c_c+=1
            
            state=(c_a-c_b,c_b-c_c)

            if state in state_map:
                max_len=max(max_len,i-state_map[state])
            else:
                state_map[state]=i
        
        return max_len

