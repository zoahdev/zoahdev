from math import gcd
from fractions import Fraction
import time

def cert(n,cap=4,L=None):
    if L is None:L=n
    m=n//6;q=n//2;f=n//2+n//3-n//6;M=f-q+1
    O=list(range(1,n+1,2));h=len(O)
    def phi(v):
        r=v;t=v;p=2
        while p*p<=t:
            if t%p==0:
                r=r//p*(p-1)
                while t%p==0:t//=p
            p+=1
        if t>1:r=r//t*(t-1)
        return r
    O.sort(key=lambda v:(-Fraction(phi(v),v),v))
    eb=[sum(1<<(k-1) for k in range(1,L//2+1) if gcd(k,v)==1) for v in O]
    fb=[sum(1<<(k-1) for k in range(1,L+1) if gcd(k,v)==1) for v in O]
    masks=[sum((1<<i) for i,p in enumerate([3,5,7,11][:cap]) if v%p==0) for v in O]
    se=[[q+1]*(h+1) for _ in range(cap+1)]
    sf=[[n+1]*(h+1) for _ in range(cap+1)]
    for k in range(2,h+1):
        for s in range(cap+1):
            se[s][k]=se[s][k-1];sf[s][k]=sf[s][k-1]
        for i in range(k-1):
            ce=(eb[k-1]&eb[i]).bit_count(); cf=(fb[k-1]&fb[i]).bit_count()
            diff=masks[k-1]^masks[i]
            for s in range(cap+1):
                if diff&((1<<s)-1):break
                se[s][k]=min(se[s][k],ce);sf[s][k]=min(sf[s][k],cf)
    fail=[]
    for b in range(h-M+1):
        for j in range(1,m+1):
            works=False
            for s in range(cap+1):
                cross=0 if s==0 else 2**s+1
                if j<=cross:continue
                k=h-b-(j-cross-1)//2
                if se[s][k]>=b+j or sf[s][k]>=n-f+m+j:
                    works=True;break
            if not works:fail.append((b,j));break
    return fail
if __name__=='__main__':
    st=time.process_time()
    for L,U in [(36,42),(60,66),(100,110),(180,200),(300,330),(500,550),(900,1000),(1800,2000),(2000,2200),(2000,2300)]:
        f=cert(U,L=L);print(L,U,'pass' if not f else 'FAIL',len(f),f[:8],flush=True)
    print('CPU',time.process_time()-st)
