class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[]
        print(folder)
        for f in folder:
            if not res:
                res.append(f)
            elif f.startswith(res[-1]) and len(f)>len(res[-1]) and f[len(res[-1])]=='/':
                continue
            else:
                res.append(f)
        
        return res
