class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list=defaultdict(list)

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        print(adj_list)

        cnt=0
        def dfs(node,parent):
            nonlocal cnt
            cur_sum=values[node]
            
            for nei_node in adj_list[node]:
                if nei_node !=parent:
                    cur_sum+=dfs(nei_node,node)

            if cur_sum%k==0:
                cnt+=1
                return 0

            return cur_sum%k


        dfs(0,-1)
        return cnt


        
        
