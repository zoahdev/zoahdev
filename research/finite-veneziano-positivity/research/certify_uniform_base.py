#!/usr/bin/env python3
"""Exact finite certificates of infinitely many spins at selected n.
NOT a universal proof in n. All infinite Taylor tails are proved positive.
"""
from fractions import Fraction as Q
from math import factorial,comb
from pathlib import Path
import json,time

def partialfractions(n,k):
    out=[];a=n-k+1
    for r in range(a,n+1):
        A=Q(2,k)*comb(r+k,k)*Q(factorial(n),factorial(n-k))*Q((-1)**(r-a),factorial(r-a)*factorial(n-r))
        out.append((A,Q(k,k+2*r))) # R=constant + sum A*q/(1-q*x)
    return Q((-1)**k*comb(n,k)),out

def coefficients(n,k,M):
    c,pf=partialfractions(n,k)
    vals=[a*q for a,q in pf];out=[]
    for m in range(M+1):
        out.append(sum(vals)+(c if m==0 else 0));vals=[v*q for v,(_,q) in zip(vals,pf)]
    return out

def positive_tail_start(n,k):
    _,pf=partialfractions(n,k);a0,q0=pf[0];M=0
    vals=[a*q for a,q in pf]
    while vals[0] <= -sum(v for v in vals if v<0):
        M+=1; vals=[v*q for v,(_,q) in zip(vals,pf)]
        if M>2000:raise RuntimeError('tail search cap exceeded')
    return max(M,1)

def moments(d,N):
    out=[Q(1)]
    for r in range(N):out.append(out[-1]*Q(2*r+1)/(d+2*r-1))
    return out

def certify(n,k,d):
    M0=positive_tail_start(n,k);a=coefficients(n,k,M0)
    negatives=[m for m,v in enumerate(a) if v<0]
    L=max(negatives,default=-1)
    # Exact Rodrigues projections: all terms after M0 are positive.
    # G_j has same sign as partial wave j and is sum a_m binom(m,j) M_((m-j)/2)(D+2j).
    M=max(M0,64);fails=[]
    while True:
        a=coefficients(n,k,M);mins=[];fails=[]
        for j in range(L+1):
            mom=moments(d+2*j,(M-j)//2)
            val=sum(a[m]*comb(m,j)*mom[(m-j)//2] for m in range(j,M+1,2))
            if val<=0:fails.append(j)
            mins.append(float(val))
        if not fails:return dict(n=n,k=k,D_cap=str(d),positive_tail_from=M0,last_negative_Taylor_degree=L,certificate_degree=M,min_Rodrigues_projection_lower_bound=min(mins,default=0))
        if M>=512:return dict(n=n,k=k,D_cap=str(d),status='not certified',failed_spins=fails,positive_tail_from=M0,last_negative_Taylor_degree=L,values=mins)
        M*=2

def scalar_upper(n,d,J=100):
    c,pf=partialfractions(n,3);a=coefficients(n,3,2*J);mom=moments(d,J)
    low=sum(a[2*j]*mom[j] for j in range(J+1))
    tail=sum(A*q*(q*q)**(J+1)/(1-q*q) for A,q in pf if A>0)
    assert low+tail<0
    if n==35 and d==Q(51,5): assert low+tail<Q(-3,100000)
    return float(low),float(low+tail)

def find_cap(n):
    # Exact bisection of the normalized level-three scalar. Upper bracket is negative.
    lo=Q(10);hi=Q(14);J=80
    _,pf=partialfractions(n,3);a=coefficients(n,3,2*J)
    tail=sum(A*q*(q*q)**(J+1)/(1-q*q) for A,q in pf if A>0)
    while hi-lo>Q(1,100000):
        mid=(lo+hi)/2;mom=moments(mid,J)
        low=sum(a[2*j]*mom[j] for j in range(J+1))
        if low>0:lo=mid
        elif low+tail<0:hi=mid
        else:raise RuntimeError('Need sharper scalar enclosure')
    return hi
caps={n:find_cap(n) for n in range(3,35)}
if __name__=='__main__':
    rows=[];bounds=[];start=time.time()
    for n,cap in caps.items():
        d=Q(cap);bounds.append(dict(n=n,D_cap=str(cap),level3_scalar_interval=scalar_upper(n,d)))
        for k in range(1,n+1):
            if k==3:continue
            r=certify(n,k,d);rows.append(r)
            if 'status' in r: print('FAIL',r,flush=True)
        print('completed n',n,'cap',float(d),'elapsed',round(time.time()-start,2),flush=True)
    assert not any('status' in r for r in rows), 'Uncertified rows remain'
    cutoff=scalar_upper(35,Q(51,5))
    out=dict(uniform_cutoff={'n':35,'D':'51/5','scalar_interval':cutoff},status='Exact finite base n=3..34 for the separately proved uniform n>=35 reduction',method='exact rational partial fractions, dominant nearest pole proves positive Taylor tail, finite positive Rodrigues lower bounds',caps=bounds,rows=rows)
    Path(__file__).with_name('uniform_base_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
    print('total',len(rows),'failures',sum('status' in r for r in rows))
