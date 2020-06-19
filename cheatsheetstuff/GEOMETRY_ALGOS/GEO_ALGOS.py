import math
from sys import stdin as rf

#euclidean_distance (floats)tested on cursethedarkness, sibice, imperfectgps
#dist_pt_seg tested on goatrope
#segments_intersect tested on countingtriangles
EPS=1e-12
NUM_SIG=9
#todo make sure we know the math behind the functions it loosk like 
# a lot of matrix operation stuffs 
#uncomment the comment the commented lines for floating point cords
class pt_xy:
    #def __init__(self, new_x, new_y):self.x,self.y=map(round,[new_x,new_y])
    def __init__(self, new_x=float(0), new_y=float(0)):
        self.x,self.y=round(new_x, NUM_SIG), round(new_y, NUM_SIG)
    
    def set_pt_xy(self, n_pt_xy): self.x,self.y=n_pt_xy.x,n_pt_xy.y
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
    
    def __round__(self, n): return pt_xy(round(self.x,n),round(self.y,n))

class GEO_ALGOS:
    def __init__(self):
        pass
    
    def epscmp(self, x):
        return -1 if x<-EPS else 1 if x>EPS else 0
    
    def euclidean_distance(self, a, b): return math.hypot((a-b).x, (a-b).y)
    
    #TODO look up and see how well the z cord translates into these functions
    def dot_product(self, a, b): return a.x*b.x+a.y*b.y #move to point class
    def cross_product(self, a, b): return a.x*b.y-a.y*b.x
    
    def dist2(self, a, b): return self.dot_product(a-b,a-b)
    
    def rotate_ccw90(self, p): return pt_xy(-p.y, p.x)
    def rotate_cw90(self, p):  return pt_xy( p.y,-p.x)
    def rotate_ccw(self, p, t): 
        return pt_xy(p.x*math.cos(t)-p.y*math.sin(t), p.x*math.sin(t)+p.y*math.cos(t))
    
    def point_rotation_wrt_line(self, a, b, c):
        return self.epscmp(self.cross_product(b-a,c-a))
    
    def angle_abc(self, a, b, c): #MARKED
        ab,cb=a-b,c-b
        return math.acos(self.dot_product(ab,cb)/math.sqrt(self.dot_product(ab,ab)*self.dot_product(cb,cb)))
    
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
        return (self.epscmp(self.cross_product(b-a, c-d))==0)
        #return (abs(self.cross_product(b-a, c-d))<EPS)
        
    def is_lines_collinear(self, a, b, c, d): #copy paste code if its too slow this is safety from typing errors
        return (self.is_lines_parallel(a,b,c,d) 
        and self.is_lines_parallel(b,a,a,c) 
        and self.is_lines_parallel(d,c,c,a))
    
    #return if collinear to get a unique intersection or check outside the funtion before hand
    def is_segments_intersect(self, a, b, c, d):
        if self.is_lines_collinear(a, b, c, d):
            if self.dist2(a, c)<EPS or self.dist2(a, d)<EPS or self.dist2(b, c)<EPS or self.dist2(b, d)<EPS:
                return True
            return not(self.dot_product(c-a, c-b)>0 and self.dot_product(d-a, d-b)>0 and self.dot_product(c-b, d-b)>0)
        return not((self.cross_product(d-a,b-a)*self.cross_product(c-a,b-a)>0)
        or (self.cross_product(a-c,d-c)*self.cross_product(b-c,d-c)>0))
    
    #move not outside the expr to get unique checker
    def is_lines_intersect(self, a, b, c, d):
        return (not self.is_lines_parallel(a,b,c,d) or self.is_lines_collinear(a,b,c,d))
    
    #this assumes you checked if unique intersections
    #doubles as segment intersections if youve check that they actually intersect
    def pt_lines_intersect(self, a, b, c, d):
        b,c,d=b-a,c-a,c-d
        return a+b*self.cross_product(c,d)/self.cross_product(b,d)
        
        
    #add the case for lines collinear
    def circle_center_given_abc(self, a, b, c):
        b,c=(a+b)/2,(a+c)/2
        return self.pt_lines_intersect(b, b+self.rotate_cw90(a-b), c, c+rotate_cw90(a-c))
    
    #mod for integer return later 
    def circle_has_point(self, a, b, r): return (self.euclidean_distance(a, b)<r)
    
    def circle_line_intersection(self, a, b, c, r):
        b,a=b-a,a-c
        A,B,C=self.dot_product(b,b), self.dot_product(a,b), self.dot_product(a,a)-r*r
        D=B*B-A*C
        if D<-EPS: return None
        rVal=c+a+b*(-B+math.sqrt(D+EPS))/A
        return (rVal) if not(D>EPS) else (rVal, c+a+b*(-B-math.sqrt(D))/A)
        
    def circle_circle_intersection(self, a, b, r1, r2):
        d=self.euclidean_distance(a, b)
        if d>r1+r2 or d+min(r1, r2)<max(r1,r2): return None
        x=(d*d-r2*r2+r1*r1)/(2*d)
        y=math.sqrt(r1*r1-x*x)
        v=(b-a)/d
        i,j=a+v*x,self.rotate_ccw90(v)*y
        return (i+j) if not(y>0) else (i+j, i-j)
    
    def triangle_area_2bh(self, b, h):
        return b*h/2
    
    def triangle_area_heron(self, ab, bc, ca):
        s=self.triangle_perimeter(ab, bc, ca)*0.5
        return math.sqrt(s*(s-ab)*(s-bc)*(s-ca))
        
    def triangle_perimeter(self, ab, bc, ca):
        return ab+bc+ca
        
    def incircle_helper(self, ab, bc, ca):
        return self.triangle_area_heron(ab, bc, ca)/(self.triangle_perimeter(ab, bc, ca)*0.5)
    
    def triangle_incircle_radius(self, a, b, c):
        ab=self.euclidean_distance(a,b)
        bc=self.euclidean_distance(b,c)
        ca=self.euclidean_distance(c,a)
        return self.incircle_helper(ab,bc,ca)
    
    def circumcircle_helper(self, ab, bc, ca):
        return ab*bc*ca/(4*self.triangle_area_heron(ab,bc,ca))
        
    def triangle_circumcircle_radius(self, a, b, c):
        ab=self.euclidean_distance(a,b)
        bc=self.euclidean_distance(b,c)
        ca=self.euclidean_distance(c,a)
        return self.circumcircle_helper(ab,bc,ca)
    
    # def triangle_incircle(self, a, b, c):
    #     r=self.triangle_incircle_radius(a,b,c)
    #     if abs(r)<EPS: return (False,0,0)
    #     ratio=self.euclidean_distance(a,b)/self.euclidean_distance(a,c)
    #     p1=b+(c-b)*(ratio/(1.0+ratio))
        
    #     ratio=self.euclidean_distance(a,b)/self.euclidean_distance(b,c)
    #     p2=a+(c-a)*(ratio/(1.0+ratio))
    #     if self.is_lines_intersect(a,p1,b,p2): return (True, r, round(self.pt_lines_intersect(a,p1,b,p2),12))
    #     else: return  (False,0,0)
    
    #center of triangle circle stuff 
    
    def triangle_circle_center(self, a, b, c, d):
        p1,p2=b-a,d-c
        p1=pt_xy(p1.y,-p1.x)
        p2=pt_xy(p2.y,-p2.x)
        c12,c21=self.cross_product(p1,p2),self.cross_product(p2,p1)
        if self.epscmp(c12)==0: return None # doesnt exist? colined <=> a1*c2-a2*c1=0 && b1*c2-b2*c1=0
        p3=pt_xy(self.dot_product(a,p1), self.dot_product(c,p2))
        return pt_xy((p3.x*p2.y-p3.y*p1.y)/c12,(p3.x*p2.x-p3.y*p1.x)/c21)
        
    
    def triangle_angle_bisector(self, a, b, c):
        val=(b-a)/math.sqrt(self.dist2(b,a))*math.sqrt(self.dist2(c,a))
        return val+(c-a)+a
    
    def triangle_perpendicular_bisector(self, a, b):
        v=b-a
        v.x,v.y=-v.y,v.x
        return v+(a+b)/2
        
    def triangle_incenter(self, a, b, c):
        v1=self.triangle_angle_bisector(a,b,c)
        v2=self.triangle_angle_bisector(b,c,a)
        return self.triangle_circle_center(a, v1, b, v2)
    
    def triangle_circumcenter(self, a, b, c):
        v1=self.triangle_perpendicular_bisector(a,b)
        v2=self.triangle_perpendicular_bisector(b,c)
        return self.triangle_circle_center((a+b)/2, v1, (b+c)/2, v2)
    
    def triangle_orthocenter(self, a, b, c):
        return a+b+c-self.triangle_circumcenter(a,b,c)*2
    
    #note these are based on counter clowck wise ordering 
    #check for improvements on integers
    def polygon_perimeter(self, ps):#MARKED
        return math.fsum([self.euclidean_distance(ps[i], ps[i+1]) for i in range(len(ps)-1)])
    
    def polygon_signed_area(self, ps): #MARKED
        return math.fsum([self.cross_product(ps[i], ps[i+1]) for i in range(len(ps)-1)])/2
    
    def polygon_area(self, ps): #MARKED
        return abs(self.polygon_signed_area(ps))
    
    #notes for this function (subject to change)
    #test it obviously 
    #isLeft is for counter clockwise swapping rot=-1 goes for clock wise ordering
    #not modified for colinear points yet
    def polygon_convex(self, ps): #MARKED
        lim,rot=len(ps),1
        if lim<4: return False
        isLeft=(1==self.point_rotation_wrt_line(ps[0],ps[1],ps[2]))
        for i in range(rot, lim-1):
            if isLeft!=(rot==self.point_rotation_wrt_line(ps[i],ps[i+1],ps[i+1 if i+2<lim else 1])):
                return False
        return True
    
    #maybe change to not fsum but i think fsum good idea 
    def polygon_has_pt(self, ps, p): #MARKED
        if len(ps)<4: return 0
        tmp=[self.angle_abc(ps[i],p,ps[i+1]) for i in range(len(ps)-1)]
        soa=math.fsum([el if 1==self.point_rotation_wrt_line(ps[i],p,ps[i+1]) else -el for i,el in enumerate(tmp)])
        return (0==self.epscmp(abs(soa)-math.tau))

def main():
    obj=GEO_ALGOS()
    a=pt_xy(0,0)
    b=pt_xy(4,0)
    c=pt_xy(4,3)
    r=obj.triangle_incircle_radius(a,b,c)
    p1=obj.triangle_incenter(a,b,c)
    p2=obj.triangle_circumcenter(a,b,c)
    print(r)
    p1.display()
    p2.display()
main()
