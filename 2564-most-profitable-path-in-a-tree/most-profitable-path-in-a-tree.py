class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj={i:[] for i in range(len(amount))}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfsbob(cur,t,visited):
            bob_map[cur]=t
            visited.add(cur)

            if cur==0:
                return True
            
            for nei in adj[cur]:
                if nei not in visited:
                    if dfsbob(nei,t+1,visited):
                        return True
            
            if cur in bob_map:
                del bob_map[cur]

            return False
        
        def dfsAlice(cur,t,income,visited):
            nonlocal alice_income
            visited.add(cur)

            if cur not in bob_map or t<bob_map[cur]:
                income+=amount[cur]
            elif t==bob_map[cur]:
                income+=amount[cur]//2
            
            if len(adj[cur])==1 and cur!=0:
                alice_income=max(income,alice_income)
            
            for nei in adj[cur]:
                if nei not in visited:
                    dfsAlice(nei,t+1,income,visited)
            
        
        bob_map={}
        visited=set()
        dfsbob(bob,0,visited)
    
        # nonlocal alice_income
        alice_income=float('-inf')
        visited=set()
        dfsAlice(0,0,0,visited)

        return alice_income

