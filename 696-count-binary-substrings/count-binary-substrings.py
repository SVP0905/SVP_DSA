class Solution:
    def checkConsequtive(self,sub):
        prev=sub[0]
        grp=1
        for i in range(1,len(sub)):
            if sub[i]!=prev:
                grp+=1
                prev=sub[i]
        
        return grp==2

            

    def isSub(self,sub):
        map_=Counter(sub)

        zeros=map_.get('0',0)
        ones=map_.get('1',0)

        if zeros==ones:
            if self.checkConsequtive(sub):
                return True
        
        return False



    def countBinarySubstrings(self, s: str) -> int:
            groups = []
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    groups.append(count)
                    count = 1
            groups.append(count)
            
            return sum(min(groups[i], groups[i+1]) for i in range(len(groups)-1))