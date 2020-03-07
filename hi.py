
from sys import stdin
from collections import deque

inf = 10001
N, H, L = map(int, input().rstrip().split())
hl = set(map(int, input().rstrip().split()))
al = [[] for _ in range(N)]
for line in stdin:
  u, v = map(int, line.split())
  al[u].append(v)
  al[v].append(u)

HI = [inf] * N

def bfs(u):
  q = deque()
  q.append(u)
  while len(q) > 0:
    cur = q.popleft()
    for v in al[cur]:
      if HI[cur] + 1 < HI[v]:
        HI[v] = HI[cur] + 1
        q.append(v)

for v in hl:
  HI[v] = 0

for v in hl:
  bfs(v)

maxHI = -1
maxHIind = -1
for i, hi in enumerate(HI):
  if hi > maxHI:
    maxHI = hi
    maxHIind = i

print(maxHIind)
