class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        when_room_become_free=[0]*n
        meetings_per_room=[0]*n

        for start,end in sorted(meetings):
            d=end-start
            assigned_room=None
            for i in range(n):
                if when_room_become_free[i]<=start:
                    when_room_become_free[i]=end
                    assigned_room=i
                    break
                
            if assigned_room is None:
                earliest_time=min(when_room_become_free)
                assigned_room=when_room_become_free.index(earliest_time)

                when_room_become_free[assigned_room]=earliest_time+d
            
            meetings_per_room[assigned_room]+=1
        
        i=max(meetings_per_room)
        return meetings_per_room.index(i)

                