class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms=list(range(n))
        heapq.heapify(available_rooms)

        busy_rooms=[]
        meetings_per_room=[0]*n
        for start,end in sorted(meetings):
            while busy_rooms and busy_rooms[0][0]<=start:
                cur_end,cur_room=heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms,cur_room)
            
            if available_rooms:
                choosen_room=heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms,(end,choosen_room))
            else:
                earliest_end,earliest_room=heapq.heappop(busy_rooms)
                new_end=earliest_end+end-start
                heapq.heappush(busy_rooms,(new_end,earliest_room))
                choosen_room=earliest_room
            
            meetings_per_room[choosen_room]+=1
        
        return meetings_per_room.index(max(meetings_per_room))