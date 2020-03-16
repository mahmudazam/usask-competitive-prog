#using our faster prims template
#agis daniels
import heapq as h
inf=2000000000
taken=[]
pq=[]
mat={} # reps an adj list rn i think
disto=[]
V=0

def mstPrimsfaster():
    global pq, taken, mat, disto, inf
    taken=[False]*V
    disto=[inf]*V
    pq=[(0,0,0)]
    msc=0
    mst=[]
    while pq and len(mst)<V:
        w,v,u=h.heappop(pq)
        if not taken[v]:
            msc+=w
            mst.append((u+1, v+1))
            taken[v]=True
            for nv in mat:
                if nv==v or taken[nv]:
                    continue
                dist=mat[v][nv]
                if dist>disto[nv]:
                    continue
                disto[nv]=dist
                h.heappush(pq, (dist,nv,v))
    for u,v in mst[1:]:
        print(u,v)

def main():
    global mat, V
    n=int(input())
    mat={i:{} for i in range(n)}
    for i in range(n):
        tmp=list(map(int, input().split()))
        for j,w in enumerate(tmp):
            mat[i][j]=w
    V=n
    mstPrimsfaster()
main()
