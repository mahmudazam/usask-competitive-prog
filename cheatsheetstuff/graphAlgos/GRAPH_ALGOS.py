from sys import stdin as rf
#dijkstras tested shortestpath1, shortestpath2(modified works), flowerytrails(modified works), fulltank(modified)
#APSP tested on allpairspath, kastenlauf(modified), arbitrage
INF=1000000000

class GRAPH_ALGOS():
    def __init__(self):
        self.adj={}
    
    def init_mat(self, n):
        self.V=n
        self.mat=[[INF]*n for _ in range(n)]
        for i in range(n): self.mat[i][i]=0
    
    #modify the bottom two as needed
    def init_adj(self, n):
        self.adj={i:{} for i in range(n)}
    
    def add_edge_adj(self, u, v, w):
        self.adj[u][v]=w
        
    def add_edge_mat(self, u, v, w):
        self.mat[u][v]=min(w, self.mat[u][v])
    
    
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
                    #if self.mat[i][k]<INF and self.mat[k][j]<INF: #use for negative cycles check
                    self.mat[i][j]=min(self.mat[i][j], self.mat[i][k]+self.mat[k][j])
    
    def APSP_neg_cycles(self):
        for i in range(self.V):
            for j in range(self.V):
                for k in range(self.V):
                    if self.mat[k][k]<0 and self.mat[i][k]!=INF and self.mat[k][j]!=INF:
                        self.mat[i][j]=-INF
