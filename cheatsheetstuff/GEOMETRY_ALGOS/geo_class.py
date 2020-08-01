import math as M
EPS=1e-12
NUM_SIG=9
class pt_xyz:
  def __init__(self, a, b, c): self.x,self.y,self.z=a,b,c
  def __add__(self, b): return pt_xyz(self.x+b.x, self.y+b.y, self.z+b.z)
  def __add__(self, b): return pt_xyz(self.x-b.x, self.y-b.y, self.z-b.z)
  def __mul__(self, c): return pt_xyz(self.x*c, self.y*c, self.z*c)
  def __lt__(self, b): return ((self.x,self.y,self.z)<(b.x,b.y,b.z))
  def __eq__(self, b): return ((self.x,self.y,self.z)==(b.x,b.y,b.z))
  def __str__(self): "{} {} {}".format(self.x, self.y, self.z)
  def __round__(self, n): return pt_xyz(round(self.x,n),round(self.y,n),round(self.z,n))
  def __hash__(self):return hash((self.x,self.y,self.z))

class pt_xy:
  def __init__(self, a,b):self.x,self.y=a,b
  def __add__(self, b): return pt_xy(self.x+b.x, self.y+b.y)
  def __sub__(self, b): return pt_xy(self.x-b.x, self.y-b.y) 
  def __mul__(self, c): return pt_xy(self.x*c, self.y*c)
  def __truediv__(self, c): return pt_xy(self.x/c, self.y/c)
  def __floordiv__(self, c): return pt_xy(self.x//c, self.y//c)
  def __lt__(self, b): return ((self.x, self.y)<(b.x, b.y))
  def __eq__(self, b): return ((self.x,self.y)==(b.x,b.y))
  def __str__(self): return "{} {}".format(self.x, self.y)
  def __round__(self, n): return pt_xy(round(self.x,n),round(self.y,n))
  def __hash__(self):return hash((self.x,self.y))

class GEO_ALGOS:
  def __init__(self): pass
  def epscmp(self, x): return -1 if x<-EPS else 1 if x>EPS else 0
  def c_cmp(self, a,b): return 0 if M.isclose(a, b) else -1 if a<b else 1
  
  def dot(self, a,b):   return a.x*b.x+a.y*b.y
  def dot3d(self, a,b): return a.x*b.x+a.y*b.y+a.z*b.z
  
  def cross(self, a,b): return a.x*b.y-a.y*b.x
  def cross3d(self, a,b): 
    return pt_xyz(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x)
  
  def dst1(self, a, b): return M.hypot((a-b).x, (a-b).y)
  def dst2(self, a, b): return self.dot(a-b,a-b)
  
  def rot_cw90(self, p):  return pt_xy( p.y,-p.x)
  def rot_ccw90(self, p): return pt_xy(-p.y, p.x)
  def rot_ccw(self, p,t): 
    ct,st=M.cos(t),M.sin(t); return pt_xy(p.x*ct-p.y*st, p.x*st+p.y*ct)
  
  #change is_ccw????
  def is_ccw(self, a,b,c): return self.c_cmp(self.cross(b-a,c-a),0)
  def ang_abc(self, a,b,c):
    p,q=a-b,c-b;return M.acos(self.dot(p,q)/M.sqrt(self.dot(p,p)*self.dot(q,q)))
  
  def pjt_pt_ln(self, a,b,c): p=b-a; return a+p*self.dot(c-a,p)/self.dot(p,p)
  def pjt_pt_seg(self, a,b,c):
    p=b-a; r=self.dot(p,p)
    if self.c_cmp(r,0): return a
    r=self.dot(c-a,p)/r
    return a if r<0 else b if r>1 else a+p*r
  
  def dst_pt_ln(self, a,b,c): return self.dst1(c, self.pjt_pt_ln(a,b,c))
  def dst_pt_seg(self, a,b,c): return self.dst1(c, self.pjt_pt_ln_seg(a,b,c))
  
  #following three might have bugs
  def is_ln_par(self, a,b,c,d): return (self.c_cmp(self.cross(b-a,c-a))==0)
  def is_ln_col(self, a,b,c,d):
    return (self.is_ln_par(a,b,c,d) 
    and self.is_ln_par(b,a,a,c) and self.is_ln_par(d,c,c,a))
  
  def is_seg_cross(self, a,b,c,d):
    if self.is_ln_col(a,b,c,d):
      
    
  def is_ln_cross(self, a,b,c,d): 
    return (not self.is_ln_par(a,b,c,d) or self.is_ln_col(a,b,c,d))
    
  def pt_ln_cross(self, a,b,c,d):
    p,q=b-a,c-d; return a+p*self.cross(c-a,q)/self.cross(p,q)
    
  
  

def main():
  print("here")

main()
  
  
  
