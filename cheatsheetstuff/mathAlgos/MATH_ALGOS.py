#is_prime tested on primes2
#lcm/gcd tested on temperatureconfusion, primes2, dasblinkenlights, jackpot, prsteni, smallestmultiple, jughard
#extendedEuclid tested on candydistribution, modulararithmetic

class MATH_ALGOS:
    def __init__(self):
        self.n=None
    
    def set_N(self, val):
        self.N=val
    
    def is_prime(self, n):
        if n<=3:
            return n>1
        elif n%2==0 or n%3==0:
            return False
        p=5
        while p*p<=n:
            if n%p==0 or n%(p+2)==0:
                return False
            p+=6
        return True
    
    def gcd(self, u, v):
        while v:
            u,v=v,u%v
        return abs(u)

    def lcm(self, u, v):
        return u*v//self.gcd(u,v)
    
    def Sieve(self, n):
        pb=[True]*n
        self.ps=[2]
        for i in range(4, n, 2):
            pb[i]=False
        for i in range(3, n, 2):
            if pb[i]:
                self.ps.append(i)
                for j in range(i*i, n, 2*i):
                    pb[j]=False
    
    def pFactorize(self, n):
        facts=[]
        for p in self.ps:
            if p*p>n:
                break
            if n%p==0:
                facts.append(p)
                while n%p==0:
                    n//=p
        if n>1:
            facts.append(n)
        return facts
    
    def extendedEuclid(self, a, b):
        if b==0:
            return 1,0,a
        x,y,d=self.extendedEuclid(b, a%b)
        return y, x-y*(a//b), d
    
