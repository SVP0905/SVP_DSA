class SegmentTree:
    def __init__(self,arr,MOD):
        self.MOD=MOD
        self.n=len(arr)
        self.tree=[0]*(4*self.n)
        self.pow10=[1]*(self.n+1)
    

        for i in range(1,self.n+1):
            self.pow10[i]=(self.pow10[i-1]*10)%self.MOD
        
        self.arr=[]
        for ch in arr:
            d=int(ch)
            if d!=0:
                self.arr.append((d,d,1))
            else:
                self.arr.append((0,0,0))
        
        if self.n>0:
            self._build(0,0,self.n-1)
    

    def _build(self,node,start,end):
        if start==end:
            self.tree[node]=self.arr[start]
        else:
            mid=(start+end)//2
            left_ch=2*node+1
            right_ch=2*node+2

            self._build(left_ch,start,mid)
            self._build(right_ch,mid+1,end)
        
            self.tree[node]=self._merge(self.tree[left_ch],self.tree[right_ch])
    


    def _get_identity(self):
        return (0,0,0)
    

    def _merge(self,left_val,right_val):
        v1,s1,c1=left_val
        v2,s2,c2=right_val

        combined_cnt=c1+c2
        combined_sum=s1+s2

        combined_val=(v1*self.pow10[c2]+v2)%self.MOD

        return (combined_val,combined_sum,combined_cnt)
    

    def query(self,left,right):
        return self._query(0,0,self.n-1,left,right)
    

    def _query(self,node,start,end,left,right):
        if right<start or left>end:
            return (0,0,0)
        
        if left<=start and end<=right:
            return self.tree[node]
        
        mid=(start+end)//2
        left_ch=2*node+1
        right_ch=2*node+2
        left_res=self._query(left_ch,start,mid,left,right)
        right_res=self._query(right_ch,mid+1,end,left,right)

        return self._merge(left_res,right_res)



class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD=10**9+7
        tree=SegmentTree(s,MOD)
        ans=[]

        for l,r in queries:
            val,sum_,cnt=tree.query(l,r)
            ans.append((val*sum_)%MOD)

        return ans
                