class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        rooms_free=[False]*n
        rooms_free[0]=True

        q=deque([0])

        while q:
            for _ in range(len(q)):
                node=q.popleft()
                for nei in rooms[node]:
                    if not rooms_free[nei] and not rooms_free[nei]:
                        q.append(nei)
                        rooms_free[nei]=True
        
        for i in range(n):
            if not rooms_free[i]:
                return False
        
        return True

            
