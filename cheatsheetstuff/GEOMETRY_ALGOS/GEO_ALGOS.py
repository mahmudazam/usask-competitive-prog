import math
from sys import stdin as rf

#euclidean_distance (floats)tested on cursethedarkness, sibice, imperfectgps
#dist_pt_seg tested on goatrope
#segments_intersect tested on countingtriangles
EPS=1e-12
#todo make sure we know the math behind the functions it loosk like 
# a lot of matrix operation stuffs 
#uncomment the comment the commented lines for floating point cords
class pt_xy:
    #def __init__(self, new_x, new_y):self.x,self.y=map(round,[new_x,new_y])
    def __init__(self, new_x=float(0), new_y=float(0)):self.x,self.y=map(float,(new_x,new_y))
    
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
    
    def euclidean_distance(self, a, b): return math.hypot((a-b).x, (a-b).y)
    
    #TODO look up and see how well the z cord translates into these functions
    def dot_product(self, a, b): return a.x*b.x+a.y*b.y #move to point class
    def cross_product(self, a, b): return a.x*b.y-a.y*b.x
    
    def rotate_ccw90(self, p): return pt_xy(-p.y, p.x)
    def rotate_cw90(self, p):  return pt_xy( p.y,-p.x)
    def rotate_ccw(self, p, t): 
        return pt_xy(p.x*math.cos(t)-p.y*math.sin(t), p.x*math.sin(t)+p.y*math.cos(t))
    
    def project_pt_line(self, a, b, c): 
        return a+(b-a)*self.dot_product(c-a,b-a)/self.dot_product(b-a, b-a)
    
    def project_pt_line_segment(self, a, b, c):
        r=self.dot_product(b-a,b-a)
        if abs(r)<EPS: return a
        r=self.dot_product(c-a,b-a)/r
        if r<0: return a
        elif r>1: return b
        else: return a+(b-a)*r
    
    def dist_pt_segment(self, a, b, c):
        return self.euclidean_distance(c, self.project_pt_line_segment(a,b,c))
        
    def dist_pt_line(self, a, b, c): #cross product version to fomula sheeet
        return self.euclidean_distance(c, self.project_pt_line(a,b,c))
    
    def is_lines_parallel(self, a, b, c, d):
        return (abs(self.cross_product(b-a, c-d))<EPS)
        
    def is_lines_collinear(self, a, b, c, d): #copy paste code if its too slow this is safety from typing errors
        return (self.lines_parallel(a,b,c,d) 
        and self.lines_parallel(b,a,a,c) 
        and self.lines_parallel(d,c,c,a))
    
    def is_segments_intersect(self, a, b, c, d):
        if self.is_lines_collinear(a, b, c, d):
            if self.dist2(a, c)<EPS or self.dist2(a, d)<EPS or self.dist2(b, c)<EPS or self.dist2(b, d)<EPS:
                return True
            return not(self.dot(c-a, c-b)>0 and self.dot(d-a, d-b)>0 and self.dot(c-b, d-b)>0)
        ba=b-a
        dc=d-c
        if self.cross(d-a, ba)*self.cross(c-a, ba)>0: return False
        return not(self.cross(a-c, dc)*self.cross(b-c, dc)>0)
    
