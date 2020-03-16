#basic bfs sssp on a grid
#agis daniels
import sys
from collections import deque

dr=[1,0,-1,0]
dc=[0,1,0,-1]
grid=[]
R=0
C=0
dist=[]

def bfs():
    q=deque()
    q.append((0,0))
    dist[0][0]=0
    while q:
        r,c=q.popleft()
        if r==R-1 and c==C-1:
            return
        curg=grid[r][c]
        curd=dist[r][c]
        for i in range(4):
            nr=r+dr[i]*curg
            nc=c+dc[i]*curg
            if nc<0 or nr<0 or nr>=R or nc>=C:
                continue
            if dist[nr][nc]>curd+1:
                dist[nr][nc]=curd+1
                q.append((nr,nc))

def main():
    global R,C,grid,dist
    inf=10000000
    for line in sys.stdin:
        R,C=map(int, line.split())
        break
    grid=[[0]*C for _ in range(R)]
    dist=[[inf]*C for _ in range(R)]
    for i,line in enumerate(sys.stdin):
        grid[i]=list(map(int, list(line.strip())))
    bfs()
    if dist[R-1][C-1]<inf:
        print(dist[R-1][C-1])
    else:
        print(-1)
main()
    
