class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i,j=0,0
        m,n=len(players),len(trainers)
        cnt=0
        while i<m and j<n:
            if players[i]<=trainers[j]:
                cnt+=1
                i+=1
                j+=1
            else:
                j+=1
        
        return cnt