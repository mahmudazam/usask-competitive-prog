import math
from sys import stdin as rf

#euclidean_distance (floats)tested on cursethedarkness, sibice
#dist_pt_seg tested on goatrope
EPS=1e-12
#todo make sure we know the math behind the functions it loosk like 
# a lot of matrix operation stuffs 
#uncomment the comment the commented lines for floating point cords
class pt_xy:
    def __init__(self, new_x, new_y):self.x,self.y=map(round,(new_x,new_y))
    #def __init__(self, new_x=float(0), new_y=float(0)):self.x,self.y=map(float,(new_x,new_y))
    
    def set_pt_i(self, n_pt_xy): self.x,self.y=n_pt_xy.x,n_pt_xy.y
    def display(self): print(self.x,self.y)
        
    def __add__(self, b): return pt_xy(self.x+b.x, self.y+b.y)
    def __sub__(self, b): return pt_xy(self.x-b.x, self.y-b.y) 
    def __mul__(self, c): return pt_xy(self.x*c, self.y*c)
    def __truediv__(self, c): return pt_xy(self.x/c, self.y/c) #does this even make sense in a int based point
    def __floordiv__(self, c): return pt_xy(self.x//c, self.y//c)
    
    #def __lt__(self, b): return (self.x<b.x) if self.x!=b.x else (self.y<b.y)
    #def __eq__(self, b): return (self.x==b.x) and (self.y==b.y)
    def __lt__(self, b): return (self.x<b.x) if abs(self.x-b.x)<EPS else (self.y<b.y)
    def __eq__(self, b): return (abs(self.x-b.x)<EPS) and (abs(self.y-b.y)<EPS)
    
class GEO_ALGOS:
    def __init__(self):
        pass
    
    def euclidean_distance(self, a, b):
        ror=a-b
        return math.hypot(ror.x,ror.y)
    
    def dot(self, a, b): return a.x*b.x+a.y*b.y
    def dist2(self, a, b): return self.dot(a-b,a-b)
    def cross(self, a, b): return a.x*b.y-a.y*b.x
    
    def rotate_ccw90(self, p): return pt_xy(-p.y, p.x)
    def rotate_cw90(self, p):  return pt_xy( p.y,-p.x)
    def rotate_ccw(self, p, t):
        return pt_xy(p.x*math.cos(t)-p.y*math.sin(t), p.x*math.sin(t)+p.y*math.cos(t))
    
    def move_pt_dist_deg(self, p, d, t):
        return pt_xy(p.x+d*math.sin(t), p.y+d*math.cos(t))
    
    def project_pt_line(self, a, b, c):
        pass
        
    def project_pt_seg(self, a, b, c):
        ba=b-a
        ca=c-a
        r=self.dot(ba,ba)
        if math.fabs(r)<EPS: return a
        r=self.dot(ca,ba)/r
        if r<0: return a
        elif r>1: return b
        else: return a+ba*r
    
    def dist_pt_seg(self, a, b, c):
        return math.sqrt(self.dist2(c, self.project_pt_seg(a,b,c)))
    
    def dist_pt_line(self, a,b,c):
        ba=b-a
        ca=c-a
        return abs(self.cross(ba,ca)/self.euclidean_distance(a,b))
