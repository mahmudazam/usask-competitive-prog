#this uses flood fill template merged with bfs
#agis daniels
from collections import deque

inf=2000000
grid=[['X']*100 for _ in range(100)]
moves=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
R=0
C=0
dist=[]

def ff(r,c,c1,c2):
    global grid,moves,R,C,dist
    dist=[[inf for _ in range(C)] for _ in range(R)]
    q=deque()
    q.append((r,c))
    dist[r][c]=0
    while q:
        r,c=q.popleft()
        if grid[r][c]!=c1:
            continue
        grid[r][c]=c2
        for dr,dc in moves:
            rr=r+dr
            cc=c+dc
            if (0<=rr and rr<R and 0<=cc and cc<C) and dist[rr][cc]>dist[r][c]+1:
                dist[rr][cc]=dist[r][c]+1
                q.append((rr,cc))
def main():
    global grid,R,C
    n=int(input())
    R=n
    C=n
    for i in range(n):
        grid[i]=list(input().strip())
    ans=0
    for i in range(R):
        for j in range(C):
            if grid[i][j]=='K':
                grid[i][j]='.'
                ff(i,j,'.','X')
    if dist[0][0]!=inf:
        print(dist[0][0])
    else:
        print(-1)
main()
