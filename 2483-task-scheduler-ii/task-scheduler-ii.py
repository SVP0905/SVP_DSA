class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_seen={}
        current_days=0
        for task in tasks:
            current_days+=1

            if task in last_seen:
                next_allowed=last_seen[task]+space+1

                if current_days<next_allowed:
                    current_days=next_allowed
            
            last_seen[task]=current_days
        
        return current_days
