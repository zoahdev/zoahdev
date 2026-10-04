from math import prod,isqrt
from collections import deque
import time

def primes_upto(N):
    a=bytearray(b'\1')*(N+1);a[:2]=b'\0\0'
    for p in range(2,isqrt(N)+1):
        if a[p]:a[p*p::p]=b'\0'*(((N-p*p)//p)+1)
    return [i for i in range(3,N+1,2) if a[i]]
def phis(N):
    a=list(range(N+1))
    for p in range(2,N+1):
        if a[p]==p:
            for k in range(p,N+1,p):a[k]-=a[k]//p
    return a

def cert_interval(L,U,verbose=False,ph=None):
    if ph is None:ph=phis(U)
    assert len(ph)>U
    ps=primes_upto(1000)
    m=U//6;H=(U+1)//2;f=U//2+U//3-U//6;M=f-U//2+1;bmax=H-M;D=U-f+m
    pp=1;r=0
    for p in ps:
        if pp*p>U*U:break
        pp*=p;r+=1
    else:raise AssertionError("Prime list exhausted in IE cutoff")
    e=2**(r-1)-1
    covered=[False]*(m+1);choices={}; fail=[]
    for s in range(0,min(20,m.bit_length())):
        h=0 if s==0 else 2**s+1
        if h>=m:break
        prodq=1;et_num=1;et_den=1;tail=[]
        for p in ps[s:]:
            if prodq*p>U:break
            prodq*=p;et_num*=p-1;et_den*=p;tail.append(p)
        else:raise AssertionError("Prime list exhausted in tail cutoff")
        # rho(v)*eta bounds rho(rad(uv)) for equal signatures.
        ze=bmax+m;zr=D+m
        ec=[0]*(ze+1);rc=[0]*(zr+1)
        for v in range(1,U+1,2):
            nv=et_num*ph[v];dv=et_den*v
            if ph[v]*et_den>=et_num*v:
                nv=ph[v]*ph[v];dv=v*v
            ed=max(-1,(L//2)*nv//dv-e);rd=max(-1,L*nv//dv-e)
            if ed<ze:ec[ed+1]+=1
            if rd<zr:rc[rd+1]+=1
        # E[z]=number of odds with lower common-neighbor degree <z
        # histogram index d+1: cumulative through z counts d<z.
        for z in range(1,ze+1):ec[z]+=ec[z-1]
        for z in range(1,zr+1):rc[z]+=rc[z-1]
        E=ec;R=rc
        Z=[E[z]-z for z in range(bmax+m+1)]
        dq=deque();pushed=-1;count=0;bad=[]
        for j in range(h+1,m+1):
            a=(j-h-1)//2
            # resource works for b >= R[D+j]-a, need E for smaller b.
            end=min(j+bmax,j+R[D+j]-a-1)
            if end<j:ok=True
            else:
                while pushed<end:
                    pushed+=1
                    while dq and Z[dq[-1]]<=Z[pushed]:dq.pop()
                    dq.append(pushed)
                while dq and dq[0]<j:dq.popleft()
                ok=Z[dq[0]]<=a-j
            if ok:
                covered[j]=True;choices.setdefault(j,s);count+=1
            else:bad.append(j)
        if verbose:print('s',s,'eta',et_num/et_den,'tail',tail,'e',e,'h',h,'covered',count,'firstbad',bad[:3],flush=True)
        if all(covered[1:]):break
    fail=[j for j in range(1,m+1) if not covered[j]]
    return {'L':L,'U':U,'failure_count':len(fail),'first_failed_ranks':fail[:20],'last_failed_ranks':fail[-10:]}
if __name__=='__main__':
    start=time.process_time()
    for L,U in [(2300,2300),(10000,10000),(100000,100000)]:
        print(cert_interval(L,U,True),flush=True)
    print('CPU',time.process_time()-start)
