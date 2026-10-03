#!/usr/bin/env python3
"""Independent audit of finite all-spin certificates.
Rebuilds Taylor coefficients by polynomial division, checks partial fractions
as a complete polynomial identity, and evaluates exact monomial projections.
Does not import the candidate implementation.
"""
from fractions import Fraction as Q
from math import comb,factorial
from pathlib import Path
import json,time,sys
from functools import lru_cache
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parent.parent/'research'
data=json.loads((root/'uniform_base_certificates.json').read_text())

def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):out[i+j]+=u*v
 return out

def prod(factors):
 out=[Q(1)]
 for f in factors:out=mul(out,f)
 return out

def residue_polys(n,k):
 # Directly from binom(t+k,k) product r/(r-t), t=k(x-1)/2.
 num=prod([[Q(2*i-k,2),Q(k,2)] for i in range(1,k+1)])
 factor=Q(factorial(n),factorial(n-k)*factorial(k))
 num=[c*factor for c in num]
 den=prod([[Q(2*r+k,2),-Q(k,2)] for r in range(n-k+1,n+1)])
 return num,den

def series(num,den,M):
 out=[]
 for m in range(M+1):
  rhs=num[m] if m<len(num) else Q(0)
  rhs-=sum(den[i]*out[m-i] for i in range(1,min(m,len(den)-1)+1))
  out.append(rhs/den[0])
 return out

def pf_exact(n,k):
 a=n-k+1;polys=[[Q(k+2*r,k),Q(-1)] for r in range(a,n+1)]
 den=prod(polys)
 C=Q((-1)**k*comb(n,k));reconstructed=[C*c for c in den]
 terms=[]
 for index,r in enumerate(range(a,n+1)):
  zz=Q(k+2*r,k)
  # Residue numerator evaluated directly in the angular variable,
  # divided by all remaining angular denominator factors.
  nup,dep=residue_polys(n,k)
  scale=Q(k,2)**k
  nvalue=sum(c*zz**i for i,c in enumerate(nup))/scale
  others=Q(1)
  for ss in range(a,n+1):
   if ss!=r:others*=Q(k+2*ss,k)-zz
  A=nvalue/others
  claimed=Q(2,k)*comb(r+k,k)*Q(factorial(n),factorial(n-k))*Q((-1)**(r-a),factorial(r-a)*factorial(n-r))
  assert A==claimed
  contribution=prod(polys[:index]+polys[index+1:])
  for i,c in enumerate(contribution):reconstructed[i]+=A*c
  terms.append((A,1/zz))
 num,den0=residue_polys(n,k)
 assert [c*Q(k,2)**k for c in reconstructed]==num
 assert [c*Q(k,2)**k for c in den]==den0
 return C,terms

@lru_cache(maxsize=None)
def moment(d,r):
 ans=Q(1)
 for u in range(r):ans*=Q(2*u+1)/(d+2*u-1)
 return ans

def projection_lower(a,j,d):
 # Independently apply explicit monomial Gegenbauer connection formula.
 # Rescale by the positive coefficient of C_j in x^j.
 # Coefficient ratio for m=j+2r is binom(j+2r,j) * (1/2)_r / ((D+2j-1)/2)_r.
 return sum(a[m]*comb(m,j)*moment(d+2*j,(m-j)//2) for m in range(j,len(a),2))

start=time.time();rows=[];smallest=None
for row in data['rows']:
 n,k=row['n'],row['k'];M0=row['positive_tail_from'];M=row['certificate_degree'];d=Q(row['D_cap'])
 assert M>=M0>=1
 num,den=residue_polys(n,k);a=series(num,den,M)
 C,pf=pf_exact(n,k)
 assert all(a[m]==sum(A*q**(m+1) for A,q in pf)+(C if m==0 else 0) for m in range(M+1))
 A0,q0=pf[0]
 assert A0>0 and all(Q(0)<q<q0 for A,q in pf[1:]) and q0<1
 dominant=A0*q0**(M0+1)-sum(-A*q**(M0+1) for A,q in pf if A<0)
 assert dominant>0
 assert all(c>0 for c in a[M0:])
 L=max((i for i,c in enumerate(a) if c<0),default=-1)
 assert L==row['last_negative_Taylor_degree'] and L<M0
 vals=[projection_lower(a,j,d) for j in range(L+1)]
 assert all(v>0 for v in vals)
 if vals:
  val=min(vals)
  if smallest is None or val<smallest[0]:smallest=(val,n,k)
 rows.append(dict(n=n,k=k,D_cap=str(d),tail_from=M0,last_negative=L,M=M,tail_dominance_margin=str(dominant),low_spin_exact_bounds=[str(v) for v in vals]))
 print('pass',n,k,flush=True)
# Recheck cap > root direction by an independent direct polynomial series and PF upper tail.
caprows=[]
for row in data['caps']:
 n=row['n'];d=Q(row['D_cap']);J=100
 num,den=residue_polys(n,3);a=series(num,den,2*J);_,pf=pf_exact(n,3)
 partial=sum(a[2*r]*moment(d,r) for r in range(J+1))
 tail=sum(A*q*q**(2*J+2)/(1-q*q) for A,q in pf if A>0)
 assert partial+tail<0
 caprows.append(dict(n=n,D_cap=str(d),scalar_strict_upper=str(partial+tail)))

assert len(rows)==560 and {(r['n'],r['k']) for r in rows}=={(n,k) for n in range(3,35) for k in range(1,n+1) if k!=3}
assert len({(r['n'],r['k']) for r in rows})==len(rows)
assert {r['n'] for r in caprows}==set(range(3,35))
capmap={r['n']:Q(r['D_cap']) for r in caprows}
assert all(Q(r['D_cap'])==capmap[r['n']] for r in rows)
num,den=residue_polys(35,3);coefs=series(num,den,200);_,pf=pf_exact(35,3);dim=Q(51,5)
cut_partial=sum(coefs[2*r]*moment(dim,r) for r in range(101))
cut_tail=sum(A*q*q**202/(1-q*q) for A,q in pf if A>0)
assert cut_partial+cut_tail<0
cutoff={'n':35,'D':'51/5','exact_strict_upper':str(cut_partial+cut_tail)}
# Symbolically independent finite connection formula sanity checks, exact rational parameters.
# Infinite-spin dimension descent uses its general positive-parameter identity.
import sympy as s
x=s.symbols('x');mu=s.Rational(1,2);nu=s.Rational(361,100)
for ell in range(12):
 rhs=sum(s.rf(nu,ell-r)*s.rf(nu-mu,r)*(ell-2*r+mu)/(s.rf(mu,ell-r+1)*s.factorial(r))*s.gegenbauer(ell-2*r,mu,x) for r in range(ell//2+1))
 assert s.expand(s.gegenbauer(ell,nu,x)-rhs)==0
out={'status':'PASS independent exact reconstruction and all-spin finite certificates',
'uniform_cutoff':cutoff,'num_residues':len(rows),'caps':caprows,'rows':rows,'smallest_positive_rescaled_projection':str(smallest[0]),
'smallest_at':list(smallest[1:]),'elapsed_seconds':time.time()-start}
Path(__file__).with_name('independent_uniform_base.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(rows),'residues; smallest exact projection',float(smallest[0]),'at',smallest[1:],'seconds',time.time()-start)
