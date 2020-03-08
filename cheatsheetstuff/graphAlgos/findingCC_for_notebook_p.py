V=1000
adjList=[[]]
seen=set()
curSeen=set() # global below init 4
# change 6 to curSeen.add(u) in dfs
numCC=0
def findCC():
    for v in range(V):
        if v not in seen:
            curSeen=set(); numCC+=1
            dfs(v)
            print("{} {}".format(numCC,
                ' '.join(map(str,curSeen))))

