#solved using our bfs toposort template
from collections import deque
import sys
adj=[]
V=0

def topoSortBFS(s,t):
    ans=[]
    deg=[0]*(V+1)
    for u in adj:
        for v in u:
            deg[v]+=1
    q=deque()
    for v in range(1, V+1):
        if deg[v]==0:
            q.append(v)
    while q:
        u=q.popleft()
        ans.append(u)
        for v in adj[u]:
            deg[v]-=1
            if deg[v]==0:
                q.append(v)
    if len(ans)==V:
        for el in ans:
            print(el)
    else:
        print("IMPOSSIBLE")

def main():
    global V, adj
    for line in sys.stdin:
        V,m=map(int, line.split())
        break
    adj=[[] for _ in range(V+1)]
    for line in sys.stdin:
        a,b=map(int, line.split())
        adj[a].append(b)
    topoSortBFS(0,V)
main()
