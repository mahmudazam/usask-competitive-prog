#using our basic dijkstras template has a custom weight function
#agis daniels
import heapq as h
adjList=[]
dist=[]
V=0
inf=1000000000

def getCost(t, P, d):
    if P==0:
        return t-d if t>=d else inf
    if t>=d:
        return t-d
    rt=(d-t+P-1)//P
    return t+rt*P-d
    
def dijkstras(s):
    global dist
    dist=[inf]*V
    dist[s]=0
    pq=[]
    h.heappush(pq,(0, s))
    while pq:
        ct, cu = h.heappop(pq)
        for v, d, t, P in adjList[cu]:
            w=getCost(t, P, dist[cu])+d
            if dist[cu]+w<dist[v]:
                dist[v]=dist[cu]+w
                h.heappush(pq,(dist[v], v))
def main():
    global adjList, V, dist
    n,m,q,s=map(int, input().strip().split())
    while True:
        if n==0 and m==0 and q==0 and s==0:
            break
        V=n
        adjList=[[] for _ in range(V)]
        for i in range(m):
            u,v,t,P,d=map(int, input().strip().split())
            adjList[u].append((v, d, t, P))
        dijkstras(s)
        for i in range(q):
            qq=int(input())
            if dist[qq]==inf:
                print("Impossible")
            else:
                print(dist[qq])
        print()
        n,m,q,s=map(int, input().strip().split())
main()
