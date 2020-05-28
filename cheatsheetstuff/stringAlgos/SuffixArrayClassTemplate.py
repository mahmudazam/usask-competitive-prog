class SUFF_ARR:
    def __init__(self, s, offset):
        self.n=len(s)+1
        self.T     =[ord(c) for c in s]
        self.RA    =[0]*self.n
        self.SA    =[0]*self.n
        self.tempSA=[0]*self.n
        self.tempRA=[0]*self.n
        self.K     =[]
        self.T.append(0)
        k=1
        while k<self.n:
            self.K.append(k)
            k*=2
    def countingSort(self, k):
        maxi=max(300,self.n)
        tmp=0
        #j=self.n
        c=[0]*maxi
        # for i in range(self.n): #try self.n-k
        #     if i+k<self.n:
        #         c[self.RA[i+k]]+=1
        #     else:
        #         c[0]+=1
        for i in range(self.n-k):
            c[self.RA[i+k]]+=1
        c[0]+=(self.n-(self.n-k))
        for i in range(maxi):
            t=c[i]
            c[i]=tmp
            tmp+=t
        for i in range(self.n):
            pos=0
            if self.SA[i]+k<self.n:
                pos=self.RA[self.SA[i]+k]
            self.tempSA[c[pos]]=self.SA[i]
            c[pos]+=1
        for i, el in enumerate(self.tempSA):
            self.SA[i]=el
    
    def constructSA(self):
        for i,el in enumerate(self.T):
            self.RA[i]=el
            self.SA[i]=i
        for k in self.K:
            self.countingSort(k)
            self.countingSort(0)
            self.tempRA[self.SA[0]],r=0,0
            for i in range(1, self.n):
                if not (self.RA[self.SA[i]] == self.RA[self.SA[i-1]] and self.RA[self.SA[i]+k] == self.RA[self.SA[i-1]+k]):
                    r+=1
                self.tempRA[self.SA[i]]=r
            for i,el in enumerate(self.tempRA):
                self.RA[i]=el
            if self.RA[self.SA[-1]]==self.n-1:
                break
        self.tempRA=[]
        self.tempSA=[]
        self.RA=[]
