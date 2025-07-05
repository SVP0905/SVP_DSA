class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            if room in visited:
                return
            
            visited.add(room)
            for room in rooms[room]:
                dfs(room)
        visited=set()
        dfs(0)

        return len(visited)==len(rooms)