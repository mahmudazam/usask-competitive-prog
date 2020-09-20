
from sys import stdin as rf

class edge:
  def __init__(self, cap, flow):
    self.cap = cap
    self.flow = flow

  def __str__(self):
    return f'(c={self.cap},f={self.flow})'

class MAX_FLOW():
  def __init__(self):
    self.adj = {}
    self.res = {}
    self.level = {}

  def add_vert(self, u):
    if u not in self.adj:
      self.adj[u] = {}
      return True
    return False

  def set_edge(self, u, v, cap, flow):
    self.add_vert(u)
    self.add_vert(v)
    if flow <= cap:
      self.adj[u][v] = edge(cap, flow)
      return True
    return False

  def res_graph(self):
    pass

  def __str__(self):
    return str({
        u: {v : str(e) for (v, e) in uadj.items()}
                  for (u, uadj) in self.adj.items()
      })

sol = MAX_FLOW()
sol.set_edge(1, 2, 3, 0)
sol.set_edge(1, 3, 3, 0)
sol.set_edge(1, 4, 2, 0)
sol.set_edge(2, 3, 1, 0)
sol.set_edge(2, 5, 2, 0)
sol.set_edge(2, 5, 2, 0)
sol.set_edge(3, 6, 3, 0)
sol.set_edge(4, 6, 3, 0)
sol.set_edge(5, 6, 1, 0)
sol.set_edge(5, 7, 7, 0)
sol.set_edge(6, 7, 7, 0)

print(sol)
