class Tarjan:
    def __init__(self,edges):
        self.timer=0
        self.graph=defaultdict(list)
        self.all_vertices=set()
        for u,v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.all_vertices.add(u)
            self.all_vertices.add(v)
        self.n=len(self.all_vertices)
        self.stack=[]
        self.onStack=set()
        self.tin=defaultdict(int)
        self.low=defaultdict(int)
        self.visited=set()
        self.bridges=[]
        self.scc=[]
    
    def dfs(self,v,parent):
        self.visited.add(v)
        self.stack.append(v)
        self.onStack.add(v)
        self.tin[v]=self.low[v]=self.timer
        self.timer+=1

        for nei in self.graph[v]:
            if nei==parent:
                continue
            if nei not in self.visited:
                self.dfs(nei,v)
                self.low[v]=min(self.low[v],self.low[nei])
                if self.low[nei]>self.tin[v]:
                    self.bridges.append((v,nei))
            elif nei in self.onStack:
                self.low[v]=min(self.low[v],self.tin[nei])
        
        if self.low[v]==self.tin[v]:
            cur_scc=[]
            while True:
                node=self.stack.pop()
                self.onStack.remove(node)
                cur_scc.append(node)
                if node==v:
                    break
            self.scc.append(cur_scc)



class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        tr=Tarjan(connections)
        for v in tr.all_vertices:
            if v not in tr.visited:
                tr.dfs(v,-1)

        return tr.bridges
        