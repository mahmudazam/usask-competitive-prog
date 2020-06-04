#kmp works on id stringmatching, irepeatmyself, 


class STR_ALGOS:
    def __init__(self, s, offset):
        self.n=len(s)
        self.m=0
        self.T=[c for c in s]
        self.P=[]
        self.B=[]
    
    def reset_t(self, s):
        self.n=len(s)
        self.T=[c for c in s]
    
    def kmpPreprocess(self, s):
        self.m=len(s)
        self.P=[c for c in s]
        self.B=[0]*(self.m+1) #add plus one if no work
        self.B[0]=j=-1
        for i in range(self.m):
            while j>=0 and self.P[i] != self.P[j]:
                j=self.B[j]
            j+=1
            self.B[i+1]=j
    
    def kmpSearch(self):
        ans=[]
        j=0
        for i in range(self.n):
            while j>=0 and self.T[i] != self.P[j]:
                j=self.B[j]
            j+=1
            if j==self.m:
                ans.append(1+i-j)
                j=self.B[j]
        return ans
