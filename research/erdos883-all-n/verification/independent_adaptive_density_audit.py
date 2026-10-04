from math import gcd,isqrt,prod
from fractions import Fraction
from bisect import bisect_left
from pathlib import Path
import importlib.util,time
root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('fast',root/'adaptive_density_probe.py')
fast=importlib.util.module_from_spec(spec);spec.loader.exec_module(fast)
primes=[p for p in range(3,1000,2) if all(p%d for d in range(2,isqrt(p)+1))]

def slow(L,U):
    m=U//6;H=(U+1)//2;f=U//2+U//3-U//6;M=f-U//2+1;bmax=H-M;D=U-f+m
    w=0;P=1
    for p in primes:
        if P*p>U*U:break
        P*=p;w+=1
    delta=2**(w-1)-1
    rho=[Fraction(sum(gcd(v,z)==1 for z in range(1,v+1)),v) for v in range(1,U+1,2)]
    covered=set()
    for s in range(min(20,m.bit_length())):
        h=0 if s==0 else 2**s+1
        if h>=m:break
        eta=Fraction(1);P=1
        for p in primes[s:]:
            if P*p>U:break
            eta*=Fraction(p-1,p);P*=p
        E=sorted(int((L//2)*max(r*r,eta*r))-delta for r in rho)
        R=sorted(int(L*max(r*r,eta*r))-delta for r in rho)
        for j in range(h+1,m+1):
            a=(j-h-1)//2
            ok=True
            for b in range(bmax+1):
                if bisect_left(E,b+j)>b+a and bisect_left(R,D+j)>b+a:
                    ok=False;break
            if ok:covered.add(j)
    return [j for j in range(1,m+1) if j not in covered]

start=time.process_time()
cases=[(n,n) for n in range(6,81)]+[(36,42),(60,66),(93,102),(100,120)]
for L,U in cases:
    failure=slow(L,U);got=fast.cert_interval(L,U)
    assert got['failure_count']==len(failure),(L,U,got,failure)
    assert got['first_failed_ranks']==failure[:20]
    assert got['last_failed_ranks']==failure[-10:]
print('PASS: direct all-b/all-j rational audit matches fast deque criterion in',len(cases),'cases')
print('CPU seconds:',time.process_time()-start)
