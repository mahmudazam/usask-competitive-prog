#using a floyd worshals template 
#agis daniels
import sys

n=m=q=0

def APSP():
    global n,m,q
    INF = 1000000000
    mat=[[INF]*n for _ in range(n)]
    for i in range(n):
        mat[i][i]=0
    for i in range(m):
        u,v,w=map(int, sys.stdin.readline().split())
        mat[u][v]= min(w, mat[u][v])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][k]<INF and mat[k][j]<INF:
                    mat[i][j]=min(mat[i][j], mat[i][k]+mat[k][j])
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if mat[k][k]<0 and mat[i][k]!=INF and mat[k][j]!=INF:
                    mat[i][j]=-INF
    for i in range(q):
        u,v=map(int, sys.stdin.readline().split())
        if mat[u][v]==INF:
            print("Impossible")
        elif mat[u][v]==-INF:
            print("-Infinity")
        else:
            print(mat[u][v])
    print




def main():
    global n,m,q
    n,m,q=map(int, sys.stdin.readline().split())
    while n or m or q:
        APSP()
        n,m,q=map(int, sys.stdin.readline().split())
main()
