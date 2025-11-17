class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        map_={}
        days=0
        for i in range(len(tasks)):
            days+=1

            if tasks[i] in map_:
                allowed_days=map_[tasks[i]]+space+1

                if days<allowed_days:
                    days=allowed_days
            
            map_[tasks[i]]=days
        
        return days
        
        print(map_)
        return days


