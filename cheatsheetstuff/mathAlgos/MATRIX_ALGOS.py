import math
from sys import stdin as rf

EPS=1e-10
NUM_SIG=15

class MATRIX_ALGOS:
    def __init__(self, inMat):
        self.N,self.M=len(inMat),len(inMat[0])
        self.mat=[[el for el in row] for row in inMat]
    
    def epscmp0(self, x):
        return -1 if x<-EPS else 1 if x>EPS else 0
    
    def epscmpab(self, a, b):
        return epscmp0(a-b)
    
    def gauss_jordan(self, b):
        n,m=self.N,b.M
        irow,icol,ipiv,det=[0]*n,[0]*n,[0]*n,1
        det=1
        for i in range(n):
            pj=pk=-1
            for j in range(n):
                if ipiv[j]: continue
                for k in range(n):
                    if ipiv[k]: continue
                    if pj==-1 or math.fabs(self.mat[j][k])>math.fabs(self.mat[pj][pk]): pj,pk=j,k
            if self.epscmp0(self.mat[pj][pk])==0:
                print("matrix is singular")
                return None
            ipiv[pk]+=1
            self.mat[pj],self.mat
        

def main():
    obj=GEO_ALGOS()
    a=pt_xy(0,0)
    b=pt_xy(4,0)
    c=pt_xy(4,3)
    r=obj.triangle_incircle_radius(a,b,c)
    p1=obj.triangle_incenter(a,b,c)
    p2=obj.triangle_circumcenter(a,b,c)
    print(r)
    p1.display()
    p2.display()
main()
