from sys import stdin as rf
#dijkstras tested shortestpath1, shortestpath2(modified works), flowerytrails(modified works), fulltank(modified)
INF=1000000000

class GRAPH_ALGOS():
    def __init__(self):
        self.adj={}
    
    #modify the bottom two as needed
    def init_adj(self, n):
        self.adj={i:{} for i in range(n)}
    
    def add_edge_adj(self, u, v, w):
        self.adj[u][v]=w
    
    def dijkstras(self, s, t):
        import heapq as h
        self.dst={i:INF for i in self.adj}; self.dst[s]=0
        self.par={i:i for i in self.adj}; self.par[s]=s
        pq=[]; h.heappush(pq, (0,s))
        while pq:
            d,u=h.heappop(pq)
            if d>self.dst[u]: 
                continue
            #if u==t: return d #uncomment this line for fast return
            for v,w in self.adj[u].items():
                if self.dst[v]>d+w:
                    self.dst[v],self.par[v]=d+w,u
                    h.heappush(pq, (d+w, v))
    
    def APSP(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    self.adjmat[i][j]=min(self.adjmat[i][j], self.adjmat[i][k]+self.adjmat[k][j])
