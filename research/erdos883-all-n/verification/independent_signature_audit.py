from math import gcd, prod
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import importlib.util,time
ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('original',ROOT/'interval_profile_probe.py')
original=importlib.util.module_from_spec(spec);spec.loader.exec_module(original)

def independent(L,U):
    odds=sorted(range(1,U+1,2),key=lambda v:(-Fraction(sum(gcd(v,i)==1 for i in range(1,v+1)),v),v))
    H=len(odds);m=U//6;q=U//2;f=q+U//3-m;M=f-q+1
    pairs={}
    for x,y in combinations(odds,2):
        e=sum(gcd(x,z)==gcd(y,z)==1 for z in range(2,L+1,2))
        r=sum(gcd(x,z)==gcd(y,z)==1 for z in range(1,L+1))
        s=0
        for p in [3,5,7,11]:
            if (x%p==0)!=(y%p==0):break
            s+=1
        pairs[x,y]=(e,r,s)
    profiles={}
    for k in range(1,H+1):
        for s in range(5):
            good=[pairs[x,y] for x,y in combinations(odds[:k],2) if pairs[x,y][2]>=s]
            profiles[s,k]=(min((v[0] for v in good),default=q+1),min((v[1] for v in good),default=U+1))
    fails=[]
    for b in range(H-M+1):
        for j in range(1,m+1):
            passed=False
            for s in range(5):
                cross=0 if s==0 else 2**s+1
                for k in range(1,H+1):
                    if 2*max(0,H-k-b)+cross>=j:continue
                    e,r=profiles[s,k]
                    if e>=b+j or r>=U-f+m+j:passed=True;break
                if passed:break
            if not passed:fails.append((b,j));break
    return fails

start=time.process_time()
for U in range(6,65):
    got=independent(U,U); want=original.cert(U)
    assert got==want,(U,got,want)
for L,U in [(6,8),(24,28),(36,42),(60,66)]:
    got=independent(L,U);want=original.cert(U,L=L)
    assert got==want,(L,U,got,want)
P=[13,17,19,23,29,31,37,41]
Q=[p for p in range(43,228) if all(p%d for d in range(2,int(p**.5)+1))]
x=prod(P);y=prod(Q);t=x*y;px=prod(p-1 for p in P);py=prod(p-1 for p in Q)
assert gcd(x,y)==1 and 3*px>2*x and 3*py>2*y and 2*px*py<t
assert all(x%p and y%p for p in [3,5,7,11])
print('Independent profiles agree for every n=6..64 and four intervals.')
print('Fixed-signature obstruction exact arithmetic verified.')
print('x=',x,'y=',y,'t=',t,'n=',12*t)
print('CPU seconds:',time.process_time()-start)
