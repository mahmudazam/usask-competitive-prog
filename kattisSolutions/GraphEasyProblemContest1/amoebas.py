#this uses our template flood fill
#agis daniels
import sys

grid=[['X']*100 for _ in range(100)]
dr=[1,1,0,-1,-1,-1, 0, 1]
dc=[0,1,1, 1, 0,-1,-1,-1]
R=0
C=0

def ff(r, c, c1, c2):
    global R, C, grid
    stk=[(r, c)]
    while stk:
        r,c=stk.pop()
        if c<0 or r<0 or r>=R or c>=C: continue
        if grid[r][c]!=c1: continue
        grid[r][c]=c2
        for i in range(8):
            stk.append((r+dr[i],c+dc[i]))

def main():
    global grid,R,C
    n=0
    m=0
    for line in sys.stdin:
        m,n=map(int, line.split())
        break
    R=m
    C=n
    for i, line in enumerate(sys.stdin):
        grid[i]=list(line.strip())
    ans=0
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j]=='#':
                ff(i,j,'#','P')
                ans+=1
    print(ans)
main()
