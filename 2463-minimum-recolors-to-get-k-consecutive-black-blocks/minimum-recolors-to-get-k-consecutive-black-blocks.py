class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        num_whites=0
        n=len(blocks)
        q=deque()
        for i in range(k):
            if blocks[i]=='W':
                num_whites+=1
            q.append(blocks[i])
        
        res=num_whites

        for i in range(k,n):
            if q.popleft()=='W':
                num_whites-=1
            
            if blocks[i]=='W':
                num_whites+=1
            q.append(blocks[i])

            res=min(res,num_whites)
        
        return res

