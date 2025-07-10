class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])
        q=deque([entrance])
        visited=set()
        visited.add((entrance[0],entrance[1]))
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        steps=0
        while q:
            q_len=len(q)

            for _ in range(q_len):
                x,y=q.popleft()
    
                if (x==0 or x==m-1 or y==0 or y==n-1) and [x,y]!=entrance:
                    return steps
                
                for dx,dy in directions:
                    new_x,new_y=dx+x,dy+y

                    if (0<=new_x<m and 0<=new_y<n and maze[new_x][new_y]=='.' and (new_x,new_y) not in visited):
                        q.append((new_x,new_y))
                        visited.add((new_x,new_y))
            steps+=1

        return steps if steps==0 else -1