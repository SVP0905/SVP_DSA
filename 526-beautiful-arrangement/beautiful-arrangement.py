class Solution:
    def countArrangement(self, n: int) -> int:
        cnt=0
        visited=[False]*(n+1)

        def dfs(path):
            nonlocal cnt
            if len(path)==n:
                cnt+=1
                return

            for num in range(1,n+1):
                if not visited[num]:
                    pos=len(path)+1
                    if num%pos==0 or pos%num==0:
                        path.append(num)
                        visited[num]=True
                        dfs(path)
                        path.pop()
                        visited[num]=False
        

        dfs([])

        return cnt
            

