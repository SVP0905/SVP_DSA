from queue import PriorityQueue
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m,n=len(grid),len(grid[0])
        result=[0]*len(queries)
        directions=((0,1),(1,0),(0,-1),(-1,0))
        sorted_queries=sorted([(query,queryIdx) for queryIdx,query in enumerate(queries)])
        min_heap=PriorityQueue()
        visited=set()
        total_points=0

        min_heap.put((grid[0][0],0,0))
        visited.add((0,0))

        for query,queryIdx in sorted_queries:
            while not min_heap.empty() and min_heap.queue[0][0]<query:
                cell_val,r,c=min_heap.get()
                total_points+=1

                for dr,dc in directions:
                    new_r,new_c=dr+r,dc+c

                    if (0<=new_r<m and 0<=new_c<n and (new_r,new_c) not in visited):
                        min_heap.put((grid[new_r][new_c],new_r,new_c))
                        visited.add((new_r,new_c))
            result[queryIdx]=total_points
        return result
