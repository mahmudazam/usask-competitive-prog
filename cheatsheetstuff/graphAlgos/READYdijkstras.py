# 
def dijkstras(s):
    global adj, V, inf,dist
    dist=[inf]*V; dist[s]=0
    pq=[]; h.heappush(pq, (0, s))
    while pq:
        d,u=h.heappop(pq)
        if d>dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
                h.heappush(pq, (dist[v], v))
